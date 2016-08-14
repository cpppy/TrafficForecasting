from numpy import *
import regression

xarr,yarr = regression.loadDataSet('ex0.txt')
print xarr[:2]

ws = regression.standRegres(xarr,yarr)
print ws

xmat = mat(xarr)
ymat = mat(yarr)
yhat = xmat * ws

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.scatter(xmat[:,1].flatten().A[0] , ymat.T[:,0].flatten().A[0])

#xcopy = xmat.copy()
#xcopy.sort(0)
#ypre = xcopy * ws
#ax.plot(xcopy[:,1],ypre)

#plt.show()

print corrcoef(yhat.T,ymat)


print yarr[0]
#ypre = regression.lwlr(xarr[0],xarr,yarr,1.0)
#print ypre

print xarr[0]
print xmat[0,:]
print mat(xarr[0])

ypre = regression.lwlrTest(xarr,xarr,yarr,0.01)
#print ypre
srtInd = xmat[:,1].argsort(0)
xsort = xmat[srtInd][:,0,:]

ax.plot(xsort[:,1],ypre[srtInd])
ax.scatter(xmat[:,1].flatten().A[0],mat(yarr).T.flatten().A[0],s=2,c='red')

plt.show()


























