#!/usr/bin/python3

import subprocess

class ChoiceHandler():
    # _vserpiPaths = "/home/pi/openFrameworks/apps/myApps"
    _vserpiPaths = "/home/pi/vserpi_menu/running_scripts"

    # _options = {
    #     '43': "WAAAVE_POOL_4",
    #     '44': "SPECTRAL_MESH_4",
    #     '42': "ARTIFICIAL_LIFE_4",
    #     '41': "CHROMATIC_ABERRATION_4",
    #     '45': "TEMPORAL_VORTEX_4",
    # }
    _options = {
        '43': "run_waaave_pool.sh",
        '44': "run_spectral_mesh.sh",
        '42': "run_artificial_life.sh",
        '41': "run_chromatic_aberration.sh",
        '45': "run_temporal_vortex.sh",        
    }

    def runOption(self, option):

        for key in self._options.keys():
            key = int(key)

            if option == key:
                # runPath = "make run " + self._vserpiPaths + '/' + self._options[str(option)]
                runPath = self._vserpiPaths + "/" + self._options[str(option)]                
                subprocess.call(runPath, shell=True)
                break
        pass

if __name__ == '__main__':
    choiceHandler = ChoiceHandler()
    choice = int(input())
    choiceHandler.runOption(choice)
