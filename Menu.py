#!/usr/bin/python3

import os
import time
from MidiInterface import MidiInterface


class Menu:
    _midiInterface = MidiInterface()

    vserpiPaths = "/home/pi/openFrameworks/apps/myApps"

    options = {
        '43': "WAAAVE_POOL_4",
        '44': "SPECTRAL_MESH_4",
        '42': "ARTIFICIAL_LIFE_4",
        '41': "CHROMATIC_ABERRATION_4",
        '45': "TEMPORAL_VORTEX_4",
        'default': ""
    }

    def printMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print("    CONNECTED DEVICE NAME:")
        print("        [", self._midiInterface.getDeviceName(), "]", sep="")
        print('    __________________________________')
        print("   /                 KORG             .")
        print("  /              nanoKONTROL2         .   1 - WAAAVE_POOL")
        print("  |  [ < ] [ > ]                      .   ")
        print("  |   N/A   N/A                       .   2 - SPECTRAL_MESH")
        print("  |                                   .")
        print("  |  [CYC]       [SET]  [ < ]  [ > ]  .   3 - ARTIFICIAL_LIFE")
        print("  |    0          N/A    N/A    N/A   .")
        print("  |                                   .   4 - CHROMATIC ABBERATION")
        print("  |  [ < ] [ > ] [ [] ] [ |> ] [ O ]  .")
        print("  \\    1     2     3      4      5    .   5 - TEMPORAL VORTEX")
        print('   \__________________________________.')

    def checkChoice(self):
        option = self._midiInterface.getMidiMsg() # [1] bo to wtedy midi CC jest nasze
        if option != None: 
            pickedOption = option[1]
            self.runOption(pickedOption)


    def runOption(self, pickedOption):
        # tu gdzies getMidiMsg
        print("Picked option:", pickedOption)


if __name__ == '__main__':
    menu = Menu()
    menuRefreshTime = 1 # seconds
    lastTime = time.time()
    while True:
        #tutaj dodac obsluge midi
        #menu.midiInterface.getMidiMsg()
        menu.checkChoice()
        if time.time() - lastTime > menuRefreshTime:
            lastTime = time.time()
            menu.printMenu()
#            print(time.time())
