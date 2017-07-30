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



class yass_buddy(object):
    """ Class for holding buddy data:
            - name
            - uri
            - subscription state
            - pj Buddy object instance
    """

    def status(self):
        if self.buddy is not None:
            return (self.buddy.info().online_status, self.buddy.info().online_text)
        else:
            return None

    def __init__(self, name, uri, buddy_obj):
        self.name = name
        self.uri = uri
        self.buddy = buddy_obj
        self.subscribed = False

if __name__ == "__main__":
    pass

