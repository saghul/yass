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



from pysqlite2 import dbapi2 as sqlite
from yass.core.error import YassException
import yass.core.dbconfig as dbconfig

""" Module for updating call history.
"""

call_type = ["INBOUND", "OUTBOUND"]

def update_history(num, type):
    try:
        con = sqlite.connect(dbconfig.DB_HISTORY)
        con.isolation_level = None
        con.execute("INSERT INTO history(num, type, date) VALUES('%s', '%s', current_timestamp)" % (num, call_type[type]))
        con.close()
    except sqlite.Error:
        raise YassException("HIS", "001", "Error loading call history.")

def delete_history():
    try:
        con = sqlite.connect(dbconfig.DB_HISTORY)
        con.isolation_level = None
        con.execute("DELETE FROM history")
        con.close()
    except sqlite.Error:
        raise YassException("HIS", "002", "Error resetting call history data.")
    
def get_history_data():
    try:
        con = sqlite.connect(dbconfig.DB_HISTORY)
        data = []
        for row in con.execute("SELECT num, type, date FROM history ORDER BY date DESC"):
            value = (str(row[0]), str(row[1]), str(row[2]))
            data.append(value)
        con.close()
        return data
    except sqlite.Error:
        raise YassException("HIS", "001", "Error loading call history.")

