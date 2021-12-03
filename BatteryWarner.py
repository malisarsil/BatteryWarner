# The model which warns the user by voice and notification
# when the charge level gets below a certain value


import psutil
import time
import pyttsx3
from win10toast import ToastNotifier
import threading

toaster = ToastNotifier()
x=pyttsx3.init()
x.setProperty('rate',115)
x.setProperty('volume',1)
count = 0
def show_notification(show_text):
   toaster.show_toast(show_text,icon_path='C:\\Users\\sarsi\\Desktop\\image.png',duration=10)
   # loop the toaster over some period of time
while toaster.notification_active():
   time.sleep(0.1)
def monitor():
   while (True):
      time.sleep(10)
      battery = psutil.sensors_battery()
      plugged = battery.power_plugged
      percent = int(battery.percent)
      if percent <= 11:
         if plugged == False:
            processThread = threading.Thread(target=show_notification, args=("Your Battery at "+str(percent)+"% Please plug the cable",))  # <- note extra ','
            processThread.start()
            x.say("Your battery is getting low so charge it right now")
            x.runAndWait()
            count = 0
      elif percent == 100:
            if plugged == True:
               processThread = threading.Thread(target=show_notification, args=("Charging is completed",))  # <- note extra ','
               processThread.start()
               x.say("Charging is completed. Please unplug")
               x.runAndWait()
      elif percent == 90:
            if plugged == True:
               if count == 0:
                  processThread = threading.Thread(target=show_notification, args=("Your Battery at 90% Please plug out the cable",))  # <- note extra ','
                  processThread.start()
                  x.say("Your battery at 90% ")
                  x.runAndWait()
                  count = count + 1
while True:
   if __name__ == "__main__":
      monitor()
      time.sleep(2000)
