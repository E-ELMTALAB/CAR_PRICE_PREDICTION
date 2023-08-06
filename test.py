import re
import numpy as np
import pandas as pd


text = "112.7619 Nm @ 4000 rpm"

pattern = r"(\d+)"

match = re.search(pattern, text)
if match:
    number_before_bhp = int(match.group(1))
    print(number_before_bhp)
else:
    print("No match found.")