#!/usr/bin/python2.5
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



from yass.core.core import yass_core
import pjsua as pj

def incoming_message_cb(msg):
    print str(msg)

def regstate_cb(state):
    print str(state)

def main():

    core = yass_core()
    core.cb.set_cb_incoming_message(incoming_message_cb)
    core.cb.set_cb_regstate(regstate_cb)
    core.start()
    
    while True:
        comm = raw_input(">>> ")
        c = comm.split()

        if len(c) > 0:
            if c[0] == "quit":
                break
            elif c[0] == "call":
                core.make_call(c[1])
                continue
            elif c[0] == "dtmf":
                core.send_dtmf(core.calls.current, c[1])
                continue
            elif c[0] == "hangup":
                core.hangup_call(core.calls.current)
                continue
            elif c[0] == "hold":
                core.hold_call(core.calls.current)
                continue
            elif c[0] == "unhold":
                core.unhold_call(core.calls.current)
                continue
            elif c[0] == "answer":
                core.answer_call(core.calls.current)
                continue
            elif c[0] == "reject":
                core.reject_call(core.calls.current)
                continue
            elif c[0] == "message" and len(c) > 2:
                msg = " ".join(c[2:])
                core.send_message(c[1], msg)

    print "Stopping core..."
    core.stop()


if __name__ == "__main__":
    main()

