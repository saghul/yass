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
from yass.core.error import YassException
from PyQt4 import QtCore, QtGui

class DtmfDlgController(object):
    """ Controller class for sending DTMF tones from the DTMF Tone window.
    """

    def send_dtmf(self, digit):
        try:
            self.core.send_dtmf(self.core.calls.current, digit)
        except YassException:
            "We don't really care if DTMF tones aren't sent, as we can't do anything to solve it."
            pass
    
    def __init__(self):
        self.core = yass_core()

if __name__ == "__main__":
    pass

