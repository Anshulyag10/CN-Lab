from ftplib import FTP

def ftp_demo():
    host = "ftp.dlptest.com"
    user = "dlpuser"
    pwd = "rNrKYTX9g7z3RgJRmxWuGHbeu"

    ftp = FTP(host)
    ftp.login(user, pwd)

    print("Connected to", host)
    print("Directory listing:")
    ftp.retrlines("LIST")

    with open("upload.txt", "w") as f:
        f.write("Hello from FTP client")

    with open("upload.txt", "rb") as f:
        ftp.storbinary("STOR upload.txt", f)
    print("File uploaded: upload.txt")

    with open("download.txt", "wb") as f:
        ftp.retrbinary("RETR upload.txt", f.write)
    print("File downloaded: download.txt")

    ftp.quit()

if __name__ == "__main__":
    ftp_demo()
