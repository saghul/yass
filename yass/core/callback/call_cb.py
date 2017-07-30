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
from yass.core.callback.util.call_state import yass_call_state

class yass_call_cb(pj.CallCallback):
    """ Class wrapping PJSIP CallCallback. It implements the following callbacks:
            * on_state
            * on_media_state
            * on_dtmf_digit
    """

    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)
        self.core = yass_core()

    def on_state(self):
        if self.call.info().state == pj.CallState.DISCONNECTED:
            self.core.calls.current = None
            self.core.cb.hangup()
            if self.core.cfg.player > -1:
                self.core.lib.conf_disconnect(self.core.lib.player_get_slot(self.core.cfg.player), 0)
                self.core.lib.player_destroy(self.core.cfg.player)
                self.core.cfg.player = -1

        uri = self.call.info().remote_uri
        state = self.call.info().state_text
        code = self.call.info().last_code
        reason = self.call.info().last_reason
        call_state = yass_call_state(uri, state, code, reason)
        self.core.cb.callstate(call_state)
    
    def on_media_state(self):
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            slot = self.call.info().conf_slot
            self.core.lib.conf_connect(slot, 0)
            self.core.lib.conf_connect(0, slot)

    def on_dtmf_digit(self, digits):
        pass

if __name__ == "__main__":
    pass
