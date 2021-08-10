import os
import shutil
import time

path=input("Enter the folder to be deleted: ")
days=30
secs= days * 24 * 60 * 60

if os.path.exists(path):
   list=os.listdir(path)
   time=0
   for file in list:
       time=os.stat(path+'/'+file).st_ctime
       timesec=(time/1000)%60
       print(timesec)

       if(timesec>=secs):
           if(os.path.isdir(path+'/'+file)):
                os.rmdir(path+'/'+file)
           else:
               os.remove(path+'/'+file)
else:
    print("Path does'nt exist.")