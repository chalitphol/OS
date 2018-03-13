import matplotlib.pyplot as plt
import numpy as np
import random

def createProcess(process,time1,time2,time3,percent1,percent2,percent3,totalP):
    for i in range(int(percent1*totalP/100)):
        process.append(random.randint(time1[0],time1[1]))
    for i in range(int(percent2*totalP/100)):
        process.append(random.randint(time2[0],time2[1]))
    for i in range(int(percent3*totalP/100)):
        process.append(random.randint(time3[0],time3[1]))
    return process

def randomizeProcess (process):
    for i in range(len(process)-1,0,-1):
        j = random.randint(0,i)
        process[i],process[j] = process[j],process[i]
    return process

def firstComeFirstServe(process):
    waitingTime = []
    waitingTime.append(0)
    for i in range(len(process)-1):
        waitingTime.append(waitingTime[i]+process[i])
    x = np.arange(0,len(process),1)
    plt.plot(x, waitingTime)
    print("Average Waiting Time FCFS: ")
    print(averageWaitingTime(waitingTime))

def shortestJobFirst(process):
    pc = process.copy()
    pc.sort()
    waitingTime = []
    waitingTime.append(0)
    for i in range(len(process)-1):
        waitingTime.append(waitingTime[i]+pc[i])
    x = np.arange(0,len(process),1)
    plt.plot(x, waitingTime)

    print("Average Waiting Time SJF: ")
    print(averageWaitingTime(waitingTime))

def roundRobin(process,q):
    waitingTime = []
    waitingTime2 = []
    processNum = []
    pc = process.copy()
    for i in range(len(process)):
        processNum.append(i)
    processList = []
    waitingTime.append(0)
    processList.append(0)
    waitingTime2.append(0)
    i = 0
    while len(pc)!= 0:
        if pc[i] <= q:
            waitingTime.append(waitingTime[len(waitingTime)-1]+pc[i])
            waitingTime2.append(pc[i])
            processList.append(processNum[i])
            pc.pop(i)
            processNum.pop(i)
            i -= 1
        elif pc[i] > q:
            waitingTime.append(waitingTime[len(waitingTime)-1]+q)
            waitingTime2.append(q)
            pc[i] -= q
            processList.append(processNum[i])

        if(i+1 == len(pc)):
            i = 0
        else:
            i += 1
    x = np.arange(0,len(processList),1)
    plt.plot(x, waitingTime)

    print("Average Waiting Time RR: ")
    print(averageWaitingTimeRR(waitingTime2,processList,process))

def averageWaitingTime(waitingTime):
    return (sum(waitingTime)/len(waitingTime))

def averageWaitingTimeRR(waitingTime,processList,pc):
    count = 0
    for i in range(2,len(processList)):
        if processList[i-1] <= processList[i]:
            count += 1
        else:
            break
    wait = [0]*count
    exeTime = [0]*count
    for i in range(count):
        wait[i] = 0
        for j in range(len(processList)):
            if processList[i] == processList[j]:
                exeTime[i] += waitingTime[j] 
            elif processList[i] != processList[j]:
                if  exeTime[i] < pc[processList[i]]:
                    wait[i] += waitingTime[j]
                else:
                    break
    return (sum(wait)/len(wait))
        

def plotGraph():
    plt.xlabel('Process')
    plt.ylabel('Waiting time')
    plt.title('Process Run')
    plt.grid(True)
    plt.savefig("test.png")
    plt.legend(['FCFS', 'SJF' , 'RR'], loc='upper left')
    plt.show()

def main():
    process1 = []
    process2 = []
    process3 = []
    
    createProcess(process1,[10,20],[25,35],[45,80],10,20,70,60)
    randomizeProcess(process1)
    print("Process1: ")
    print(process1)
    firstComeFirstServe(process1)
    shortestJobFirst(process1)
    roundRobin(process1,60)
    plotGraph()

    # createProcess(process2,[2,8],[20,30],[35,40],50,30,20,40)
    # randomizeProcess(process2)
    # print("Process2: ")
    # print(process2)
    # firstComeFirstServe(process2)
    # shortestJobFirst(process2)
    # roundRobin(process2,8)
    # plotGraph()

    # createProcess(process3,[2,8],[20,30],[35,40],40,40,20,20)
    # randomizeProcess(process3)
    # print("Process3: ")
    # print(process3)
    # firstComeFirstServe(process3)
    # shortestJobFirst(process3)
    # roundRobin(process3,8)
    # plotGraph()

main()