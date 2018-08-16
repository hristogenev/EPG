# -*- coding: utf-8 -*-
import os
import sys
import datetime

reload(sys)
sys.setdefaultencoding('utf-8')

bindir         = os.path.dirname(os.path.realpath(__file__))
gitdir         = os.path.join(bindir, "..")
logfile        = os.path.join(gitdir, "logs", "log.txt")
wglogfile      = os.path.join(gitdir, "logs", "run.log.txt")
configdir      = os.path.join(gitdir, "config")
wgpath         = os.environ.get("wgpath")
wgmulti        = os.path.join(wgpath, "wgmulti.exe")
wgmulti        = "wgmulti.exe"
epg_file       = os.path.join(configdir, "epg.xml")
final_epg_file = os.path.join(gitdir, "epg.xml")
commitEnabled  = True

if os.path.isfile(logfile):
  os.remove(logfile)
sys.stdout = open(logfile, "w")

def log(msg):
  text = "%s | %s" % (datetime.datetime.now(), msg)
  #with open(logfile, "a") as w:
  #  w.write(text + "\n")
  print(text.encode("utf-8"))

log("EPG Generation started")
log("Chaning dir to bin dir")
os.chdir(bindir)
log("Current working dir: %s" % bindir)
log("Git dir: %s" % gitdir)
#log("Initializing log file")
  