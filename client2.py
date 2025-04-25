import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 65432

def start_client():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print(f"[CLIENT] Connected to server at {HOST}:{PORT}")
            while True:
                message = input("[CLIENT] Enter message (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    print("[CLIENT] Disconnecting.")
                    break
                s.sendall(message.encode())
                data = s.recv(1024)
                print(f"[CLIENT] Received from server: {data.decode()}")
        except ConnectionRefusedError:
            print("[CLIENT ERROR] Could not connect to server. Is it running?")
        except Exception as e:
            print(f"[CLIENT ERROR] {e}")

if __name__ == "__main__":
    start_client()
