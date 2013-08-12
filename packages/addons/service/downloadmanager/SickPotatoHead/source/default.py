#
import os
import sys
import xbmcaddon

__scriptname__ = "SickPotatoHead"
__author__     = "lsellens"
__url__        = "http://dl.dropbox.com/u/42265484/repository.SickPotatoHead/repo"
__settings__   = xbmcaddon.Addon(id='service.downloadmanager.SickPotatoHead')

if __name__ == '__main__':
    __settings__.openSettings()
    #Restart Suite
    subprocess.check_call(['bash',__stop__])
    time.sleep(10)
    subprocess.call(['python',__start__])
