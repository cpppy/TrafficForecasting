# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt

#清洗并保存数据
def washDataSet(filename):
      fr = open(filename) 
      arrayolines = (fr.readlines())
      numoflines = len(arrayolines)
      print numoflines
      datalist = []
      busline = []
      fo = open('mydataX.txt',"w")

      for lineindex in range(numoflines-1):
            line = arrayolines[lineindex].strip()
            listfromline = line.split(',')
           
            line_name = int((listfromline[1])[3:5])
            terminal_id = listfromline[2]
            card_id = listfromline[3]
            deal_time = listfromline[5]
            try:
                  card_type = int(listfromline[6])
            except ValueError:
                  card_type = 6
                  
            '''
            if cardtypestr[0] == '\xc6':                      #普通卡
                  card_type = 1
            elif cardtypestr[0] == '\xd1':                   #学生卡
                  card_type = 2
            elif cardtypestr[0] == '\xc0':                   #老人卡
                  card_type = 3
            elif cardtypestr[0] == '\xb2':                   #残疾卡  
                  card_type = 4
            else:
                  card_type = 5                                  #员工卡

            #print card_type
            '''
                  
            datalist.append([lineindex,int(line_name),terminal_id,card_id,int(deal_time),card_type])
            #busline.append(listfromline[1])
            
            lineoutstr = str(lineindex) + '   ' + str(line_name) + '   ' + terminal_id  + '   ' + card_id + '   ' + str(deal_time) + '   ' + str(card_type) + '\n'
            if lineindex%100 == 0:
                  print lineindex,'lines have been finished!'
                  print lineoutstr

            fo.write(lineoutstr)
      fo.close()
      print "output finished"
      return datalist , busline

#创建星期字典
def weekDayDic():
      weekdaydic = {'801':5}
       #构建星期几查询字典
      datenum = 801
      weekdaynum = 5
      for begindata in range(802,1232):
            if((801<=begindata<=831) or (901<=begindata<=930) or (1001<=begindata<=1031) or (1101<=begindata<=1130) or (1201<=begindata<=1231)):
                  weekdaystr = str(begindata)
                  weekdaynum +=1
                  if weekdaynum ==8:
                        weekdaynum =1
                  weekdaydic[weekdaystr] = weekdaynum                       
      return weekdaydic
      
#创建天气和温度字典

#配置每天是星期几
def weekDay(dealtime):
      weekdaydic = {'0801':5}
      datenum = int(dealtime[4:8])
      datestr = str(datenum)

      #构建星期几查询字典
      datenum = 801
      weekdaynum = 5
      for begindata in range(802,1232):
            if((801<=begindata<=831) or (901<=begindata<=930) or (1001<=begindata<=1031) or (1101<=begindata<=1130) or (1201<=begindata<=1231)):
                  weekdaystr = str(begindata)
                  weekdaynum +=1
                  if weekdaynum ==8:
                        weekdaynum =1
                  weekdaydic[weekdaystr] = weekdaynum
            
      weekdayout = weekdaydic[datestr]
      return weekdayout
      
      
#读取数据,输出    线路名、时间、卡的类型 到 返回值readmat矩阵
def loadData(filename):
      fr = open(filename)
      arrayolines = fr.readlines()
      numberoflines = len(arrayolines)
      readmat=[]
      index = 0
      for line in arrayolines:
            line = line.strip()
            listfromline = line.split()
            linename = listfromline[1]
            dealtime = listfromline[4]
            cardtype = listfromline[5]
            readmat.append([linename,dealtime,cardtype])
            
      return readmat

