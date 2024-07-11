import time

from kivy.properties import StringProperty, BooleanProperty, ListProperty, NumericProperty
from ArduinoClass import ArduinoClass



class Mediator:

    def __init__(self):
        self.arduino = ArduinoClass()
        self.arduinoList = []

    def getSensorName(self,specificKey):
        if specificKey in vars(self.arduino):
            print(f"Sensor: {specificKey}")
        else:
            print(f"{specificKey} does not exist in the instance")

        return specificKey

    def getAnalogueSensor(self,sensorName):
        sensorDetails =  getattr(self.arduino, sensorName, None)
        PIN = self.arduino.getPIN(sensorDetails)
        sensorVal = self.arduino.getAnaloguePinReading(PIN)
        sensorStr = f"{sensorVal}"
        return sensorStr


    def getDigitalSensor(self,sensorName):
        sensorDetails =  getattr(self.arduino, sensorName, None)
        PIN = self.arduino.getPIN(sensorDetails)
        sensorVal = self.arduino.getDigitalPinReading(PIN)
        print(f"Sensor: {sensorVal}")
        sensorStr = f"{sensorVal}"
        self.arduino.calcSpeed()
        return sensorStr

    #####################################################################################
    def getCalculatedReading(self,sensorName):
        speed = self.arduino.calcSpeed()
        distanceTravelled = self.arduino.getDistanceTravelled()
        current = self.arduino.getCurrent()
        voltage = self.arduino.getVoltage()
        batteryPercentage = self.arduino.getBatteryPercentage()

        switch = {
            "speed": speed,
            "distanceTravelled": distanceTravelled,
            "current": current,
            "voltage": voltage,
            "batteryPercentage": batteryPercentage
        }
        print(f"SWITCH CASE{switch[sensorName]}")

<<<<<<< Updated upstream
        return switch[sensorName]



    def getVoltage(self):
        return self.arduino.getVoltage()
=======
        print(f"Calculated Sensor: {switch[sensorName]}")
        return switch[sensorName]
>>>>>>> Stashed changes
