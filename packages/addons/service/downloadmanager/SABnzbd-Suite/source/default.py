################################################################################
#      This file is part of OpenELEC - http://www.openelec.tv
#      Copyright (C) 2009-2012 Stephan Raue (stephan@openelec.tv)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with OpenELEC.tv; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################

import os
import sys
import xbmc
import xbmcaddon

__scriptname__ = "SABnzbd Suite"
__author__     = "OpenELEC"
__url__        = "http://www.openelec.tv"
__settings__   = xbmcaddon.Addon(id='service.downloadmanager.SABnzbd-Suite')
__cwd__        = __settings__.getAddonInfo('path')
__start__      = xbmc.translatePath( os.path.join( __cwd__, "service.py") )
__stop__       = xbmc.translatePath( os.path.join( __cwd__, 'bin', "SABnzbd-Suite.stop") )

#Stoping the service
subprocess.Popen(__stop__, shell=True, close_fds=True)
xbmc.executebuiltin("XBMC.Notification('SABnzbd-Suite', 'Shuting down Services', '5000', %s)" % ( __cwd__ + '/icon.png'))

#Open settings dialog
if __name__ == '__main__':
    __settings__.openSettings()

#Restarting the service
xbmc.executebuiltin("XBMC.Notification('SABnzbd-Suite', 'Starting Services', '500', %s)" % ( __cwd__ + '/icon.png'))
subprocess.call(['python',__start__])

#Sending a notification for debugging
xbmc.executebuiltin("XBMC.Notification('SABnzbd-Suite', 'Shuting down Services', '5000', %s)" % ( __cwd__ + '/icon.png'))
