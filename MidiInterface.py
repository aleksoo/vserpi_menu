#!/usr/bin/python3

from pygame import midi as midi
import inspect

# Not the best solution with this class, 
# dataclass structures were introduced in Python 3.7
# but VSERPi images are mostly distributed with <3.7 version,
# so for sake of simplicity I decided to make "workaround"
class DeviceInfo:
    def __init__(self, name, input):
        self.name = name
        self.input = input

    name = None
    input = None


class MidiInterface:
    _connectedDeviceId = -1
    _deviceInfo = DeviceInfo('N\\A', -1)
    _midiController = None

    def __init__(self):
        midi.init()
        self.scanForDevices()
        self._midiController = midi.Input(self._connectedDeviceId)

    def getDeviceName(self):
        device = midi.get_device_info(self._connectedDeviceId)
        # print(str(device[1]).split("'")[1])
        device_info = DeviceInfo(str(device[1]).split("'")[1], device[2])
        return device_info.name

    def scanForDevices(self):
        devices_number = midi.get_count()
        # print("devices_number: ", devices_number)
        if devices_number > 0:
            for deviceIndex in range(0, devices_number):
                # get_device_info(an_id) -> (interf, name, input, output, opened)
                device = midi.get_device_info(deviceIndex)
                device_info = DeviceInfo(str(device[1]).split("'")[1], device[2])

                print("Found devices list: ")
                if device_info.input is 1: # "input" tells if "device" is input or output, 0 for 0utput, 1 for 1nput
                    print(" - ", device_info.name)


                if "nanoKONTROL2" in device_info.name and device_info.input == 1:
                    print("New device name: ", device_info.name, " , new device index: ", deviceIndex,sep="")  # todo logic some kind of
                    self._connectedDeviceId = deviceIndex
                    self._deviceInfo.name = device_info.name
                    self._deviceInfo.input = device_info.input
                    # return True
                elif device_info.input == 1 and self._connectedDeviceId == -1:
                    self._deviceInfo.name = device_info.name
                    self._deviceInfo.input = device_info.input
                    self._connectedDeviceId = deviceIndex
                    

        if self._connectedDeviceId != -1:
            return True
        else:
            return False

    def checkConnection(self):
        if self._connectedDeviceId == -1:
            return False

        device = midi.get_device_info(self._connectedDeviceId)
        device_info = DeviceInfo(str(device[1]).split("'")[1], device[2])
        if "nanoKONTROL2" in device_info.name and device_info.input == 1:
            return True
        if self.scanForDevices() is True:
            return True
        return False

    def getMidiMsg(self):
        #print("connectedDeviceId = ", self._connectedDeviceId)
        midiInput = self._midiController.read(1)
        if len(midiInput) > 0:
            # print(midiInput[0][0])
            return(midiInput[0][0])
        return None 
        #print(inspect.stack()[0][3])

    def menuMidiChoice(self, button):
        print("non available")

    def printDevices(self):
        devices_number = midi.get_count()
        if devices_number > 0:
            for deviceIndex in range(0, devices_number):
                # get_device_info(an_id) -> (interf, name, input, output, opened)
                device = midi.get_device_info(deviceIndex)
                device_info = DeviceInfo(str(device[1]).split("'")[1], device[2])
                #print(device_info.name, device_info.input)



if __name__ == '__main__':
    midiInterface = MidiInterface()
    midiInterface.printDevices()
    while True:
        midiInterface.getMidiMsg()
