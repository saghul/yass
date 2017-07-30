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



class yass_net(object):
    """ Class for holding network configuration.
    """

    def get_system_ips(self):
        pass

    def __init__(self):
        """
            Default values. Real values are taken from the DB and loaded by sysconfig module.
        """
        self.bindaddr = "0.0.0.0"
        self.bindport = "5060"

if __name__ == "__main__":
    pass

