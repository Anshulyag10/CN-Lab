import socket

def run_client():
    host = "127.0.0.1"
    port = 5050

    cname = "Client of Yagyesh Anshul"
    num = int(input("Enter an integer between 1 and 100: "))

    if not (1 <= num <= 100):
        print("Invalid input! Exiting.")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    msg = f"{cname},{num}"
    sock.send(msg.encode())

    data = sock.recv(1024).decode().strip()
    sname, snum = data.split(",")
    snum = int(snum)

    total = num + snum

    print(f"Client Name: {cname}")
    print(f"Server Name: {sname}")
    print(f"Client Number: {num}")
    print(f"Server Number: {snum}")
    print(f"Sum: {total}")

    sock.close()

if __name__ == "__main__":
    run_client()
