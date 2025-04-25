import socket

# Server configuration
HOST = '127.0.0.1'  # localhost
PORT = 65432        # non-privileged ports are > 1023

def start_server():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            print(f"[SERVER] Listening on {HOST}:{PORT}")
            
            conn, addr = s.accept()
            with conn:
                print(f"[SERVER] Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("[SERVER] Client disconnected.")
                        break
                    print(f"[SERVER] Received: {data.decode()}")
                    conn.sendall(b"Server received: " + data)
        except Exception as e:
            print(f"[SERVER ERROR] {e}")

if __name__ == "__main__":
    start_server()
