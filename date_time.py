from datetime import datetime
import time

total_print =5
print_count=0

while (print_count < total_print):
    time.sleep(1)
    print(datetime.now())
    print_count = print_count + 1
