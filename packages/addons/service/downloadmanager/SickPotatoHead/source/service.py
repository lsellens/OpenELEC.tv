#
import os
import sys
import xbmc
import xbmcaddon
import time
import subprocess

__scriptname__ = "SickPotatoHead"
__author__     = "lsellens"
__url__        = "http://dl.dropbox.com/u/42265484/repository.SickPotatoHead/repo"
__settings__   = xbmcaddon.Addon(id='service.downloadmanager.SickPotatoHead')
__cwd__        = __settings__.getAddonInfo('path')
__start__      = xbmc.translatePath( os.path.join( __cwd__, 'bin', "SickPotatoHead.py") )
__stop__       = xbmc.translatePath( os.path.join( __cwd__, 'bin', "SickPotatoHead.stop") )

#xbmc.executebuiltin("XBMC.Notification('SickPotatoHead', 'Starting Services', '500', %s)" % ( __cwd__ + '/icon.png'))
subprocess.call(['python',__start__])

while (not xbmc.abortRequested):
    time.sleep(0.250)

#xbmc.executebuiltin("XBMC.Notification('SickPotatoHead', 'Shuting down Services', '5000', %s)" % ( __cwd__ + '/icon.png'))
subprocess.Popen(__stop__, shell=True, close_fds=True)
