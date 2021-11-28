#!/usr/bin/python3

import os

class ChoiceHandler():
    _vserpiPaths = "/home/pi/openFrameworks/apps/myApps"

    _options = {
        '43': "WAAAVE_POOL_4",
        '44': "SPECTRAL_MESH_4",
        '42': "ARTIFICIAL_LIFE_4",
        '41': "CHROMATIC_ABERRATION_4",
        '45': "TEMPORAL_VORTEX_4",
    }

    def runOption(self, option):

        for key in self._options.keys():
            key = int(key)

            if option == key:
                runPath = "make run " + self._vserpiPaths + '/' + self._options[str(option)]
                print(runPath)
                os.system(runPath) # nie dziala uruchamianie
                break
        pass

if __name__ == '__main__':
    choiceHandler = ChoiceHandler()
    choiceHandler.runOption(43)
    choiceHandler.runOption(10)
