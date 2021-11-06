#!/usr/bin/python3

from os.path import exists

import os
import signal
import subprocess
import sys
import time

class TouchOscController:
    _processName = "touchosc2midi"
    _touchoscPath = "/home/pi/.local/bin/touchosc2midi"
    _subProcess = None
    
    def __init__(self):
        if self._checkTouchOsc():
            self._runSubProcess()
        else:
            print("No touchosc2midi found at", self._touchoscPath, ", can't start process")

    def __del__(self):
        self._subProcess.terminate()

    def isSubProcessRunning(self):
        return self._subProcess.poll()

    def startTouchOsc(self):
        subProcessStatus = self.isSubProcessRunning()
        print("subProcessStatus:", subProcessStatus, end = '; ')
        if subProcessStatus is not None : # TODO: jezeli proces nie jest w trakcie wykonywania (None - trakcie)
            print("process is dead before starting")
            self._runSubProcess()
            return True
        else:
            print("process is alive cant start")
            return False

    def killTouchOsc(self):
        subProcessStatus = self.isSubProcessRunning()
        if subProcessStatus is None: # TODO: Jezeli proces jest w trakcie wykonywania (None - w trakcie)
            self._subProcess.terminate()
            # os.killpg(os.getpgid(self._subProcess.pid), signal.SIGTERM)  # Send the signal to all the process group
            print("TERMINATING......................................................")
            return True
        print("Cant terminate, dead already")
        return False

    def restartTouchOsc(self):
        self.killTouchOsc()
        self.startTouchOsc()

    def _runSubProcess(self):
        self._subProcess = subprocess.Popen(["/home/pi/.local/bin/touchosc2midi"])#, \
                                            # preexec_fn=os.setsid)   
        # self._subProcess = subprocess.Popen(["ls"])  

    def _checkTouchOsc(self):
        return exists(self._touchoscPath)
    
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
    touchOscController.killTouchOsc()
    time.sleep(1)
    touchOscController.startTouchOsc()
    time.sleep(1)
    touchOscController.killTouchOsc()
    time.sleep(2)
    os.system("ps")
    # touchOscController.startTouchOsc()
    