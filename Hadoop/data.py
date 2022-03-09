import csv
from datetime import datetime
import pandas as pd
import numpy
import os
import time

def runCommandHdfs(command):
        os.system(command)

def data():
        header = ['Id','Name','Gender','Age']

        now =  datetime.now()
        local_datetime =    now.strftime("%Y-%m-%d %H:%M:%S")  
        result_utc_datetime =  now.strftime("%Y%m%d%H%M")
        day_month =  now.strftime("%d%m")
         
        house =  now.strftime("%H")

        Id1 = str('10101' +  day_month)
        Id2 = str('10201' +  day_month)

        Name1 = 'Mary Jane '+house+ day_month
        Name2 = 'Peter Parker '+house+ day_month
                                        
        nameFile =  house + day_month
        arr1 = [Id1,Name1,'Female','30']
        arr2 =  [Id2,Name2,'Male','29']
        arr = [header,arr1,arr2]
        save_path = '/home/anhtrieu/data/'

        fileName =str(result_utc_datetime) + ".csv"
        with open(save_path + fileName, 'w',encoding='UTF8' , newline='') as file:
            mywriter = csv.writer(file, delimiter=',')                      
            mywriter.writerows(arr)
        return save_path, fileName

def hdfs(fileName):
    runCommandHdfs('hdfs dfs -put /home/anhtrieu/data/'+fileName+' '+'/user/root/data/result_data/')

def sleepTime():
    now =  datetime.now()
    time.sleep(3600 - datetime.now().second - datetime.now().minute*60)

if __name__ == "__main__":
    
    while True:
        save_path,fileName =  data()
        hdfs(fileName)
        sleepTime()
