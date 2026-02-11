import time
import shutil
from ascutil import mutate

shutil.copy("circuit.asc", "circuit_copy.asc")

rows = list(range(16))
columns = list(range(54))

t1 = time.time()
mutate("circuit_copy.asc", rows, columns, 0.5)
print(time.time() - t1)
