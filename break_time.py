import webbrowser
import time

total_breaks = 3
break_count = 0
print("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)    # can set it to 2 hrs like 2*60*60
    webbrowser.open("https://www.youtube.com/watch?v=inEu2qQuGZ8")
    break_count = break_count + 1
