from services import save_data
from datetime import datetime
import random

for day in range(1):
    for t in range(24):
        time = datetime(2022, 3, day + 1, t)
        temp = random.randrange(25, 30)
        humi = random.randrange(60, 70)

        save_data(1, temp, humi, time)

    print(day+1)