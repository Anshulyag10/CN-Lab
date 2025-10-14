import random as R

def b():
    f = int(input("Total frames: "))
    n = int(input("Window size: "))
    p = float(input("Loss probability (0-1): "))
    b = 0
    while b < f:
        e = min(b + n - 1, f - 1)
        print("Sending frames", ' '.join(str(x) for x in range(b, e + 1)))
        lost = False
        for j in range(b, e + 1):
            if R.random() < p:
                print(f"Frame {j} lost , retransmitting frames {j} {min(f - 1, j + n - 1)}")
                b = j
                lost = True
                break
            print(f"ACK {j} received")
        if not lost:
            b = e + 1

if __name__ == "__main__":
    b()
