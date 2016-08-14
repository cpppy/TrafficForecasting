# -*- coding: utf-8 -*-
import gdrace
from numpy import *
import matplotlib.pyplot as plt
import regression
import myregression

#datalist,busline = gdrace.washDataSet('gdracedata2.txt')
#print datalist[12][1],busline

#output = gdrace.weekDay('20140805')
#print output
'''
dicdic,wordsum = gdrace.weekDayDic()
print wordsum

print dicdic['925']l
'''

readmat = gdrace.loadData('mydataX.txt')
print readmat
weathermat = gdrace.weatherinfo()

pephourmat = gdrace.everyHourSum(readmat,weathermat)
print pephourmat[:30]
print pephourmat[-1]
pepdaymat = gdrace.pepDayMat(pephourmat)



'''
 # plot 按照每天的人数画图
pdmindex = len(pepdaymat)
yarr = zeros(pdmindex)
for i in range(pdmindex):
    yarr[i] = int(pepdaymat[i][-1])
            
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(500),yarr)
plt.show()
'''
'''
# plot 从周一到周天 不断循环的曲线
pdmindex = len(pepdaymat)
fig = plt.figure()
ax = fig.add_subplot(111)
xarr = zeros(8)
yarr =  zeros(8)    
[60:for j in range(70,pdmindex):
    weekday = int(pepdaymat[j][1])
    xarr[weekday] = weekday
    yarr[weekday] = int(pepdaymat[j][-1])
    ax.plot(xarr[1:],yarr[1:])
plt.show()
'''
'''
# plot 每天各时间段的人数
phmlen = len(pephourmat)
fig = plt.figure()
ax = fig.add_subplot(111)
xarr = zeros(19)
yarr = zeros(19)
for phmindex in range(1122,1330):
    linelist = pephourmat[phmindex]
    hour = int(linelist[1])
    weekday = str(linelist[2])
    xarr[hour-5] = hour
    yarr[hour-5] = int(linelist[-1])
    if hour==23:
        ax.plot(xarr[:],yarr[:])
        #ax.annotate('++++', xy=(.5,.2), xycoords='data')
        ax.annotate(linelist[0], xy = (xarr[13], yarr[13]),xycoords='data')
plt.show()
'''




qarr =([1.0,2,2,15.5],[1.0,2,2,13.5],[1.0,2,2,14.5],[1.0,3,3,18.5],[1.0,3,3,20],[1.0,4,4,19],[1.0,3,3,13.5])

#rw = regression.stageWise(xarr,yarr,0.1,2000)

'''
b=20150101
cankao = 1161
weekday = 6
for hour in range(6,22):
    xarr,yarr = gdrace.loadHourData(pephourmat,weekday,hour)
    ypre = myregression.lwlr(qarr[weekday-1],xarr,yarr,1)
    if hour<10:
        hourstr = '0'+str(hour)
    else:
        hourstr = str(hour)
    cankaonum = int(pephourmat[cankao][-1])
    y=(int(ypre[0][0]) + cankaonum*16600/20721)*0.5
    print '线路15,'+str(b)+','+hourstr+','+str(int(y))
    cankao +=1

b=20150102
cankao = 1218
weekday = 7
for hour in range(6,22):
    xarr,yarr = gdrace.loadHourData(pephourmat,weekday,hour)
    ypre = myregression.lwlr(qarr[weekday-1],xarr,yarr,1)
    if hour<10:
        hourstr = '0'+str(hour)
    else:
        hourstr = str(hour)
    cankaonum = int(pephourmat[cankao][-1])
    y=(int(ypre[0][0]) + cankaonum*15884/19613)*0.5
    print '线路15,'+str(b)+','+hourstr+','+str(int(y))
    cankao +=1

b=20150103
cankao = 1275
weekday = 7
for hour in range(6,22):
    xarr,yarr = gdrace.loadHourData(pephourmat,weekday,hour)
    ypre = myregression.lwlr(qarr[weekday-1],xarr,yarr,1)
    if hour<10:
        hourstr = '0'+str(hour)
    else:
        hourstr = str(hour)
    cankaonum = int(pephourmat[cankao][-1])
    y=(int(ypre[0][0]) + cankaonum*17757/19613)*0.5
    print '线路15,'+str(b)+','+hourstr+','+str(int(y))
    cankao +=1
'''




b=20150101
for weekday in range(6,8):
    for hour in range(6,22):
        xarr,yarr = gdrace.loadHourData(pephourmat,weekday,hour)
        ypre = myregression.lwlr(qarr[weekday-1],xarr,yarr,1)
        if hour<10:
            hourstr = '0'+str(hour)
        else:
            hourstr = str(hour)
        y=int(ypre[0][0])
        print '线路15,'+str(b)+','+hourstr+','+str(y)
    b +=1

c=20150103
week = 7
for hour in range(6,22):
    xarr,yarr = gdrace.loadHourData(pephourmat,weekday,hour)
    ypre = myregression.lwlr(qarr[weekday-1],xarr,yarr,1)
    if hour<10:
        hourstr = '0'+str(hour)
    else:
        hourstr = str(hour)
    y=int(0.95*int(ypre[0][0]))
    print '线路15,'+'20150103,'+hourstr+','+str(y)


a=20150104
for weekday in range(1,5):
    for hour in range(6,22):
        xarr,yarr = gdrace.loadHourData(pephourmat,weekday,hour)
        ypre = myregression.lwlr(qarr[weekday-1],xarr,yarr,1)
        if hour<10:
            hourstr = '0'+str(hour)
        else:
            hourstr = str(hour)
        y=int(ypre[0][0])
        print '线路15,'+str(a)+','+hourstr+','+str(y)
    a +=1


'''
for i in range(len(ypre)):
    print (abs(ypre[i]-int(yarr[i])))/int(yarr[i])



'''
'''
fig = plt.figure()
ax = fig.add_subplot(111)


ypre = regression.lwlrTest(xarr,xarr,yarr,1)
#print ypre
xmat = mat(xarr)
srtInd = xmat[:,1].argsort(0)
xsort = xmat[srtInd][:,0,:]

ax.plot(xsort[:,1],ypre[srtInd])
ax.scatter(xmat[:,1].flatten().A[0],mat(yarr).T.flatten().A[0],s=2,c='red')

plt.show()

'''




















