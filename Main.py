from datetime import datetime
import keyboard
from scapy.sendrecv import sniff, AsyncSniffer
import time
i = 1
x=True
counter = 1
while(True):
    if counter != 0:
        capture = sniff(count = counter)
        print(f"{i} {str(datetime.now())}  {capture[0]}")
        time.sleep(0.1)
        i += 1
    if keyboard.is_pressed("shift") and counter != 0:
        print("<PAUSED>")
        print(f"<sniffed {i} Packets so far>")
        counter = 0

    if keyboard.is_pressed("ctrl") and counter != 1:
        print("<RESTARTING>")
        counter = 1


