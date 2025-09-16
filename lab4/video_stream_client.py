import cv2
import socket
import numpy as np

server_ip = "0.0.0.0"
server_port = 9999
packet_size = 4096

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((server_ip, server_port))

print("Client listening... Press 'q' to quit.")

data_buffer = b""

while True:
    received_packet, _ = udp_socket.recvfrom(packet_size + 1)
    marker, chunk = received_packet[0:1], received_packet[1:]
    data_buffer += chunk

    if marker == b'1':
        frame = cv2.imdecode(np.frombuffer(data_buffer, np.uint8), cv2.IMREAD_COLOR)
        data_buffer = b""

        if frame is not None:
            cv2.imshow("Video Stream", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

udp_socket.close()
cv2.destroyAllWindows()
print("Client stopped.")


