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

class yass_call(object):
    """ yass_calls keeps track of concurrent calls in the system:
            * current: contains the current call object.
            * list: contains a list of calls currently active.
    """
    _current_call = None
    _calls = []

    def _get_current(self):
        return yass_call._current_call

    def _set_current(self, call):
        yass_call._current_call = call

    current = property(_get_current, _set_current)

    def _get_list(self):
        return yass_call._calls

    def _set_list(self, calls):
        yass_call._calls = calls

    list = property(_get_list, _set_list)

    def __init__(self):
        pass

if __name__ == "__main__":
    pass

