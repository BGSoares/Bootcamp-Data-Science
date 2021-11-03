import requests

def pick_luftdaten_values(sensor_id):

    SENSOR_URL = "http://api.luftdaten.info/static/v1/sensor/{}/".format(sensor_id)

    result = requests.get(SENSOR_URL)
    data_json = result.json()

    time_stamp = data_json[0]['timestamp'] # first element is most recent measurement
    PM25, PM10 = data_json[0]['sensordatavalues'][0]['value'], data_json[0]['sensordatavalues'][1]['value']
    lon, lat = data_json[0]['location']['longitude'], data_json[0]['location']['latitude']
    
    
    return time_stamp, PM25, PM10, lon, lat 

print(pick_luftdaten_values(8104))