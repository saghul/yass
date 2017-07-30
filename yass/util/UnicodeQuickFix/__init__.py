# Tells the python interpreter to use Unicode.  
#
# People say this is a bad/ugly way to fix Plone's Unicode issues, but it
# appears to work.  Your mileage may vary.
#
#
# !!!!!!!!!!!!!!! USE AT YOUR OWN RISK !!!!!!!!!!!!!!!
#
#
# This is totally free, public domain software.  No author is given, because he
# has no intention whatsoever of supporting this hack.

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
