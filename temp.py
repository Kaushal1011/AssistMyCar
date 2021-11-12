from gpiozero import LEDBarGraph, CPUTemperature
from signal import pause
import requests

# Use minimums and maximums that are closer to "normal" usage so the
# bar graph is a bit more "lively"
URL = "https://api.thingspeak.com/update"
while True:
    cpu = CPUTemperature()
    print('Initial temperature: {}C'.format(cpu.temperature))
    PARAMS = {'api_key':'68OQ0IJY2UZ8LYE9','field1':cpu.temperature}
    r = requests.get(url = URL, params = PARAMS)
    data=r.json()
    print(data)
    
