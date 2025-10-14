import matplotlib.pyplot as plt

def simulate_tcp(max_r=100, init_thresh=64, loss_r=None):
    if loss_r is None:
        loss_r = [40, 75]

    cwnd = 1
    thresh = init_thresh
    
    r_hist = []
    c_hist = []

    for r in range(1, max_r + 1):
        r_hist.append(r)
        c_hist.append(cwnd)
        
        if r in loss_r:
            thresh = max(cwnd // 2, 2)
            cwnd = 1
            continue

        if cwnd < thresh:
            cwnd *= 2
        else:
            cwnd += 1
            
    plt.figure(figsize=(12, 7))
    plt.plot(r_hist, c_hist, marker='o', linestyle='-', label='cwnd')
    
    for lr in loss_r:
        l_idx = lr - 1
        if l_idx < len(c_hist):
            plt.axvline(x=lr, color='r', linestyle='--', label=f'Packet Loss at Round {lr}' if lr == loss_r[0] else "")
            plt.scatter(lr, c_hist[l_idx], color='red', s=100, zorder=5)
            plt.annotate(
                f'Timeout!\ncwnd reset to 1',
                xy=(lr, c_hist[l_idx]),
                xytext=(lr + 2, c_hist[l_idx] / 2),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
                bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="black", lw=1, alpha=0.8)
            )

    plt.title('TCP Congestion Window (cwnd) Simulation', fontsize=16)
    plt.xlabel('Transmission Round', fontsize=12)
    plt.ylabel('Congestion Window Size (cwnd) in MSS', fontsize=12)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    
    plt.savefig('cwnd_plot.png')
    print("Plot saved as 'cwnd_plot.png'")
    plt.show()

if __name__ == "__main__":
    simulate_tcp(max_r=100, init_thresh=64, loss_r=[40, 75])
