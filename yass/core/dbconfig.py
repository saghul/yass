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
from error import YassException
from yass.util.version import yass_version
import os
import sys
import ConfigParser as cfgparser

"""
Module for containing and initialising configuration databases.
"""


yass_conf_dir = os.path.join(os.environ['HOME'], '.yass')
DB_CONFIG = os.path.join(yass_conf_dir, 'config.sqlite')
DB_HISTORY = os.path.join(yass_conf_dir, 'call_history.sqlite')
DB_BUDDIES = os.path.join(yass_conf_dir, 'buddies.sqlite')
YASS_LOG = os.path.join(yass_conf_dir, 'yass.log')
YASS_CFG = os.path.join(yass_conf_dir, 'yass.cfg')

def create_default_config_db(db):
    try:
        con = sqlite.connect(db)
        con.executescript("""
            CREATE TABLE ua(opt varchar(80), val varchar(80));
            INSERT INTO "ua" VALUES('max_calls','2');
            INSERT INTO "ua" VALUES('user_agent','YASS - %s');
            INSERT INTO "ua" VALUES('stun_host','');
    
            CREATE TABLE media(opt varchar(80), val varchar(80));
            INSERT INTO "media" VALUES('no_vad','1');
            INSERT INTO "media" VALUES('enable_ice','0');
            INSERT INTO "media" VALUES('audio_frame_ptime','20');
            INSERT INTO "media" VALUES('quality','10');
            INSERT INTO "media" VALUES('dtmfmode','info');
            INSERT INTO "media" VALUES('snd_auto_close_time','5');

            CREATE TABLE log(opt varchar(80), val varchar(80));
            INSERT INTO "log" VALUES('filename','%s');
            INSERT INTO "log" VALUES('level','9');
            INSERT INTO "log" VALUES('console_level','9');
            INSERT INTO "log" VALUES('msg_logging','1');
    
            CREATE TABLE acc(opt varcgar(80), val varchar(80));
            INSERT INTO "acc" VALUES('reg_timeout','600');
            INSERT INTO "acc" VALUES('allow_contact_rewrite','0');
            INSERT INTO "acc" VALUES('require100rel','0');
            INSERT INTO "acc" VALUES('publish_enabled','1');
            INSERT INTO "acc" VALUES('use_srtp','0');
            INSERT INTO "acc" VALUES('secure_signalling','0');
            INSERT INTO "acc" VALUES('acc_password','');
            INSERT INTO "acc" VALUES('acc_domain','');
            INSERT INTO "acc" VALUES('acc_user','');
            INSERT INTO "acc" VALUES('acc_transport','udp');
            INSERT INTO "acc" VALUES('voicemail_exten','*98');
    
            CREATE TABLE presentity(opt varcgar(80), val varchar(80));
            INSERT INTO "presentity" VALUES('p_online','1');
            INSERT INTO "presentity" VALUES('p_text','');
            
            CREATE TABLE net(opt varcgar(80), val varchar(80));
            INSERT INTO "net" VALUES('bindaddr','0.0.0.0');
            INSERT INTO "net" VALUES('bindport','5080');
    
            CREATE TABLE codecs(codec varchar(80), priority integer);
            INSERT INTO "codecs" VALUES('PCMA/8000/1',200);
            INSERT INTO "codecs" VALUES('PCMU/8000/1',-1);
            INSERT INTO "codecs" VALUES('GSM/8000/1',190);
            INSERT INTO "codecs" VALUES('iLBC/8000/1',-1);
            INSERT INTO "codecs" VALUES('speex/16000/1',-1);
            INSERT INTO "codecs" VALUES('speex/8000/1',-1);
            INSERT INTO "codecs" VALUES('speex/32000/1',-1);
            INSERT INTO "codecs" VALUES('G722/16000/1',-1);
    
            CREATE TABLE dev(opt varcgar(80), val varchar(80));
            INSERT INTO "dev" VALUES('capture','-1');
            INSERT INTO "dev" VALUES('playback','-1');
        """ % (yass_version, YASS_LOG))
        con.close()
    except sqlite.Error:
        pass

def create_default_callhistory_db(db):
    try:
        con = sqlite.connect(db)
        con.executescript("""
            CREATE TABLE history(num varchar(50), type varchar(10), date timestamp);
        """)
        con.close()
    except sqlite.Error:
        pass

def create_default_buddies_db(db):
    try:
        con = sqlite.connect(db)
        con.executescript("""
            CREATE TABLE buddies(name varchar(80), uri varchar(80), subscribed int(1));
        """)
        con.close()
    except sqlite.Error:
        pass

def reinit_databases():
    if os.path.isfile(DB_CONFIG):
        os.remove(DB_CONFIG)
    if os.path.isfile(DB_HISTORY):
        os.remove(DB_HISTORY)
    if os.path.isfile(DB_BUDDIES):
        os.remove(DB_BUDDIES)
    create_default_config_db(DB_CONFIG)
    create_default_callhistory_db(DB_HISTORY)
    create_default_buddies_db(DB_BUDDIES)
 
def init_databases():
    try:
        if not os.path.isdir(yass_conf_dir):
            os.mkdir(yass_conf_dir)
        if not os.path.isfile(YASS_CFG):
            cfg = cfgparser.ConfigParser()
            cfg.read(YASS_CFG)
            cfg.add_section("yass")
            cfg.set("yass", "firstrun", "no")
            cfg.set("yass", "version", yass_version)
            fp = open(YASS_CFG, "w")
            cfg.write(fp)
            fp.close()
        else:
            cfg = cfgparser.ConfigParser()
            cfg.read(YASS_CFG)
            firstrun = cfg.get("yass", "firstrun")
            version = cfg.get("yass", "version")
            if firstrun == "yes":
                reinit_databases()           
                cfg.set("yass", "firstrun", "no")
                cfg.set("yass", "version", yass_version)
                fp = open(YASS_CFG, "w")
                cfg.write(fp)
                fp.close()
            elif version != yass_version:
                reinit_databases()           
                cfg.set("yass", "version", yass_version)
                fp = open(YASS_CFG, "w")
                cfg.write(fp)
                fp.close()

        if not os.path.isfile(DB_CONFIG):
            create_default_config_db(DB_CONFIG)
        if not os.path.isfile(DB_HISTORY):
            create_default_callhistory_db(DB_HISTORY)
        if not os.path.isfile(DB_BUDDIES):
            create_default_buddies_db(DB_BUDDIES)
    except:
        raise YassException("DBCONFIG", "001", "Error initialising DB configuration.")


if __name__ == "__main__":
    pass


