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

""" SIP helper methods.
"""

def make_uri(dst, domain):
    uri = ""
    if len(dst.split('@')) == 2:
        uri = dst
    else:
        uri = "sip:%s@%s" % (dst, domain)
    if uri[:4] == "sip:":
        return uri
    else:
        return "sip:%s" % (uri)

def get_user_from_uri(uri):
    try:
        u = pj.SIPUri(uri)
        return u.user
    except:
        return ""

def get_domain_from_uri(uri):
    try:
        u = pj.SIPUri(uri)
        if u.port:
            return "%s:%s" % (u.host, u.port)
        else:
            return u.host
    except:
        return ""

def check_uri(uri):
    from yass.core.core import yass_core
    res = yass_core().lib.verify_sip_url(uri)
    if res == 0:
        return True
    else:
        return False

