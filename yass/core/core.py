# -*- coding: utf-8 -*-

# Copyright 2008, 2009 Saúl Ibarra <saghul@gmail.com>
# This file is part of YASS.
# 
# YASS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# YASS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with YASS.  If not, see <http://www.gnu.org/licenses/>.



import pjsua as pj
import sys
import threading
import re
import codecs
import dbconfig
import yass.util.sip as sip_utils
import yass.modules.callhistory as mod_callhistory
from sysconfig import yass_sysconfig
from device import yass_devices
from core_callbacks import yass_cb
from call import yass_call
from buddy import yass_buddy
from error import YassException

class yass_core(object):
    """ Class holding the heart of YASS. It contains the following objects:
            * lib: PJSIP Lib instance.
            * cfg: yass_sysconfig class instance, containing yass configuration.
            * transport: PJSIP Transport object.
            * acc: PJSIP Account class instance, containing the real account object.
            * calls: yass_call class instance, for keeping track of calls in the system.
            * cb: yass_cb class instance containing the core callbacks.
            * dev: yass_devices class, for managing soundcard configuration.

        It also contains the main functions for making calls, etc:
            * make_call
            * answer_call
            * hold_call
            * unhold_call
            * hangup_call
            * reject_call
            * send_dtmf
            * blind_xfer

        It's a thread-safe singleton, we just want ONE single core instance for the whole application.
    """

    ## Class for holding the *real* core implementation.
    class __impl(object):

        ## Getters/setters
        def _get_lib(self):
            return self._lib
    
        def _set_lib(self, lib):
            self._lib = lib
    
        lib = property(_get_lib, _set_lib)
    
        def _get_cfg(self):
            return self._cfg
    
        def _set_cfg(self, cfg):
            self._cfg = cfg
    
        cfg = property(_get_cfg, _set_cfg)
        
        def _get_transport(self):
            return self._transport
    
        def _set_transport(self, transport):
            self._transport = transport
    
        transport = property(_get_transport, _set_transport)
    
        def _get_acc(self):
            return self._acc
    
        def _set_acc(self, acc):
            self._acc = acc
    
        acc = property(_get_acc, _set_acc)
        
        def _get_calls(self):
            return self._calls
    
        def _set_calls(self, calls):
            self._calls = calls
    
        calls = property(_get_calls, _set_calls)
    
        def _get_cb(self):
            return self._cb
    
        def _set_cb(self, cb):
            self._cb = cb
    
        cb = property(_get_cb, _set_cb)
    
        def _get_dev(self):
            return self._dev
    
        def _set_dev(self, dev):
            self._dev = dev
    
        dev = property(_get_dev, _set_dev)
    

        ## Start/stop/reload the core.
        def start(self):
            try:
                self._start_lib()
                self._start_acc()
                self.load_buddies()
            except pj.Error:
                raise YassException("CORE", "002", "Error starting the core.")
    
        def stop(self):
            try:
                self.lib.hangup_all()
                self._stop_acc()
                self.transport = None
                self._stop_lib()
            except pj.Error:
                raise YassException("CORE", "003", "Error stoping the core.")
    
        def restart_core(self):
            try:
                self.stop()
                self.cfg.reload_config()
                self.cfg.reload_acc()
                self.lib = pj.Lib()
                self.start()
            except pj.Error:
                raise YassException("CORE", "004", "Error restarting the core.")
            
        def _bind(self):
            try:
                t = pj.TransportConfig()
                t.bound_addr = self.cfg.net.bindaddr
                t.port = self.cfg.net.bindport
                if self.cfg.acc.acc.acc_transport == "tcp":
                    self.transport = self.lib.create_transport(pj.TransportType.TCP, t)
                else:
                    self.transport = self.lib.create_transport(pj.TransportType.UDP, t)
            except pj.Error:
                raise YassException("CORE", "001", "Error creating transport.")
        
        def _start_lib(self):
            self.lib.init(ua_cfg=self.cfg.ua, log_cfg=self.cfg.log, media_cfg=self.cfg.media)
            self._bind()
            self.lib.start()
            self.dev = yass_devices(self.lib)
            codecs.load_codecs()
    
        def _stop_lib(self):
            if self.lib:
                self.lib.destroy()
                self.lib = None
            self.dev = None
    
        def _start_acc(self):
            from callback.acc_cb import yass_acc_cb
            try:
                if self.cfg.acc.ready:
                    self.acc = self.lib.create_account(acc_config=self.cfg.acc.acc, cb=yass_acc_cb())
                    status = bool(int(self.cfg.acc.p_online))
                    self.set_presence_status(status, self.cfg.acc.p_text)
            except pj.Error:
                raise YassException("ACC", "001", "Error creating account.")
        
        def _stop_acc(self):
            if self.acc is not None:
                self.acc.delete()
    
        def restart_acc(self):
            self._stop_acc()
            self.cfg.reload_acc()
            self._start_acc()
        

        ## Telephony related functions.
        def make_call(self, dsturi):
            if self.calls.current:
                pass
            else:
                try:
                    self.dev.set_stored_dev()
                    dsturi = sip_utils.make_uri(dsturi, self.cfg.acc.acc.acc_domain)
                    if not sip_utils.check_uri(dsturi):
                        raise YassException("SIP", "001", "Invalid SIP URI.")

                    from callback.call_cb import yass_call_cb
                    call = self.acc.make_call(dsturi,cb=yass_call_cb())
                    self.calls.current = call
                    num = sip_utils.get_user_from_uri(dsturi)
                    mod_callhistory.update_history(num, 1)
                except pj.Error:
                    raise YassException("CALL", "001", "Couldn't make the call.")
    
        def answer_call(self, call):
            if call:
                if self.cfg.player > -1:
                    self.lib.conf_disconnect(self.lib.player_get_slot(self.cfg.player), 0)
                    self.lib.player_destroy(self.cfg.player)
                    self.cfg.player = -1
                    call.answer()
                    num = sip_utils.get_user_from_uri(str(call.info().remote_uri))
                    mod_callhistory.update_history(num, 0)
            else:
                raise YassException("CALL", "002", "Not an active call.")
    
        def hangup_call(self, call):
            if call:
                call.hangup()
            else:
                raise YassException("CALL", "002", "Not an active call.")
        
        def reject_call(self, call):
            if call:
                call.answer(486, "Busy")
            else:
                raise YassException("CALL", "002", "Not an active call.")
    
        def hold_call(self, call):
            if call:
                call.hold()
            else:
                raise YassException("CALL", "002", "Not an active call.")
    
        def unhold_call(self, call):
            if call:
                call.unhold()
            else:
                raise YassException("CALL", "002", "Not an active call.")
    
        def send_dtmf(self, call, digit):
            if call:
                try:
                    if self.cfg.media.dtmfmode == "rfc2833":
                        call.dial_dtmf(digit)
                    elif self.cfg.media.dtmfmode == "info":
                        body = "Signal=%s\r\nDuration=100\r\n" % digit
                        call.send_request("INFO", None, "application/dtmf-relay", body)
                except pj.Error:
                    pass
            else:
                raise YassException("CALL", "002", "Not an active call.")
    
        def blind_xfer(self, call, dst):
            try:
                dsturi = sip_utils.make_uri(dst, self.cfg.acc.acc.acc_domain)
                call.transfer(str(dsturi))
                call.hangup()
            except pj.Error:
                raise YassException("CALL", "003", "Error during call transfer.")


        ## Presence related functions.
        def set_basic_status(self, status):
            try:
                self.acc.set_basic_status(status)
            except pj.Error:
                raise YassException("SIMPLE", "001", "Error setting basic presence status.")
        
        def set_presence_status(self, status, descr=""):
            try:
                self.acc.set_presence_status(is_online=status, pres_text=descr)
            except pj.Error:
                raise YassException("SIMPLE", "002", "Error setting presence status.")
    
        def load_buddies(self):
            if self.acc is not None:
                from callback.buddy_cb import yass_buddy_cb
                self.cfg.load_buddies()
                tmp = []
                for b in self.cfg.buddies:
                    new_b = self.acc.add_buddy(b.uri, cb=yass_buddy_cb())
                    new_buddy = yass_buddy(b.name, b.uri, new_b)
                    if b.subscribed:
                        new_buddy.buddy.subscribe()
                        new_buddy.subscribed = True
                    tmp.append(new_buddy)
    
                for b in tmp:
                    self.cfg.update_buddy(b)
    
        def add_buddy(self, name, uri):
            uri = sip_utils.make_uri(uri, self.cfg.acc.acc.acc_domain)
            if not sip_utils.check_uri(uri):
                raise YassException("SIP", "001", "Invalid SIP URI.")

            from callback.buddy_cb import yass_buddy_cb
            try:
                b = self.acc.add_buddy(uri, cb=yass_buddy_cb())
                buddy = yass_buddy(name, uri, b)
                self.cfg.add_buddy(buddy)
                self.toggle_subscription(buddy)
            except pj.Error:
                raise YassException("SIMPLE", "003", "Error adding buddy.")        
    
        def delete_buddy(self, name):
            for b in self.cfg.buddies:
                if b.name == name:
                    if b.subscribed:
                        b.buddy.unsubscribe()
                    break
            self.cfg.delete_buddy(name)    
    
        def toggle_subscription(self, buddy):
            if buddy.subscribed:
                buddy.buddy.unsubscribe()
                buddy.subscribed = False
            else:
                buddy.buddy.subscribe()
                if buddy.buddy.info().subscribed:
                    buddy.subscribed = True
            self.cfg.toggle_buddy_subscription(buddy)
            self.cfg.update_buddy(buddy)
   

        ## Instant Messaging related functions
        def send_message(self, uri, body):
            uri = sip_utils.make_uri(uri, self.cfg.acc.acc.acc_domain)
            if not sip_utils.check_uri(uri):
                raise YassException("SIP", "001", "Invalid SIP URI.")
            try:
                self.acc.send_pager(uri=uri, text=body)
            except pj.Error:
                raise YassException("IM", "001", "Error sending MESSAGE request.")


        ## Initialize YASS confiiuration.
        def __init__(self):
            dbconfig.init_databases()
            try:
                self.lib = pj.Lib()
            except pj.Error:
                raise YassException("CORE", "005", "Error initialising library.")
            
            try:
                self.cfg = yass_sysconfig()
            except:
                raise YassException("CORE", "006", "Error initialising configuration.")
    
            self.calls = yass_call()
            self.cb = yass_cb()
            self.transport = None
            self.acc = None
            self.dev = None


    ## Private attributes for holding the instance and the lock.
    __instance = None
    __lock = threading.Lock()
    

    ## Initialize the ONLY core instance (if needed).
    def __init__(self):
        yass_core.__lock.acquire(True)
        try:
            if yass_core.__instance is None:
                yass_core.__instance = yass_core.__impl()
        finally:
            yass_core.__lock.release()
        
    
    ## Delegate access to implementation.
    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    ## Delegate access to implementation.
    def __delattr__(self, attr):
        return delattr(self.__instance, attr)
    
    ## Delegate access to implementation.
    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)


if __name__ == "__main__":
    pass

