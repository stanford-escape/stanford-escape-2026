"""
Simple wrapper for HTTP servers for nodes in the escape room.

Created by Niklas Vainio on 11/07/2025.
"""
import os
import wifi
import socketpool
import mdns
from adafruit_httpserver import Server, Route

class EscapeRoomServer:
    def __init__(self,
                 routes,
                 hostname='',
                 port=8080,
                 ):
        # Connect to WiFi if not connected yet
        if not wifi.radio.ipv4_address:
            for _ in range(5):
                wifi.radio.connect(os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD"))
                if wifi.radio.ipv4_address: break
            else:
                raise Exception(f"Failed to connect to Wi-Fi!")

        # Initialize MDNS if provided
        self._hostname = hostname
        self._port = port

        if self._hostname:
            self._mdns_server = mdns.Server(wifi.radio)
            self._mdns_server.hostname = self._hostname
            self._mdns_server.advertise_service(service_type="_http", protocol="_tcp", port=self._port)

        # Initilize MDNS server
        self._socket_pool = socketpool.SocketPool(wifi.radio)
        self._server = Server(self._socket_pool)

        # Add routes
        self._server.add_routes(routes)

        # Start the server!
        self._server.start(str(wifi.radio.ipv4_address), port=self._port)

        print("=" * 90)
        if self._hostname:
            print(f"   Server started at http://{self._hostname}.local:{self._port}/ (IP={wifi.radio.ipv4_address}, MAC={self._mac_address})")        
        else:
            print(f"   Server started at http://{wifi.radio.ipv4_address}:{self._port}/ (no mDNS, MAC={self._mac_address})")  
        print("=" * 90)


    def poll(self):
        # Must be called repeatedly to process HTTP events
        self._server.poll()

    @property
    def _mac_address(self):
        return ":".join(f"{b:02X}" for b in wifi.radio.mac_address)

