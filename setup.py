#!/usr/bin/python2.5
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


yass_packages = [
        'yass',
        'yass.core',
        'yass.core.callback',
        'yass.core.callback.util',
        'yass.gui',
        'yass.gui.ui',
        'yass.modules',
        'yass.util.UnicodeQuickFix',
        'yass.util'
]

from distutils.core import setup
from yass.util.version import yass_version

setup(name = "YASS",
	version = yass_version,
        description = "YASS: Yet Another SIP Softphone",
	author = "saghul",
	author_email = "saghul@gmail.com",
	url = "http://www.saghul.net",
	license = "GPL",
        packages = yass_packages,
        data_files=[('bin',['yassphone']),
                    ('share/yass/sounds',['yass/sounds/ring.wav']),
                    ('share/yass',['desktop/yass48.png']),
                    ('share/applications',['desktop/yass.desktop'])]
)

