import threading
import subprocess
import time

ports = [5201,5202,5203,5204,5205,5206,5207,5208]
threads = []
cpu = 0
cpu1_bitrate = []
cpu2_bitrate = []
cpu3_bitrate = []
cpu4_bitrate = []
cpu5_bitrate = []
cpu6_bitrate = []
cpu7_bitrate = []
cpu8_bitrate = []


def testthread(port,cpu, lines):
    #command = ('iperf3 -c 10.0.20.111 -M 2600 -w 36k -T CPU:{1} -t 10 -p {0} -A {1} -C cubic\n'.format(port, cpu))
    command = ('iperf3 -c 10.0.20.111 -T CPU:{1} -f b -t 10 -p {0} -A {1} -C cubic \n'.format(port, cpu))
    print(command)
    lines = subprocess.check_output(command, shell=True)
    lines = lines.decode()
    print(type(lines))
    print ('{} {}'.format(cpu,lines))
    for line in lines.splitlines():
        print (line)

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