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



class YassException(Exception):
    """ Class for managing errors. sxceptions currently rised:
        ("CORE","001","Error creating transport.")
        ("CORE","002","Error starting the core.")
        ("CORE","003","Error stoping the core.")
        ("CORE","004","Error restarting the core.")
        ("CORE","005","Wrong STUN server. Please restart.")
        ("ACC","001","Error creating account.")
        ("ACC","002","Error loading account configuration.")
        ("CALL","001","Couldn't make the call.")
        ("CALL","002","Not an active call.")
        ("CALL","003","Error during call transfer.")
        ("CORE","005","Error initialising library.")
        ("CORE","006","Error initialising configuration.")
        ("DBCONFIG","001","Error initialising DB configuration.")
        ("DEV","001","There are no sound devices.")
        ("DEV","002","Error setting default sound device.")
        ("DEV","003","Error setting sound device.")
        ("DEV","004","Error getting actual sound device.")
        ("DEV","005","Error getting stored sound device.")
        ("DEV","006","Error storing sound device.")
        ("CFG","001","Error loading configuration.")
        ("GUI","001","Error loading account settings.")
        ("GUI","002","Error loading media settings.")
        ("GUI","003","Error loading log settings.")
        ("GUI","004","Error loading system settings.")
        ("GUI","005","Error saving account settings.")
        ("GUI","006","Error saving media settings.")
        ("GUI","007","Error saving log settings.")
        ("GUI","008","Error saving system settings.")
        ("GUI","009","Error loading codec settings.")
        ("GUI","010","Error saving codec settings.")
        ("GUI","011","Error loading presentity settings.")
        ("GUI","012","Error saving presentity settings.")
        ("HIS","001","Error loading call history data.")
        ("HIS","002","Error resetting call history data.")
        ("CODEC","001","Error loading codec information.")
        ("CODEC","002","Error setting codec priority.")
        ("SIMPLE","001","Error setting basic presence status.")
        ("SIMPLE","002","Error setting presence status.")
        ("SIMPLE","003","Error adding buddy.")
        ("SIMPLE","004","Error loading buddies from DB.")
        ("SIMPLE","005","Error deleting buddy.")
        ("SIMPLE","006","Error adding buddy, duplicated name or URI.")
        ("SIMPLE","007","Error storing buddy subscription status.")
        ("SIP","001","Invalid SIP URI.")
        ("STUN","001","Error disabling STUN server.")
        ("IM","001","Error sending MESSAGE request.")
    """

    def __init__(self, obj, code, msg):
        self.obj = obj
        self.code = code
        self.msg = msg

    def __str__(self):
        return "(%s-%s) %s" % (self.obj, self.code, self.msg)

