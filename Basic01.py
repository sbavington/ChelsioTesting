#!/usr/bin/python

import iperf3
import json
client = iperf3.Client()
client.duration = 30
client.num_streams = 6
client.server_hostname = '10.0.20.111'
client.port = 5101
result = client.run()
data = json.loads(result.text)

print (result)
#print ('Sent Mbps = {}'.format(result.sent_Mbps))
#print ('Received Mbps = {}'.format(result.received_Mbps))

print ('Data = {}'.format(data['start']['connecting_to']['host']))
print ('Sum Sent {}'.format(data['end']['sum_sent']))
print ('Sum Recieved {}'.format(data['end']['sum_received']))
print ('cpu % {}'.format(data['end']['cpu_utilization_percent']))
stream = 1
for key in data['end']['streams']:
    sender_socketNum = key['sender']['socket']
    sender_seconds = key['sender']['seconds']
    sender_bits_per_second = key['sender']['bits_per_second']
    sender_bytes = key['sender']['bytes']
    sender_max_snd_cwnd = key['sender']['max_snd_cwnd']
    sender_min_rtt = key['sender']['min_rtt']
    sender_max_rtt = key['sender']['max_rtt']
    sender_mean_rtt = key['sender']['mean_rtt']
    sender_retransmits = key['sender']['retransmits']

    receiver_socketNum = key['receiver']['socket']
    receiver_seconds = key['receiver']['seconds']
    receiver_bits_per_second = key['receiver']['bits_per_second']
    receiver_bytes = key['receiver']['bytes']
    print ('Stream {} Send Socket {} Receive Socket {}'.format(stream, sender_socketNum, receiver_socketNum))
    print ('Sender:\n Seconds {} bits_per_second {} bytes {} max_snd_cwnd {} min_rtt {} max_rtt {} mean_rtt {} retransmits {}'.format(sender_seconds,
                                                                                                                                      sender_bits_per_second,
                                                                                                                                      sender_bytes,sender_max_snd_cwnd,
                                                                                                                                      sender_min_rtt,
                                                                                                                                      sender_max_rtt,
                                                                                                                                      sender_mean_rtt,
                                                                                                                                      sender_retransmits
                                                                                                                                      ))
    print ('Receiver:\n Seconds {} bits_per_second {} bytes {}'.format(receiver_seconds, receiver_bits_per_second, receiver_bytes))

    stream = stream + 1
