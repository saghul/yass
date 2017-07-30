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
import dbconfig
from error import YassException
from pysqlite2 import dbapi2 as sqlite

class yass_dev(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_dev(self):
        return (self.id, self.name)


class yass_devices(object):

    def get_default_dev(self):
        if len(self.list) == 0:
            raise YassException("DEV", "001", "There are no sound devices.")
        else:
            return self.list[0]

    def set_default_dev(self):
        try:
            self.lib.set_snd_dev(0, 0)
        except pj.Error, e:
            raise YassException("DEV", "002", "Error setting default sound device.")

    def set_stored_dev(self):
        self.set_dev(self.captdev, self.playdev)

    def get_stored_dev(self):
        return (self.captdev, self.playdev)

    def set_dev(self, capt, play):
        try:
            self.lib.set_snd_dev(capt, play)
        except pj.Error:
            raise YassException("DEV", "003", "Error setting sound device.")

    def set_null_dev(self):
        try:
            self.lib.set_null_snd_dev()
        except pj.Error:
            pass

    def get_dev(self):
        try:
            return self.lib.get_snd_dev()
        except pj.Error:
            raise YassException("DEV", "004", "Error getting actual sound device.")

    def load_stored_dev(self):
        play = capt = -1
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            for row in con.execute("SELECT opt, val FROM dev"):
                if str(row[0]) == "playback":
                    play = int(row[1])
                if str(row[0] == "capture"):
                    capt = int(row[1])

            if play > -1 and capt > -1:
                self.playdev = play
                self.captdev = capt

	except sqlite.Error:
            raise YassException("DEV", "005", "Error getting stored sound device.")
    
    def store_dev(self, capt, play):
        try:
            con = sqlite.connect(dbconfig.DB_CONFIG)
            con.isolation_level = None
            con.execute("UPDATE dev SET val='%s' WHERE opt='playback'" % play)
            con.execute("UPDATE dev SET val='%s' WHERE opt='capture'" % capt)
            con.close()
            self.playdev = play
            self.captdev = capt
	except sqlite.Error:
            raise YassException("DEV", "006", "Error storing sound device.")

    def __init__(self, lib):
        self.lib = lib
        devs = self.lib.enum_snd_dev()
        self.list = []
        for dev in devs:
            d = yass_dev(len(self.list), dev.name)
            self.list.append(d)
        
        self.playdev = 0
        self.captdev = 0
        self.load_stored_dev()

if __name__ == "__main__":
    pass

