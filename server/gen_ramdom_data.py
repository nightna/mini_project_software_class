from services import save_data
from datetime import datetime
import random

count = 3

for day in range(count):
    for t in range(24):
        time = datetime(2022, 2, day + 1, t)
        temp = random.randrange(25, 35)
        humi = random.randrange(40, 50)

        save_data(1, temp, humi, time)

    print(day+1)