


def totalSeconds(
        cpu1,cpu2,cpu3,cpu4,cpu5,cpu6,cpu7,cpu8,
        retry1,retry2,retry3,retry4,retry5,retry6,retry7,retry8
        ):

    length = (len(cpu1))
    bitrate_totals = []
    retry_percent = []

    for n in range(0,length):
        bitratethisSecond = cpu1[n] + \
                     cpu2[n] + \
                     cpu3[n] + \
                     cpu4[n] + \
                     cpu5[n] + \
                     cpu6[n] + \
                     cpu7[n] + \
                     cpu8[n]
        retrythissecond = retry1[n] + \
                          retry2[n] + \
                          retry3[n] + \
                          retry4[n] + \
                          retry5[n] + \
                          retry6[n] + \
                          retry7[n] + \
                          retry8[n]
        print ('Second {} Bits {} Retries{}'.format(n,bitratethisSecond,retrythissecond))
        retries_percent_this_second = retrythissecond
        bitrate_totals.append(bitratethisSecond)
        retry_percent.append(retries_percent_this_second)

    return(bitrate_totals,retry_percent)
