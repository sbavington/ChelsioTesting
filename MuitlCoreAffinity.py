#!/usr/bin/python3

import threading
import subprocess
import time
from matplotlib import pyplot as plt
from matplotlib import style
import sumData
import datetime

ports = [5201,5202,5203,5204,5205,5206,5207,5208]
threads = []
cpu = 0
seconds = 60
cpu1_bitrate = []
cpu2_bitrate = []
cpu3_bitrate = []
cpu4_bitrate = []
cpu5_bitrate = []
cpu6_bitrate = []
cpu7_bitrate = []
cpu8_bitrate = []
total_bitrate = []

cpu1_retries = []
cpu2_retries = []
cpu3_retries = []
cpu4_retries = []
cpu5_retries = []
cpu6_retries = []
cpu7_retries = []
cpu8_retries = []
total_retries= []

def testthread(port,cpu, lines):
    #command = ('iperf3 -c 10.0.20.111 -M 2600 -w 36k -T CPU:{1} -t 10 -p {0} -A {1} -C cubic\n'.format(port, cpu))
    command = ('iperf3 -c 10.0.20.112 -T CPU:{1} -f g -t {2} -b 4G -p {0} -C reno\n'.format(port, cpu,seconds))
    print(command)
    lines = subprocess.check_output(command, shell=True)
    lines = lines.decode()
    print(type(lines))
    print ('{} {}'.format(cpu,lines))
    for line in lines.splitlines():
        if 'ID' not in line and 'iperf' not in line and '- - - - - - - - - - - - - - - - - - - - - - - - -' not in line and 'port' not in line and 'sender' not in line:
            linedata = line.split()
            if len(linedata) > 10:
                #print (linedata)
                label = linedata[0]
                time = linedata[3]
                mbytes = linedata[5]
                rate = float(linedata[7])
                retries = float(linedata[9])
                if label == 'CPU:0:':
                    cpu1_bitrate.append(rate)
                    cpu1_retries.append(retries)
                if label == 'CPU:1:':
                    cpu2_bitrate.append(rate)
                    cpu2_retries.append(retries)
                if label == 'CPU:2:':
                    cpu3_bitrate.append(rate)
                    cpu3_retries.append(retries)
                if label == 'CPU:3:':
                    cpu4_bitrate.append(rate)
                    cpu4_retries.append(retries)
                if label == 'CPU:4:':
                    cpu5_bitrate.append(rate)
                    cpu5_retries.append(retries)
                if label == 'CPU:5:':
                    cpu6_bitrate.append(rate)
                    cpu6_retries.append(retries)
                if label == 'CPU:6:':
                    cpu7_bitrate.append(rate)
                    cpu7_retries.append(retries)
                if label == 'CPU:7:':
                    cpu8_bitrate.append(rate)
                    cpu8_retries.append(retries)

                cwindow = linedata[10]
                print ('label = {} time = {} mbytes {} rate {} retries {} cwin {}'.format(label,time,mbytes,rate,retries,cwindow))

lines = ''

for port in ports:
    #time.sleep(.1)
    t = threading.Thread(name='iperf', target=testthread, args=(port,cpu,lines))
    cpu = cpu + 1
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
    time.sleep(.5)
print ('CPU1 Bitrates = {} Retries {}'.format(cpu1_bitrate,cpu1_retries))
print ('CPU2 Bitrates = {} Retries {}'.format(cpu2_bitrate,cpu2_retries))
print ('CPU3 Bitrates = {} Retries {}'.format(cpu3_bitrate,cpu3_retries))
print ('CPU4 Bitrates = {} Retries {}'.format(cpu4_bitrate,cpu4_retries))
print ('CPU5 Bitrates = {} Retries {}'.format(cpu5_bitrate,cpu5_retries))
print ('CPU6 Bitrates = {} Retries {}'.format(cpu6_bitrate,cpu6_retries))
print ('CPU7 Bitrates = {} Retries {}'.format(cpu7_bitrate,cpu7_retries))
print ('CPU8 Bitrates = {} Retries {}'.format(cpu8_bitrate,cpu8_retries))
(total_bitrate,retries_percent) = sumData.totalSeconds(cpu1_bitrate,
                                     cpu2_bitrate,
                                     cpu3_bitrate,
                                     cpu4_bitrate,
                                     cpu5_bitrate,
                                     cpu6_bitrate,
                                     cpu7_bitrate,
                                     cpu8_bitrate,
                                     cpu1_retries,
                                     cpu2_retries,
                                     cpu3_retries,
                                     cpu4_retries,
                                     cpu5_retries,
                                     cpu6_retries,
                                     cpu7_retries,
                                     cpu8_retries)



style.use('ggplot')
x = range(1,(seconds +1))

fig, ax1 = plt.subplots(figsize=(15, 7))
color1 = 'tab:red'
color2 = 'tab:blue'
ax1.plot(x,cpu1_bitrate,linewidth=1)
ax1.plot(x,cpu2_bitrate,linewidth=1)
ax1.plot(x,cpu3_bitrate,linewidth=1)
ax1.plot(x,cpu4_bitrate,linewidth=1)
ax1.plot(x,cpu5_bitrate,linewidth=1)
ax1.plot(x,cpu6_bitrate,linewidth=1)
ax1.plot(x,cpu7_bitrate,linewidth=1)
ax1.plot(x,cpu8_bitrate,linewidth=1)
ax1.plot(x,total_bitrate,linewidth=1)
ax1.tick_params(axis='y', labelcolor=color1)

ax2 = ax1.twinx()
ax2.tick_params(axis='y', labelcolor=color2)
ax2.plot(x,retries_percent,linewidth=1,linestyle='--')

plt.title('iPerf Bitrate Per Thread LttleCeasar Chelsio No Optimization to Brutus Intel {}'.format(datetime.datetime.now()))
ax1.set_ylabel('G Bits/s')
ax2.set_ylabel('Retries Count')
ax1.set_xlabel('Seconds')
ax1.legend(['T1','T2','T3','T4','T5','T6','T7','T8','TotalBW'],loc=3)
ax2.legend(['Retries %'],loc=4)
fig.tight_layout()
plt.show()