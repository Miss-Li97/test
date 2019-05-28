import numpy as np

file_name='/home/lihanyu/pycodes/yolo_loss/nohup.out'
#
# i=0
# with open('yolo.log','w+') as yolo_log:
#     with open(file_name, 'r') as f:
#         for t in f.readlines():
#             # lists.clear()
#             i = i + 1
#             if i>=8253183:
#                 #if t.startswith('1:'):
#                 if "rate" in t:
#                         yolo_log.write(t)



i=0
t_count=0
losses=[]

def judge_nan(str):
    if str == "-nan":
        str=0.000000
    return str

with open('yolo_region_ave100.log','w+') as yolo_log:
    with open(file_name, 'r') as f:
        for t in f.readlines():
            # lists.clear()
            i = i + 1
            if i>=8253183:

                if 'Region' in t and "Avg IOU" in t :

                    # if "Loaded" not in t:
                    #print(t)
                    t_count=t_count+1

                    enum=t[t.find(":")+1:]
                    Avg_IOU=enum.split(', ')[0].strip()
                    classes =((enum.split(', ')[1]).split(':')[-1]).strip()
                    obj =((enum.split(', ')[2]).split(':')[-1]).strip()
                    no_obj =((enum.split(', ')[3]).split(':')[-1]).strip()
                    five_R =((enum.split(', ')[4]).split(':')[-1]).strip()
                    seven_R =((enum.split(', ')[5]).split(':')[-1]).strip()
                    count =((enum.split(', ')[-1]).split(':')[-1]).strip()

                    losses.append(judge_nan(Avg_IOU))
                    losses.append(judge_nan(classes))
                    losses.append(judge_nan(obj))
                    losses.append(judge_nan(no_obj))
                    losses.append(judge_nan(five_R))
                    losses.append(judge_nan(seven_R))
                    losses.append(judge_nan(count))

                    if t_count>=19100:
                        Losses = np.array(losses).reshape(-1, 7).astype(np.float64)
                        # Losses_all = (Losses[0:(len(Losses)-len(Losses)%50), 0]).reshape(-1, 50).mean(1)
                        # print(Losses_all)
                        Losses_all=np.mean(Losses, axis=0)
                        np.set_printoptions(suppress=True)
                        Losses_all=np.round(Losses_all,decimals=6)

                        #np.savetxt("result.txt", Losses_all)
                        #np.savetxt('submit.txt', Losses_all, fmt='%.03f')

                        #line=Losses_all[0]+' '+Losses_all[1]+' '+Losses_all[2]+' '+Losses_all[3]+' '+Losses_all[4]+' '+Losses_all[5]+' '+Losses_all[6]
                        yolo_log.write(str(Losses_all)+'\n')
                        print(Losses_all)
                        losses.clear()
                        t_count=0

                    #print(Avg_IOU)
                    # print(classes)
                    # print(obj)
                    # print(no_obj)
                    # print(five_R)
                    # print(seven_R)
                    # print(count)

                    # losses.append(Avg_IOU)
                    # losses.append(classes)
                    # losses.append(obj)
                    # losses.append(no_obj)
                    # losses.append(five_R)
                    # losses.append(seven_R)
                    # losses.append(count)







