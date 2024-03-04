import time
# timer
def countdown(seconds):
  
  while seconds:
    hours = seconds // 3600
    minutes = (seconds % 3600 ) // 60
    secs = seconds % 60
    
    timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, secs)
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1
seconds = int(input("Enter the time in seconds: "))

countdown(seconds)
