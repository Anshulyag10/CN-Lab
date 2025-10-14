import random as R

def a():
    n = int(input("Enter number of frames: "))
    p = float(input("Enter loss probability (0-1): "))
    i = 0
    while i < n:
        print(f"Sending Frame {i}")
        if R.random() < p:
            print(f"Frame {i} lost , retransmitting ...")
            continue
        print(f"ACK {i} received")
        i += 1

if __name__ == "__main__":
    a()
