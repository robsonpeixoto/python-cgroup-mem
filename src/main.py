
import resource
import os

# reference: https://carlosbecker.com/posts/python-docker-limits/
if os.path.isfile('/sys/fs/cgroup/memory/memory.limit_in_bytes'):
    with open('/sys/fs/cgroup/memory/memory.limit_in_bytes') as limit:
        mem = int(limit.read())
        resource.setrlimit(resource.RLIMIT_AS, (mem, mem))


import pandas as pd

df = pd.read_csv("/data/simple.csv")

print(df)


