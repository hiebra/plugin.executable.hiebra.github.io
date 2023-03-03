import xbmc
import xbmcaddon
if xbmcaddon.Addon().getSetting('autostart') == 'true':
    xbmc.executebuiltin('RunAddon(plugin.executable.init.github.io)')