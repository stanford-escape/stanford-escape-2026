"""
Simple wrapper for HTTP clients for nodes in the escape room.

Created by Niklas Vainio on 11/07/2025.
"""
import os
import wifi
import socketpool
import adafruit_requests

class EscapeRoomClient:
    def __init__(self,
                 control_hostname='',
                 port=8080,
                 ):
        # Connect to WiFi if not connected yet
        if not wifi.radio.ipv4_address:
            for _ in range(5):
                wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
                if wifi.radio.ipv4_address: break
            else:
                raise Exception(f"Failed to connect to Wi-Fi!")

        # Store control hostname and port
        self._control_hostname = control_hostname
        self._port = port

        self._socket_pool = socketpool.SocketPool(wifi.radio)
        self._requests = adafruit_requests.Session(self._socket_pool)

        print('')
        print("=" * 90)
        print(f"   Client started with control at http://{self._control_hostname}:{self._port}/")        
        print("=" * 90)
        print('')

    def post(self, route, data=None):
        # Send a post request to the control node
        return self._requests.post(f"http://{self._control_hostname}:{self._port}{route}", data=data)

    def get(self, route):
        # Send a get request to the control node
        return self._requests.get(f"http://{self._control_hostname}:{self._port}{route}")


