from ..sensor.data import SensorData


def insert_weather_data(cursor, data: SensorData):
    """Opens a sensor data insertion transaction into the database.

    Function excecutes a command on an input database cursor
    object. The function opens a transaction to the database
    that needs to be terminated by the connection by calling
    either the commit() or rollback() method.

    Args:
        cursor: Database cursor created by a database connection.
        data: Data from a sensor reading.
    """
    cursor.execute(
        """
        INSERT INTO
            public.weather(temperature, humidity, pressure, date)
        VALUES (%s, %s, %s, %s);
        """, (data.temperature, data.humidity, data.preassure, data.date)
    )
