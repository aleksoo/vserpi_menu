#!/usr/bin/python3

from os.path import exists

import commands
import os
import signal
import subprocess
import sys
import time

class TouchOscController:
    _processName = "touchosc2midi"
    _touchoscPath = "/home/pi/.local/bin/touchosc2midi"
    _subProcess = None
    _subProcessRunning = False
    _touchoscPathDetected = False

    
    def __init__(self):
        if self._checkTouchOsc():
            self._touchoscPathDetected = True
        else:
            print("No touchosc2midi found at", self._touchoscPath, ", can't start process")

    def __del__(self):
        if self._touchoscPathDetected is True:
            self._subProcess.terminate()    

    def isSubProcessRunning(self):
        return self._subProcessRunning

    def getIp(self):
        ip = "N\\A"
        print(commands.getoutput('hostname -I'))
        ip = commands.getoutput('hostname -I')
        return ip

    def startTouchOsc(self):
        if self._touchoscPathDetected is True:
            if self._subProcessRunning is not True:
                print("startTouchOsc: starting process")
                self._runSubProcess()
                self._subProcessRunning = True
                return True
            else:
                print("startTouchOsc: subprocess is already running")
        else:
            print("startTouchOsc: Can't find touchosc2midi path")

    def killTouchOsc(self):
        if self._touchoscPathDetected is True:
            if self._subProcessRunning is True:
                subProcessStatus = self.isSubProcessRunning()
                # print("killTouchOsc: subProcessStatus =", subProcessStatus)
                if subProcessStatus is True: # TODO: Jezeli proces jest w trakcie wykonywania (None - w trakcie)
                    self._subProcess.terminate()
                    self._subProcessRunning = False
                    # os.killpg(os.getpgid(self._subProcess.pid), signal.SIGTERM)  # Send the signal to all the process group
                    print("killTouchOsc: terminating")
                    return True
                print("killTouchOsc: Cant terminate, process is dead already")
                return False
            else:
                print("killTouchOsc: Subprocess is not running")
                return False
        else:
            print("killTouchOsc: Can't find touchosc2midi path")
            return False

    def restartTouchOsc(self):
        if self._touchoscPathDetected is True:
            self.killTouchOsc()
            self.startTouchOsc()
        else:
            print("restartTouchOsc: Can't find touchosc2midi path")

    def _runSubProcess(self):
        if self._isPathDetected:
            self._subProcess = subprocess.Popen(["/home/pi/.local/bin/touchosc2midi"], stdout=subprocess.DEVNULL)#, \
                                            # preexec_fn=os.setsid)   
        # self._subProcess = subprocess.Popen(["ls"])  

    def _isPathDetected(self):
        return self._touchoscPathDetected

    def _checkTouchOsc(self):
        self._touchoscPathDetected = exists(self._touchoscPath)
        return self._touchoscPathDetected
    
    def infoTouchOsc(self):
        pass


if __name__ == "__main__":
    touchOscController = TouchOscController()
    # os.system("ps")
    time.sleep(5)
    touchOscController.killTouchOsc()
    time.sleep(1)
    touchOscController.killTouchOsc()
    time.sleep(1)
    touchOscController.startTouchOsc()
    time.sleep(1)
    touchOscController.startTouchOsc()
    time.sleep(1)
    touchOscController.killTouchOsc()
    time.sleep(1)
    touchOscController.killTouchOsc()
    time.sleep(1)
    os.system("ps")
    time.sleep(1)
    touchOscController.startTouchOsc()
    time.sleep(1)
    touchOscController.killTouchOsc()
    time.sleep(1)
    touchOscController.startTouchOsc()
    os.system("ps")
    