# 从readmat中统计每天每时刻的刷卡总数，并添加  小时、星期、天气、温度 再生成元组
def everyHourSum(readmat,weathermat):
      pephourmat = []
      
      pepnum = 0
      weekdaydic = weekDayDic()
      index = 0
      weatherindex = 0
      searchdic = {}

      print '创建含有dealdate,hour,weekday,wether,temp,pepsum的原始表格'
      for dtnum in range(801,1232):
            if((801<=dtnum<=831)or(901<=dtnum<=930)):
                  weather1 = int(weathermat[weatherindex][1])
                  weather2 = int(weathermat[weatherindex][2])
                  temp = float(weathermat[weatherindex][3])
                  weatherindex +=1
                  for hour in range(5,24):
                        dealdate = '0'+str(dtnum)
                        weekday = weekdaydic[str(dtnum)]
                        pephourmat.append([dealdate,hour,weekday,weather1,weather2,temp,pepnum])
                        #print pephourmat[index]
                        
                        #构建日期查询字典  日期和小时:位置
                        if hour<10:
                              hourstr = '0'+str(hour)
                        else:
                              hourstr = str(hour)
                        timeindic = dealdate + hourstr
                        searchdic[timeindic] = index
                        #print timeindic,'   ',index
                        index +=1
                                               
            if((1001<=dtnum<=1031)or(1101<=dtnum<=1130)or(1201<=dtnum<=1231)):
                  weather1 = int(weathermat[weatherindex][1])
                  weather2 = int(weathermat[weatherindex][2])
                  temp = float(weathermat[weatherindex][3])
                  weatherindex +=1
                  for hour in range(5,24):
                        dealdate = str(dtnum)
                        weekday = weekdaydic[str(dtnum)]
                        pephourmat.append([dealdate,hour,weekday,weather1,weather2,temp,pepnum])
                        #print pephourmat[index]

                        #构建日期查询字典  日期和小时:位置
                        if hour<10:
                              hourstr = '0'+str(hour)
                        else:
                              hourstr = str(hour)
                        timeindic = dealdate + hourstr
                        searchdic[timeindic] = index
                        #print timeindic,'   ',index
                        index +=1
      print 'pephourmat的原始表格创建完成'
                        

      #已创建好数据，
      print '现在开始进入读取数据pepnum++阶段'
      keyerrorcount = 0
      numoflines = len(readmat)
      print 'readmat has ',numoflines,'   lines-record'
      for lineindex in range(numoflines):
            linearr = readmat[lineindex]
            #print linearr
            if int(linearr[0]) == 11:
                  dealtimestr = str(linearr[1])
                  #print dealtimestr
                  timeofsearch = dealtimestr[4:10]
                  #print timeofsearch
                  try:
                        locindic = searchdic[timeofsearch]
                        whicharr = pephourmat[locindic]
                        #print whicharr
                        pepnum = int(whicharr[-1])
                        pepnum +=1
                        whicharr[-1] = str(pepnum)
                        pepnum=0
                  except KeyError:
                        #print timeofsearch,'  Key error ! its not exist in SearchDic !!!','--------------------------------------------------------'
                        keyerrorcount +=1
                        pass
      return pephourmat

      print 'keyerrorcount = ',keyerrorcount
      print '开始将pephourmat存储到 pephourmat.txt 文件中'
      fo = open('pephourmatX.txt',"w")
      phmlen = len(pephourmat)
      for phmindex in range(phmlen):
            phmline = pephourmat[phmindex]      #dealdate,hour,weekday,weather,temp,pepnum
            phmlinestr = str(phmline[0]) + '   ' + str(phmline[1]) + '   ' + str(phmline[2]) + '   ' + str(phmline[3]) + '   ' + str(phmline[4]) + '   ' + str(phmline[5])+ '   ' + str(phmline[6]) + '\n'
            fo.write(phmlinestr)
      print '(output pephourmat to txt file) has been finished !!!'
      fo.close()
      return pephourmat


