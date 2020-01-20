#encoding:utf-8
import os
import tempfile
import time ,re
def run_once_mem(cmd):
    result=os.popen(cmd)
    stdout=result.read()
    return stdout,0,0
def run_once_cpu(cmd):
    result=os.popen(cmd)
    stdout=result.read()
    return stdout,0,0
i=0
filename='res2.text'
if os.path.exists(filename):
    os.remove(filename)
summem=countmem=0
sumcpu=countcpu=0
time1=time.time()
tempcpu=0
tempmem=0
while i<120:
    tempsum=0
    i=i+1
    cmdmem='adb shell dumpsys meminfo com.igen.solarmanbusiness'
    outmem,std_errmem,codemem=run_once_mem(cmdmem)
    cmdcpu='adb shell top  -n 1 -d 0.02 |findstr com.igen.solarmanbusiness'
    outcpu,std_err,codecpu=run_once_cpu(cmdcpu)
    print (i)
    if codemem==0:
        mem = re.compile('TOTAL[ ]+(\d+)[ ]+.*')
        resmem = mem.findall(outmem)
        print (resmem)
        if len(resmem):
            summem += int(resmem[0])
            countmem += 1
            if (tempmem < int(resmem[0])):
                tempmem = int(resmem[0])
        # if resmem=='null':
        #     break

    if codecpu == 0:
        cpu = re.compile('(\d+)\%.*')
        rescpu = cpu.findall(outcpu)
        #print rescpu
        if len(rescpu):
            for iter in range(len(rescpu)):
                tempsum = tempsum + float(rescpu[iter])
            print (tempsum)
            sumcpu += tempsum
            countcpu += 1
            if (tempcpu < tempsum):
                tempcpu = tempsum
    time.sleep(30)
time2 = time.time()
time = time2 - time1
print ('运行时间：' + str(time) + ' s')
print ('内存均值：'+str(summem/countmem/1024.0)+' MB')
print ('内存峰值：'+str(tempmem/1024.0)+' MB')
print ('cpu均值：'+str(sumcpu/countcpu)+' %')
print ('cpu峰值：'+str(tempcpu)+' %')


