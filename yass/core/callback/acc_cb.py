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
import os
from yass.core.core import yass_core
from yass.core.error import YassException
from yass.core.callback.util.regstate import yass_regstate
from yass.core.callback.util.call_info import yass_call_info
from yass.core.callback.util.sip_message import yass_message

class yass_acc_cb(pj.AccountCallback):
    """ Class for wrapping PJSIP AccountCallbak. It implements the following callbacks:
            * on_teg_state
            * on_incoming_call
            * on_pager
    """

    def __init__(self, account=None):
        pj.AccountCallback.__init__(self, account)
        self.core = yass_core()
 
    def on_reg_state(self):
        acc_info = self.account.info()
        reg_state = yass_regstate(str(acc_info.uri), str(acc_info.reg_status), str(acc_info.reg_reason))
        self.core.cb.regstate(reg_state)

    def on_incoming_call(self, call):
        if self.core.calls.current:
            call.answer(486, "Busy")
            return
        else:
            dev_error = False
            try:
                self.core.dev.set_stored_dev()
                sound_files = ["/usr/share/yass/sounds/ring.wav",
                                os.path.join(os.path.join(os.environ['HOME'], '.yass'), "ring.wav"),
                                os.path.join(os.path.dirname(__file__), "../../sounds/ring.wav")]

                for sf in sound_files:
                    if os.path.isfile(sf):
                        self.core.cfg.player = self.core.lib.create_player(sf, True)
                        self.core.lib.conf_connect(self.core.lib.player_get_slot(self.core.cfg.player), 0)
                        break

            except YassException:
                dev_error = True
                self.core.dev.set_null_dev()
            finally:
                self.core.calls.current = call
                from call_cb import yass_call_cb
                self.core.calls.current.set_callback(yass_call_cb())        
                self.core.calls.current.answer(180)
                
                info = call.info()
                call_info = yass_call_info(str(info.remote_uri))
                self.core.cb.incoming_call(call_info, dev_error)

    def on_pager(self, from_uri, contact, mime_type, body):
        msg = yass_message(from_uri, contact, mime_type, body)
        self.core.cb.incoming_message(msg)

if __name__ == "__main__":
    pass

