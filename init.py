import debug; debug.remote()

from   com.softalks.kodi.addon  import thumb
import com.softalks.kodi.gui    as user
from   com.softalks.kodi.plugin import View
import com.softalks.kodi.plugin as plugin
from   com.softalks.kodi.vfs    import listDirectory
from   constants                import Label, Warning, Setting, Parameter, OPEN_SETTINGS
#from   main                     import getBranch

request = plugin.Request()
if action := request.get(Parameter.ACTION):
    if action == OPEN_SETTINGS: 
        request.addon.openSettings()
    else:
        raise Exception(f'An unexpected action has been requested: {action}')
else:
    root = request.get(Setting.DATA_SOURCE)
    if not root:
        user.nofity(Warning.MISSING_CONFIGURATION)
    if request.synchronized():
        response = plugin.Listing(request)
        if root:
            '''
            trunk = getBranch(root)
            leafs, branches = listDirectory(root)
            for leaf in leafs:
                pass
            for branch in branches:
                pass
            response.send(mode = View.ICON_WALL)
            '''
            raise Exception('Not implemented yet')
        else:
            response.add(Label.OPEN_SETTINGS, art = thumb('settings.png', 128), action = True)
            response.add(Label.RETRY, art = thumb('refresh.png', 128))
            response.send(mode = View.ICON_WALL)
    else:
        request.synchronize()