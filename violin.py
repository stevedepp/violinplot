import matplotlib.pyplot as plt

import numpy as np

def figure_2_1():
    plt.violinplot(dataset=np.random.randn(200, 10) + np.random.randn(10))
    plt.xlabel('Action')
    plt.ylabel('Reward distribution')
    plt.savefig('./images/figure_2_1.png')
    plt.close()
