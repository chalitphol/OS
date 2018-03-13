import random

def FIFO(frameSize,refString):
    frame = [0] * frameSize
    refPoint = 0
    pageFault = 0
    for i in range(len(refString)):
        if checkFrame(frame,refString[i]):
            pass
        else:
            frame[refPoint] = refString[i]
            refPoint += 1
            if(refPoint >= frameSize):
                refPoint = 0
            pageFault += 1
        # print("Count : ",i)
        # print(frame)
    print("FIFO")
    print("Frame Size = ",frameSize,"Page fault = ",pageFault)

def Optimal(frameSize,refString):
    frame = [0] * frameSize
    refPoint = 0
    pageFault = 0
    for i in range(len(refString)):
        if checkFrame(frame,refString[i]):
            pass
        else:
            frame[checkPeriod(frame,refString,i)] = refString[i]
            refPoint += 1
            if(refPoint >= frameSize):
                refPoint = 0
            pageFault += 1
        # print("Count : ",i)
        # print(frame)
    print("Optimal")
    print("Frame Size = ",frameSize,"Page fault = ",pageFault)

def LRU(frameSize,refString):            
    frame = [0] * frameSize
    refUse = [0] * frameSize
    refPoint = 0
    pageFault = 0
    for i in range(len(refString)):
        if checkFrame(frame,refString[i]):
            refUse[int(checkFrame(frame,refString[i])[1])] = 1
            increase(refUse,int(checkFrame(frame,refString[i])[1]))
        else:
            if(refUse[refPoint] == 0):
                frame[refPoint] = refString[i]
                refUse[refPoint] = 1
                increase(refUse,refPoint)
            else:
                frame[checkLeastUse(refUse)] = refString[i]
                tmp = checkLeastUse(refUse)
                refUse[checkLeastUse(refUse)] = 1
                increase(refUse,tmp)
            refPoint += 1
            if(refPoint >= frameSize):
                refPoint = 0
            pageFault += 1
        # print("Count : ",i)
        # print(frame)
    print("LRU")
    print("Frame Size = ",frameSize,"Page fault = ",pageFault)

def checkFrame(frame,ref):
    for i in range(len(frame)):
                if(frame[i] == ref):
                    return True,i
    return False

def checkPeriod(frame,ref,r):
    count = [0] * len(frame)
    for i in range(len(frame)):
        for j in range(r,len(ref)):
            if frame[i] != ref[j]:
                count[i] += 1
            else:
                break
    return count.index(max(count))

def checkLeastUse(refUse):
    LeastUse = 0
    LeastUseCount = 0
    for i in range(len(refUse)):
        if LeastUseCount < refUse[i]:
            LeastUseCount = refUse[i]
            LeastUse = i
    return LeastUse

def increase(refUse,r):
    for i in range(len(refUse)):
        if i == r:
            pass
        elif(refUse[i] != 0):
            refUse[i] += 1

def createRef(range1,range2,num):
    ref = [0] * num
    for i in range(num):
        ref[i] = random.randint(range1,range2)
    print(ref)
    return ref

def main():
    # ref = [7,5,1,2,5,3,5,4,2,3,5,3,2,1,2,5,1,7,5,1]
    ref = createRef(1,100,50)
    FIFO(3,ref)
    FIFO(5,ref)
    FIFO(8,ref)
    Optimal(3,ref)
    Optimal(5,ref)
    Optimal(8,ref)
    LRU(3,ref)
    LRU(5,ref)
    LRU(8,ref)

main()