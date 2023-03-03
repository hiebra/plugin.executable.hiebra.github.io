from enum import Enum
import com.softalks.kodi.addon as addon
import com.softalks.kodi.plugin as plugin
import com.softalks.kodi.gui as gui

class Label(Enum):
    OPEN_SETTINGS = 99003
    RETRY = 99004
    
class Setting(addon.Setting):
    DATA_SOURCE = 'root'
    
class Parameter(plugin.Parameter):
    ACTION = 'action'
    
class Warning(gui.Warning):  # @ReservedAssignment
    MISSING_CONFIGURATION = {'heading': 99001, 'message': 99002}
    
OPEN_SETTINGS = Label.OPEN_SETTINGS.name