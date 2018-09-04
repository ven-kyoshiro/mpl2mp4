from fig_recorder import FigRecorder
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    rc = FigRecorder()
    movie = []
    for i in range(120):
        fig = plt.figure()
        fig.add_subplot(111)

        # 折れ線グラフを出力
        left = np.array([1, 2, 3, 4, 5])
        height = np.array([100, 10*i, 200, 500, 400])
        plt.plot(left, height)
        rc.add(fig, plt)
    rc.save('rc_test.mp4', 12, 1, reset = False)
