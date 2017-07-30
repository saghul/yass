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
import threading
import dbconfig
import DNS
from pysqlite2 import dbapi2 as sqlite
from account import yass_account
from net import yass_net
from buddy import yass_buddy
from error import YassException

class yass_sysconfig(object):
    """ Class containing different configuration objects:
            * ua: PJSIP UAConfig, containing User-Agent configuration.
            * media: PJSIP MediaConfig, containing multimedia configuration.
            * log: PJSIP LogConfig, containing logging configuration.
            * acc: yass_account class object, containing Account configuration settings.
            * net: yass_net class object, containing the network configuration.

        Configuration is loaded from SQLite database.

        The configuration class is a thread-safe singleton, so we have ONLY ONE instance for the whole application.
    """

    class __impl(object):

        ## Getters/setters.
        def _get_ua(self):
            return self._ua
        
        def _set_ua(self, ua):
            self._ua = ua

        ua = property(_get_ua, _set_ua)

        def _get_media(self):
            return self._media

        def _set_media(self, media):
            self._media = media

        media = property(_get_media, _set_media)

        def _get_log(self):
            return self._log

        def _set_log(self, log):
            self._log = log

        log = property(_get_log, _set_log)

        def _get_acc(self):
            return self._acc

        def _set_acc(self, acc):
            self._acc = acc

        acc = property(_get_acc, _set_acc)
        
        def _get_net(self):
            return self._net

        def _set_net(self, net):
            self._net = net

        net = property(_get_net, _set_net)

        def _get_buddies(self):
            return self._buddies

        def _set_buddies(self, buddies):
            self._buddies = buddies

        buddies = property(_get_buddies, _set_buddies)


        ## Presence related config functions
        def load_buddies(self):
            try:
                self.buddies = []
                con = sqlite.connect(dbconfig.DB_BUDDIES)
                for row in con.execute("SELECT name, uri, subscribed FROM buddies"):
                    b = yass_buddy(str(row[0]), str(row[1]), None)
                    if int(row[2]) == 1:
                        b.subscribed = True
                    self.buddies.append(b)
                con.close()
            except sqlite.Error:
                raise YassException("SIMPLE", "004", "Error loading buddies from DB.")

        def find_buddy(self, text):
            for b in self.buddies:
                if b.name == str(text) or b.uri == str(text):
                    return b
            return None

        def update_buddy(self, buddy):
            for b in self.buddies:
                if b.name == buddy.name:
                    self.buddies.remove(b)
                    self.buddies.append(buddy)
                    break
        
        def toggle_buddy_subscription(self, buddy):
            try:
                con = sqlite.connect(dbconfig.DB_BUDDIES)
                con.isolation_level = None
                con.execute("UPDATE buddies SET subscribed='%s' WHERE uri='%s'" % (int(buddy.subscribed), buddy.uri))
                con.close()
            except sqlite.Error:
                raise YassException("SIMPLE", "007", "Error storing buddy subscription status.")

        def add_buddy(self, buddy):
            try:
                con = sqlite.connect(dbconfig.DB_BUDDIES)
                con.isolation_level = None
                for row in con.execute("SELECT COUNT(*) FROM buddies WHERE name='%s' OR uri='%s'" % (buddy.name, buddy.uri)):
                    if row[0] > 0:
                        raise YassException("SIMPLE", "006", "Error adding buddy, duplicated name or URI.")
                    else:
                        con.execute("INSERT INTO buddies(name, uri, subscribed) VALUES('%s', '%s', %d)" % (buddy.name, buddy.uri, int(buddy.subscribed)))
                        self.buddies.append(buddy)
                con.close()
            except sqlite.Error:
                raise YassException("SIMPLE", "003", "Error adding buddy.")

        def delete_buddy(self, name):
            try:
                for b in self.buddies:
                    if b.name == name:
                        self.buddies.remove(b)
                con = sqlite.connect(dbconfig.DB_BUDDIES)
                con.isolation_level = None
                con.execute("DELETE FROM buddies WHERE name='%s'" % name)
                con.close()
            except sqlite.Error:
                raise YassException("SIMPLE", "005", "Error deleting buddy.")


        ## Configuration loading/reloading
        def reload_acc(self):
            self.acc = yass_account()

        def reload_config(self):
            self.ua = pj.UAConfig()
            self._load_config(self.ua, "ua")
            self.ua.nameserver = self._get_nameservers()

            self.media = pj.MediaConfig()
            self._load_config(self.media, "media")

            self.log = pj.LogConfig()
            self._load_config(self.log, "log")

            self.net = yass_net()
            self._load_config(self.net, "net")

        def _load_config(self, obj, table):
            try:
                con = sqlite.connect(dbconfig.DB_CONFIG)
                for row in con.execute("SELECT opt, val FROM %s" % table):
            	    if str(row[1]).isdigit():
            	        obj.__dict__[str(row[0])] = int(row[1])
            	    else:
            	        obj.__dict__[str(row[0])] = str(row[1])
                con.close()
            except sqlite.Error:
                raise YassException("CFG", "001", "Error loading configuration.")

        def _get_nameservers(self):
            try:
                DNS.ParseResolvConf()
                return DNS.defaults['server']
            except:
                return []


        ## Initialize sysconfig configuration.
        def __init__(self):
            self.ua = pj.UAConfig()
            self._load_config(self.ua, "ua")
            self.ua.nameserver = self._get_nameservers()

            self.media = pj.MediaConfig()
            self._load_config(self.media, "media")

            self.log = pj.LogConfig()
            self._load_config(self.log, "log")
            
            self.acc = yass_account()

            self.net = yass_net()
            self._load_config(self.net, "net")

            self.buddies = []
            self.player = -1


    ## Private attributes for holding the instance and the lock.
    __instance = None
    __lock = threading.Lock()
    

    ## Initialize the ONLY sysconfig instance (if needed).
    def __init__(self):
        yass_sysconfig.__lock.acquire(True)
        try:
            if yass_sysconfig.__instance is None:
                yass_sysconfig.__instance = yass_sysconfig.__impl()
        finally:
            yass_sysconfig.__lock.release()
        
    
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

