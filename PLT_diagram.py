import matplotlib.pyplot as plt
import os
import shutil
import numpy as np

from scipy.interpolate import spline
import re


def getCycleLosses(files):
    losses = []
    lists=[]

    flag = 0
    i=0
    with open(files, 'r') as f:
        for t in f.readlines():
            #lists.clear()
            i=i+1
            #if t.startswith('1:'):
            #if "rate" in t:
            if i%100==0:
                enum=t[t.find(":")+1:]
                whole=enum.split(', ')[0].strip()
                ave =((enum.split(', ')[1])[:-4]).strip()
                rate=((enum.split(', ')[2])[:-5]).strip()
                #print(step)
                #if step%100==0:
                losses.append(whole)
                losses.append(ave)
                losses.append(rate)
                    #losses.append(lists)
        print(losses)

    return losses

file_name='/home/lihanyu/pycodes/yolo_loss/yolo.log'
#getCycleLosses(file_name)

folderName = 'LossesImages'
if os.path.exists(folderName):
    shutil.rmtree(folderName)
plt.figure(figsize=(20, 20))
Losses =getCycleLosses(file_name)
Losses = np.array(Losses).reshape(-1, 3).astype(np.float64)
# Losses_all = (Losses[0:(len(Losses)-len(Losses)%30), 0]).reshape(-1, 30).mean(1)
# Losses_ave = (Losses[0:(len(Losses)-len(Losses)%80), 1]).reshape(-1, 80).mean(1)


# # x_new = np.linspace(0, len(Losses[:, 1]), 300)  # 300 represents number of points to make between T.min and T.max
#
# # y_smooth = spline(np.arange(len(Losses[:, 1])), Losses[:, 1], x_new)
# plt.plot(np.arange(len(Losses_all))*30, Losses_all, linewidth=1.0,c='red')
# plt.plot(np.arange(len(Losses_ave))*80, Losses_ave, linewidth=1.0,c='blue')

plt.plot(np.arange(len(Losses[:, 0])), Losses[:, 0], linewidth=1.0,c='red')
plt.plot(np.arange(len(Losses[:, 1])), Losses[:, 1], linewidth=1.0,c='blue')
# # plt.plot(x_new, y_smooth, linewidth=1.0)
#plt.plot(np.arange(len(Losses[:, 2])), Losses[:, 2], linewidth=1.0,c='green')
# plt.plot(np.arange(len(Losses[:, 3])), Losses[:, 3], linewidth=1.0)
#os.mkdir(folderName)
plt.ylabel('Loss', fontsize=25)
plt.xlabel('training steps', fontsize=25)
#plt.xlim((0, len(Losses[:, 0])))#range of x
plt.ylim((0, 1))
# plt.xticks(fontsize=25)
# plt.yticks(fontsize=25)
# # my_x_ticks = np.arange(0, 9000, 1000)
# my_x_ticks = np.arange(0, len(Losses[:, 0]), int(len(Losses[:, 0])/5))
my_y_ticks = np.arange(0, 1,.2)
#my_y_ticks = [0,1,2,4,8,16,32,64,128,256,512,1024,2048]

#plt.yticks(my_y_ticks)
plt.show()
# plt.xticks(my_x_ticks)
# # plt.savefig(os.path.join(folderName, "Losses_" + str(count) + "_" + str(i)) + ".png")
# plt.savefig(os.path.join(folderNa*me, "pix2pix_deblur_losses.png"))
