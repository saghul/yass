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
from pysqlite2 import dbapi2 as sqlite
from error import YassException

class yass_account(object):
    """ A wrapper class around the PJSIP Account Class. Data is loaded from SQLite database.
    """

    def _load_acc(self):
    	try:
	    con = sqlite.connect(dbconfig.DB_CONFIG)
	    for row in con.execute("SELECT opt, val FROM acc"):
		if str(row[1]).isdigit():
		    self.acc.__dict__[str(row[0])] = int(row[1])
		else:
		    self.acc.__dict__[str(row[0])] = str(row[1])
	    for row in con.execute("SELECT opt, val FROM presentity"):
		self.__dict__[str(row[0])] = str(row[1])
            con.close()

            if hasattr(self.acc, "acc_user") and hasattr(self.acc, "acc_password") and hasattr(self.acc, "acc_domain"):
                if len(str(self.acc.acc_user)) > 0 and len(str(self.acc.acc_domain)) > 0:
                    self.acc.id = "sip:%s@%s" % (str(self.acc.acc_user), str(self.acc.acc_domain))
                    self.acc.reg_uri = "sip:%s" % str(self.acc.acc_domain)
                    self.acc.auth_cred = [ pj.AuthCred("*", str(self.acc.acc_user), str(self.acc.acc_password)) ]
                    if self.acc.acc_transport == "tcp":
                        proxy = "<sip:%s;lr;transport=tcp>" % str(self.acc.acc_domain)
                        self.acc.proxy.append(proxy)
                    self.ready = True

	except sqlite.Error:
            raise YassException("ACC", "002", "Error loading account configuration.")

    def __init__(self):
        self.acc = pj.AccountConfig()
        self.ready = False
        self._load_acc()

if __name__ == "__main__":
    pass

