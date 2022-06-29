#!/usr/bin/python3

import subprocess

# for every software you want to add to menu 
# you have to create run script
softwareList = [
    ["WAAAVE_POOL", "run_waaave_pool.sh"],
    ["SPECTRAL MESH", "run_spectral_mesh.sh"],
    ["ARTIFICIAL LIFE", "run_artificial_life.sh"],
    ["CHROMATIC ABERRATION", "run_chromatic_aberration.sh"],
    ["TEMPORAL VORTEX", "run_temporal_vortex.sh"],
    ["CONVOLUTIONAL CHAOS", "run_convolutional_chaos.sh"],
    ["GENERIC GEOMETRY UTILITY", "run_generic_geometry_utility.sh"],
    ["SUPER HAECKEL ADVENTURES", "run_super_haeckel_adventures_64.sh"],
    ["HELLO WORD", "run_hello_word.sh"]
]

# softwareList = [
#     [1, 1],
#     [2, 2],
#     [3, 3],
#     [4, 4],
#     [5, 5],
#     [6, 6]
# ]

class ChoiceHandler():
    # _vserpiPaths = "/home/pi/openFrameworks/apps/myApps"
    _vserpiPaths = "/home/pi/vserpi_menu/running_scripts"
    _currentMenuPage = 0

    # _options = {
    #     '43': "WAAAVE_POOL_4",
    #     '44': "SPECTRAL_MESH_4",
    #     '42': "ARTIFICIAL_LIFE_4",
    #     '41': "CHROMATIC_ABERRATION_4",
    #     '45': "TEMPORAL_VORTEX_4",
    # }
    # _options = {
    #     '43': "run_waaave_pool.sh",
    #     '44': "run_spectral_mesh.sh",
    #     '42': "run_artificial_life.sh",
    #     '41': "run_chromatic_aberration.sh",
    #     '45': "run_temporal_vortex.sh",        
    # }

    def __init__(self):
        self._softwareList = []

        softWareListFiveItems = []

        softwareCounter = 0
        softwareCounterFiveItems = 0
        softWareListLenght = len(softwareList)

        for software in softwareList:
            softWareListFiveItems.append(software)
            softwareCounterFiveItems += 1
            softwareCounter += 1

            if softwareCounterFiveItems > 4 or softwareCounter is softWareListLenght:
#                print("Current five: ", softWareListFiveItems)
                self._softwareList.append(softWareListFiveItems[:])
#                print("Current five on endpoint: ", self._softwareList)
                softWareListFiveItems.clear()
                softwareCounterFiveItems = 0

        self._softwareListLenght = len(self._softwareList)

    def runOption(self, option):

        option = int(option)

        if option is 61 and self._currentMenuPage > 0:
            self._currentMenuPage -= 1
            return True

        if option is 62 and self._currentMenuPage < self._softwareListLenght - 1:
            self._currentMenuPage += 1
            return True

        if option >= 41 and option <= 45:
            # runPath = "make run " + self._vserpiPaths + '/' + self._options[str(option)]
            try:
                fixedOption = int([43, 44, 42, 41, 45].index(option))
                runPath = self._vserpiPaths + "/" + str(self._softwareList[self._currentMenuPage][fixedOption][1]) # last [1] is for path from# fix second path         
                subprocess.call(runPath, shell=True)
            except IndexError:
                pass
            # break
        return False
    
    # obsolete?
    def getDisplayedMenuList(self):
        return self._softwareList[self._currentMenuPage]
        pass

if __name__ == '__main__':
    choiceHandler = ChoiceHandler()
    print("done")
    while True:
        choice = int(input())
        choiceHandler.runOption(choice)
