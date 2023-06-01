from pydantic import BaseModel
import datetime


class SensorData(BaseModel):
    """Represents weather data collected by the weather station.

    Attributes:
        tempoerature (float): The temperature value in Celsius.
        humidity (float): The humidity value as a percentage.
        preassure (float): The preassure value in millibars.
        date: (datetime.datetime): The date when the sensor data
            was collected.
    """
    temperature: float
    humidity: float
    preassure: float
    date: datetime.datetime
