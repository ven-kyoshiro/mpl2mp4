# -*- coding:utf-8 -*-
import matplotlib as mpl
mpl.use('Agg')
import numpy as np
import skvideo.io
import skvideo.datasets


class FigRecorder(object):
    def __init__(self):
        self.stack = []
        
    def reset(self):
        self.stack = []
        
    def add(self, fig, plt, reset_fig=True):
        fig.canvas.draw()
        data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        self.stack.append(data)
        if reset_fig:
            plt.close()
        
    def save(self, f_name, f, s, reset = True):
        # frame per second (int)
        videodata = np.array(self.stack, dtype=np.uint8)
        skvideo.io.vwrite(f_name, videodata, outputdict={
                            '-r': str(f) + '/' + str(s)},
                            inputdict={'-r': str(f) + '/' + str(s)})
        if reset:
            self.reset()
