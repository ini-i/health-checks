import psutil

#this checks the CPU usage in a user inputted interval

def cpu_usage(time):
  cpu_percent = psutil.cpu_percent(time)
  print("The CPU usage for {} seconds is {}%".format(time, cpu_percent))
