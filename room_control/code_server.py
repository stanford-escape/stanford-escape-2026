from adafruit_httpserver import Request, Response, Route, GET, PUT
from escape_room_server import EscapeRoomServer

# Define HTTP endpoint functions -------------------------------------------
def test(request: Request):
    print("Received request to /test/")
    return Response(request, "THIS IS TEST", content_type="text/plain")

# Initialize the server ----------------------------------------------------
server = EscapeRoomServer(
    routes=[
        Route("/test/", GET, test)
    ],
    hostname="your-hostname-here", 
    port=8080
)

# Main Loop ----------------------------------------------------------------
while True:
    try:
        # Perform any other actions here -----------------------------------
        # <put your code here>
        # ------------------------------------------------------------------
        server.poll()
    except Exception as e:
        print("Error:", e)