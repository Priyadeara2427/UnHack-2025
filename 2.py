with open(r'M1_ProcessedLogFile.txt', 'r') as processed_file:
        lines = processed_file.readlines()

info = 0
error = 0
warn = 0

for i in lines:
    item = i.split()[2]
    if item == 'INFO':
        info += 1
    elif item == 'WARN':
        warn += 1
    elif item == 'ERROR':
        error += 1

with open(r'Practice\Milestone1\M1_Output.txt', 'w') as output_file:
        output_file.write("INFO: " + str(info))
        output_file.write("\nWARN: " + str(warn))
        output_file.write("\nERROR: " + str(error))


        