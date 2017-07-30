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



class yass_regstate(object):
    """ Helper class for representing the registration state.
    """

    def __init__(self, uri="", code="", reason=""):
        self.uri = uri
        self.code = code
        self.reason = reason

    def __str__(self):
        return "REGISTER \nURI: %s \nCode: %s -- Reason: %s \n" % (self.uri, self.code, self.reason)

if __name__ == "__main__":
    pass

