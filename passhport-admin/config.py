# -*-coding:Utf-8 -*-

"""Configuration file"""

# Compatibility 2.7-3.4
from __future__ import absolute_import
from __future__ import unicode_literals

import os, sys, configparser

# Reading configuration from /etc if possible else form the script directory
conf = configparser.ConfigParser()
conffile="passhport-admin.ini"
if os.path.isfile("/etc/passhport/" + conffile):
    conf.read("/etc/passhport/" + conffile)
else:
    conf.read(sys.path[0] + "/" + conffile)


""" Server configuration """
HOST =  conf.get("Network", 'PASSHPORTD_HOSTNAME')
PORT =  conf.get("Network", "PASSHPORTD_PORT")

""" SSL Configuration """
SSL            = conf.getboolean("SSL", "SSL")
SSL_CERTIFICAT = conf.get("SSL", "SSL_CERTIFICAT")

url_passhport = "http" + SSL*"s" + "://" + HOST + ":" + PORT +"/"
certificate_path = conf.get("SSL", "SSL_CERTIFICAT")
