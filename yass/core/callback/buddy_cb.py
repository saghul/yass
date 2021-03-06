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
from yass.core.core import yass_core
from yass.core.callback.util.buddystate import yass_buddystate
from yass.core.callback.util.sip_message import yass_message

class yass_buddy_cb(pj.BuddyCallback):
    """ Class wrapping PJSIP BuddyCallback. It implements the following callbacks:
            * on_state
    """

    def on_state(self):
        info = self.buddy.info()
        b = self.core.cfg.find_buddy(info.uri)
        if b:
            buddy_state = yass_buddystate(b.name, info.subscribed, info.online_status, info.online_text, info.sub_state, info.uri)
            self.core.cb.buddystate(buddy_state)

    def on_pager(self, mime_type, body):
        if self.buddy:
            info = self.buddy.info()
            msg = yass_message(info.uri, info.contact, mime_type, body)
            self.core.cb.incoming_message(msg)

    def __init__(self, buddy=None):
        pj.BuddyCallback.__init__(self, buddy)
        self.core = yass_core()

if __name__ == "__main__":
    pass

