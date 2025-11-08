from escape_room_client import EscapeRoomClient

# Initialize the server ----------------------------------------------------
client = EscapeRoomClient(
    control_hostname="control-hostname-here.local",
    port=8080
)

# Main Code ----------------------------------------------------------------
result = client.get("/")
print(result.status_code, result.text)