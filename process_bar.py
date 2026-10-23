import time 
import tqdm

def s_work(item):
    time.sleep(0.1)

for item in tqdm(range(100), desc="Processing items"):
    s_work(item)
