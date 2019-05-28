import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager

file_name='yolo_region_ave100.log'
zhfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

losses=[]
i=0
with open(file_name, 'r') as f:
    for t in f.readlines():
        t=t.split(']')[0].strip('[').strip('\n').split(' ')
        for i in range(t.count('')):
            t.remove('')
        for i in range(len(t)):
            losses.append(t[i])


    Losses = np.array(losses).reshape(-1, 7).astype(np.float64)
    Losses_avg = (Losses[0:(len(Losses) - len(Losses) % 2), 0]).reshape(-1, 2).mean(1)
    Losses_class = (Losses[0:(len(Losses) - len(Losses) % 2), 1]).reshape(-1, 2).mean(1)
    Losses_obj = (Losses[0:(len(Losses) - len(Losses) % 2), 2]).reshape(-1, 2).mean(1)
    Losses_nobj = (Losses[0:(len(Losses) - len(Losses) % 2), 3]).reshape(-1, 2).mean(1)
    Losses_5r = (Losses[0:(len(Losses) - len(Losses) % 2), 4]).reshape(-1, 2).mean(1)
    Losses_7r = (Losses[0:(len(Losses) - len(Losses) % 2), 5]).reshape(-1, 2).mean(1)

    plt.figure(figsize=(20, 30))

    plt.plot(np.arange(len(Losses_avg)) * 2, Losses_avg, label='avg', linewidth=1.0, c='red')
    plt.plot(np.arange(len(Losses_class)) * 2, Losses_class, label='class', linewidth=1.0, c='blue')
    plt.plot(np.arange(len(Losses_obj)) * 2, Losses_obj, label='obj', linewidth=1.0, c='green')
    plt.plot(np.arange(len(Losses_nobj)) * 2, Losses_nobj, label='nobj', linewidth=1.0, c='red')
    plt.plot(np.arange(len(Losses_5r))*2, Losses_5r,label='.5R', linewidth=1.0,c='pink')
    plt.plot(np.arange(len(Losses_7r))*2, Losses_7r, label='.7R',linewidth=1.0,c='purple')

    # plt.plot(np.arange(len(Losses[:, 4])), Losses[:, 4], linewidth=1.0, c='red')
    # plt.plot(np.arange(len(Losses[:, 5])), Losses[:, 5], linewidth=1.0, c='blue')

    plt.title('训练损失',fontproperties=zhfont,fontsize=20)
    plt.xlabel('训练次数',fontproperties=zhfont,fontsize=20)
    plt.ylabel('损失',fontproperties=zhfont,fontsize=20)

    plt.xlim(0, len(Losses_avg)*2) #range of x
    plt.ylim((0, 1))
    # # my_x_ticks = np.arange(0, 9000, 1000)
    # my_x_ticks = np.arange(0, len(Losses_ave)*2, int(len(Losses_ave)*2/5))
    # plt.xticks(my_x_ticks)
    ax=plt.gca()

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    plt.legend()
    plt.savefig('./loss.png')
    plt.show()
