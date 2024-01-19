#we can inport datetime module to work with dates
import datetime as d
print(d.datetime.now()) #2024-01-19 20:39:35.703155

#strftime() takes the parameters and returns a string
# %a for shortversion of week day eg. Mon
# %A for full version of week day eg. Monday
# %B weekday eg. July
# %m month as a number 1 to 12
# %H hour  %M minutes %S seconds
# %x 	Local version of date 	12/31/18 	
# %X 	Local version of time 	17:41:00

x = d.datetime.now()
print(x.strftime("%A")) # note expression within " "
print(x.strftime("%H"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%x"))
print(x.strftime("%X"))
