import socket

def run_srv():
    host = "0.0.0.0"
    port = 5050
    sname = "Server of Yagyesh Anshul"
    snum = 42

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    conn, addr = sock.accept()

    data = conn.recv(1024).decode().strip()
    cname, cnum = data.split(",")
    cnum = int(cnum)

    if not (1 <= cnum <= 100):
        conn.close()
        sock.close()
        return

    tot = cnum + snum
    print(f"Client: {cname}")
    print(f"Server: {sname}")
    print(f"Client Num: {cnum}")
    print(f"Server Num: {snum}")
    print(f"Sum: {tot}")

    reply = f"{sname},{snum}"
    conn.send(reply.encode())
    conn.close()
    sock.close()

if __name__ == "__main__":
    run_srv()
