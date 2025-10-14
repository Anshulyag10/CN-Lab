import random as R
import matplotlib.pyplot as M

def c():
    n = int(input("Transmission rounds: "))
    p = float(input("Loss probability (0-1): "))
    w = 1
    t = 16
    x = []
    y = []
    i = 0
    while i < n:
        x.append(i)
        y.append(w)
        loss = False
        for _ in range(w):
            if R.random() < p:
                loss = True
                break
        if loss:
            t = max(1, w // 2)
            w = 1
        else:
            if w < t:
                w = w * 2
            else:
                w = w + 1
        i += 1
    M.plot(x, y)
    M.xlabel("Round")
    M.ylabel("cwnd")
    M.title("TCP congestion window")
    M.show()

if __name__ == "__main__":
    c()