#读取天气温度信息文件
def weatherinfo():
      wfr = open('gd_weather_report.txt')
      arrayoflines = (wfr.readlines())
      numoflines = (len(arrayoflines) + 1)/2
      #print numoflines
      weathermat = []
      index = 0
      for lineindex in range(numoflines):
            #print arrayoflines[2*lineindex]
            listfromline = (arrayoflines[2*lineindex]).strip().split(',')
            
            # deal date
            datearr = listfromline[0].split('/')
            if int(datearr[1])<10:
                  monthstr = '0'+datearr[1]
            else:
                  monthstr = datearr[1]
            if int(datearr[2])<10:
                  daystr = '0'+datearr[2]
            else:
                  daystr = datearr[2]
            datestr = monthstr + daystr
            #print datestr

            # deal weather
            warr = listfromline[1].split('/')
            #print warr
            w1 = int(warr[0])
            w2 = int(warr[1])
            '''
            print warr[0]
            if warr[0] == '\xe6\x99\xb4':   
                  w1 = 0             #晴
            elif warr[0] =='\xe5\xa4\x9a\xe4\xba\x91' or '\xe9\x98\xb4':  
                  w1 = 1                              #多云 阴
            elif warr[0] =='\xe5\xb0\x8f\xe9\x9b\xa8':   
                  w1 = 2             #小雨
            elif warr[0] =='\xe5\xb0\x8f\xe5\x88\xb0\xe4\xb8\xad\xe9\x9b\xa8':
                  w1 = 3              #小到中雨
            elif warr[0] =='\xe4\xb8\xad\xe9\x9b\xa8':
                  w1 = 4            #中雨
            elif warr[0] =='\xe4\xb8\xad\xe5\x88\xb0\xe5\xa4\xa7\xe9\x9b\xa8':
                  w1 = 5                     #中到大雨 
            elif warr[0] =='\xe5\xa4\xa7\xe9\x9b\xa8':
                  w1 = 6               #大雨
            elif warr[0] =='\xe5\xa4\xa7\xe9\x9b\xa8':
                  w1 = 7               #大到暴雨
            elif warr[0] == '\xe9\x9b\xb7\xe9\x98\xb5\xe9\x9b\xa8':
                  w1 = 8                 #雷阵雨
            else:
                  print 'error --------------------------------------------------------------------'
            #print w1

            print warr[1]
            if warr[1] == '\xe6\x99\xb4':   
                  w2 = 0             #晴
            elif warr[1] =='\xe5\xa4\x9a\xe4\xba\x91' or '\xe9\x98\xb4':  
                  w2 = 1                              #多云 阴
            elif warr[1] =='\xe5\xb0\x8f\xe9\x9b\xa8':   
                  w2 = 2             #小雨
            elif warr[1] =='\xe5\xb0\x8f\xe5\x88\xb0\xe4\xb8\xad\xe9\x9b\xa8':
                  w2 = 3              #小到中雨
            elif warr[1] =='\xe4\xb8\xad\xe9\x9b\xa8':
                  w2 = 4            #中雨
            elif warr[1] =='\xe4\xb8\xad\xe5\x88\xb0\xe5\xa4\xa7\xe9\x9b\xa8':
                  w2 = 5                     #中到大雨 
            elif warr[1] =='\xe5\xa4\xa7\xe9\x9b\xa8':
                  w2 = 6               #大雨
            elif warr[1] =='\xe5\xa4\xa7\xe9\x9b\xa8':
                  w2 = 7               #大到暴雨
            elif warr[1] == '\xe9\x9b\xb7\xe9\x98\xb5\xe9\x9b\xa8':
                  w2 = 8                 #雷阵雨
            #print w2
            '''

             # deal temperature
            tarr = listfromline[2].split('/')
            #print tarr
            t1 = float(tarr[0])
            t2 = float(tarr[1])
            meantep = float((t1+t2)/2)
            weathermat.append([datestr,str(w1),str(w2),str(meantep)])
            #print weathermat[index]
            index +=1

      return weathermat
            
            
# 计算每天的乘客量并绘制图形
def pepDayMat(pephourmat):
      pepdaymat = []
      phmlen = len(pephourmat)
      pdmindex = 0
      lastdate = '0801'
      daypepnum = 0
      for phmindex in range(phmlen):
            phmlinearr = pephourmat[phmindex]
            date = phmlinearr[0]
            pepnum = int(phmlinearr[-1])
            if date == lastdate:
                  daypepnum += pepnum
            else:
                  #先存储   lastdate, weekday,w1,w2,temp,daypepnum
                  pepdaymat.append([lastdate,pephourmat[phmindex-1][2],pephourmat[phmindex-1][3],
                                    pephourmat[phmindex-1][4],pephourmat[phmindex-1][5], daypepnum])
                  #print pepdaymat[pdmindex]
                  pdmindex +=1
                  #再开始新的一天记录
                  daypepnum = pepnum
                  lastdate = date
      if date == '1231':
            pepdaymat.append([date,pephourmat[phmindex-1][2],pephourmat[phmindex-1][3],
                                    pephourmat[phmindex-1][4],pephourmat[phmindex-1][5], daypepnum])
            pdmindex +=1
      
      return pepdaymat
                  
#分星期几 处理数据成为数组
def loadHourData(pephourmat,weekday,hour):
      xarr = []
      yarr = []
      x0 = 1.0
      numoflines = len(pephourmat)
      for lineindex in range(1300,numoflines):
            linearr = pephourmat[lineindex]
            if int(linearr[2]) == weekday and int(linearr[1]) == hour:
                  xarr.append([x0,int(linearr[3])+2,int(linearr[4])+2,float(linearr[5])])
                  yarr.append(int(linearr[-1]))
      return xarr,yarr
      

            
                  
            
            
      
      

      



















