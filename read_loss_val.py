"""
input :
1st_trial_learning.txt
"""
import matplotlib.pyplot as plt


def drawGraph():
    plt.plot(x, y)

    plt.xlabel('Epoch')
    plt.ylabel('Loss Avg')
    #plt.legend(loc="upper left")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    fp = open("1st_trial_learning.txt", 'r')

    epoch_num = 0
    x = []
    y = []
    while True:
        try:
            line = fp.readline().split()
            if int(line[4].rstrip(',')) == epoch_num:
                num = int(line[4].rstrip(','))
                loss_val = float(line[9].rstrip(','))
                epoch_num += 1

                x.append(num)
                y.append(loss_val)
        except:
            if line[4][0] == 'm':
                continue
            break

    drawGraph()
    fp.close()
