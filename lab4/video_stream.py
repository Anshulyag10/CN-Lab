import cv2
import socket
import math
import time

host_ip = "127.0.0.1"
host_port = 9999
packet_size = 4096

socket_connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

video_stream = cv2.VideoCapture("sample.mp4")
frames_per_second = video_stream.get(cv2.CAP_PROP_FPS) or 25
time_interval = 1.0 / frames_per_second

print("Streaming video started...")

while video_stream.isOpened():
    success, frame = video_stream.read()
    if not success:
        break

    frame = cv2.resize(frame, (640, 480))

    encoded, buffer = cv2.imencode(".jpg", frame)
    frame_data = buffer.tobytes()

    total_packets = math.ceil(len(frame_data) / packet_size)
    for i in range(total_packets):
        start = i * packet_size
        end = start + packet_size
        packet = frame_data[start:end]

        marker = b'1' if i == total_packets - 1 else b'0'
        socket_connection.sendto(marker + packet, (host_ip, host_port))

    time.sleep(time_interval)

video_stream.release()
socket_connection.close()
print("Streaming video stopped.")

