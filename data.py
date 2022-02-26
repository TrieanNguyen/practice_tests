import csv
import datetime
import pandas as pd
import numpy
import os
import time

def runCommandHdfs(command):
        os.system(command)

def data():
        header = ['Id','Name','Gender','Age']
        UTC_OFFSET = 7

        local_datetime    = str(datetime.datetime.today().strftime ("%Y-%m-%d %H:%M:%S") )
        local_datetime = datetime.datetime.strptime(local_datetime, "%Y-%m-%d %H:%M:%S")
        
        result_utc_datetime = local_datetime + datetime.timedelta(hours=UTC_OFFSET)
        
        daymonth =  result_utc_datetime.strftime("%d%m")
        day_month = daymonth

        house = result_utc_datetime.strftime("%H")

        result_utc_datetime =  result_utc_datetime.strftime("%Y%m%d%H%M")

        Id1 = str('10100' +  daymonth)
        Id2 = str('10200' +  daymonth)

        Name1 = 'Mary Jane '+house+ day_month
        Name2 = 'Peter Parker '+house+ day_month
                                        
        nameFile =  house + day_month
        arr1 = [Id1,Name1,'Female','30']
        arr2 =  [Id2,Name2,'Male','29']
        arr = [header,arr1,arr2]
        save_path = '/data/'

        fileName =str(result_utc_datetime) + ".csv"
        with open(save_path + fileName, 'w',encoding='UTF8' , newline='') as file:
            mywriter = csv.writer(file, delimiter=',')                      
            mywriter.writerows(arr)
        return save_path, fileName

def hdfs(fileName):
    runCommandHdfs('hdfs dfs -put /data/'+fileName+' '+'/data/result_data/')

def sleepTime():
    time.sleep(3600 - datetime.now().second - datetime.now().minute*60)

if __name__ == "__main__":
    
    while True:
        save_path,fileName =  data()
        hdfs(fileName)
        sleepTime()

