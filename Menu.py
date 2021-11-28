#!/usr/bin/python3

import os
import time
from MidiInterface import MidiInterface
from TouchOscController import TouchOscController
from ChoiceHandler import ChoiceHandler

class Menu(ChoiceHandler):
    _choiceHandler = None
    _midiInterface = None
    _touchOscController = None

    _menuRefreshTime = 1 # seconds

    def __init__(self):
        self._choiceHandler = ChoiceHandler()
        self._midiInterface = MidiInterface()
        self._touchOscController = TouchOscController()
        pass

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
        print("    TOUCHOSC2MIDI: [ ", self._touchOscController.getIp() , " ]",sep="")
        print("    ")
        print('    __________________________________')
        print("   /                 KORG             .   0 - touchOsc2Midi")
        print("  /              nanoKONTROL2         .")
        print("  |  [ < ] [ > ]                      .   1 - WAAAVE_POOL")
        print("  |   N/A   N/A                       .")
        print("  |                                   .   2 - SPECTRAL_MESH")
        print("  |  [CYC]       [SET]  [ < ]  [ > ]  .")
        print("  |    0          N/A    N/A    N/A   .   3 - ARTIFICIAL_LIFE")
        print("  |                                   .")
        print("  |  [ < ] [ > ] [ [] ] [ |> ] [ O ]  .   4 - CHROMATIC ABBERATION")
        print("  \\    1     2     3      4      5    .")
        print('   \__________________________________.   5 - TEMPORAL VORTEX')

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
    menu.run()
    
