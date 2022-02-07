#!/usr/bin/python3

import os
import time
from MidiInterface import MidiInterface
# from TouchOscController import TouchOscController
from ChoiceHandler import ChoiceHandler

class Menu(ChoiceHandler):
    _choiceHandler = None
    _midiInterface = None
    _touchOscController = None

    _menuRefreshTime = 1 # seconds

    def __init__(self):
        self._choiceHandler = ChoiceHandler()
        self._midiInterface = MidiInterface()

        self._softwareList = self._choiceHandler.getDisplayedMenuList() # might be obsolete line

        # self._touchOscController = TouchOscController()

    def run(self):
        lastTime = time.time()
        while True:
            #tutaj dodac obsluge midi
            #self.midiInterface.getMidiMsg()
            self.checkChoice()

            if time.time() - lastTime > self._menuRefreshTime:
                lastTime = time.time()
                menu.printMenu()
    #            print(time.time())
        pass

    def printMenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print("    CONNECTED DEVICE NAME: [ ", self._midiInterface.getDeviceName(), " ]", sep="")
        # print("    TOUCHOSC2MIDI: [ ", self._touchOscController.getIp() , " ]",sep="")
        print("    ")
        print('    __________________________________')
        print("   /                 KORG             .   0 - touchOsc2Midi [N\\A]")
        print("  /              nanoKONTROL2         .")
        print("  |  [ < ] [ > ]                      .   1 - WAAAVE_POOL")
        print("  |   N/A   N/A                       .")
        print("  |                                   .   2 - SPECTRAL_MESH")
        print("  |  [CYC]       [SET]  [ < ]  [ > ]  .")
        print("  |    0          N/A   NEXT   PREV   .   3 - ARTIFICIAL_LIFE")
        print("  |                                   .")
        print("  |  [ < ] [ > ] [ [] ] [ |> ] [ O ]  .   4 - CHROMATIC ABBERATION")
        print("  \\    1     2     3      4      5    .")
        print('   \__________________________________.   5 - TEMPORAL VORTEX')

    def checkChoice(self):
        option = self._midiInterface.getMidiMsg() 
        if option != None: 
            pickedOption = option[1] # [1] to get incoming CC number
            self.runOption(pickedOption)


    def runOption(self, pickedOption):
        #here should be logic changing pages of menu
        #getDisplayedMenuList() to update screen

        if self._choiceHandler.runOption(pickedOption):
            self._softwareList = self._choiceHandler.getDisplayedMenuList()


if __name__ == '__main__':
    menu = Menu()
    menu.run()
    
