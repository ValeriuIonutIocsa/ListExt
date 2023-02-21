import os
import sys
import time

start_time = time.time()
sys.stdout.write('\nlist_ext starting\n')

if len(sys.argv) < 2:
    sys.stderr.write('insufficient arguments\n\n')
    exit(-1)

folderPath = sys.argv[1]
folderPath = os.path.abspath(folderPath)
sys.stdout.write('folder path: ' + folderPath + '\n')

ext_to_count_map = {}

for path, currentDirectory, files in os.walk(folderPath):
    for file in files:
        file_path = os.path.join(path, file)
        if not os.path.isdir(file_path):
            file_name, ext = os.path.splitext(file)
            ext_count = ext_to_count_map.get(ext, 0)
            ext_to_count_map[ext] = ext_count + 1

sorted_ext_list = []
for ext in ext_to_count_map.keys():
    sorted_ext_list.append(ext)
sorted_ext_list.sort()

sys.stdout.write('\n')
for ext in sorted_ext_list:
    sys.stdout.write(ext)
    sys.stdout.write(' -> ')
    count = ext_to_count_map[ext]
    sys.stdout.write(count.__str__())
    sys.stdout.write('\n')
sys.stdout.write('\n')

exec_time = str(round(time.time() - start_time, 2))
sys.stdout.write('\ndone; execution time: ' + exec_time + ' seconds\n')
