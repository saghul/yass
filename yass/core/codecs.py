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

"""
Module for loading codecs and setting priorities.
"""

def load_codecs():
    from yass.core.core import yass_core
    try:
        con = sqlite.connect(dbconfig.DB_CONFIG)
        for row in con.execute("SELECT codec, priority FROM codecs"):
            yass_core().lib.set_codec_priority(str(row[0]), int(row[1]))
        con.close()
    except sqlite.Error:
        raise YassException("CODEC", "001", "Error loading codec information.")
    except pj.Error:
        raise YassException("CODEC", "002", "Error setting codec priority.")

if __name__ == "__main__":
    pass

