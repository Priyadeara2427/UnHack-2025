with open(r'Practice\Milestone1\M1_ProcessedLogFile.txt', 'r') as log_file:
    lines_log = log_file.readlines()

with open(r'Unhack2025_LogoscopeDatasets\Milestone2\M2_CommandFile.txt', 'r') as cmd_file:
    lines_cmd = cmd_file.readlines()

def findLine(cmd, line):
    date_time = cmd.split()
    # [2025-06-27 10:00:27]
    date = str(date_time[0])
    date = date.removeprefix('[');
    time = str(date_time[1])
    time = time.removesuffix(']')
    # [2025-06-27 10:00:26] WARN  - Failed login attempt for user 'user006' from IP 192.168.17.181

    for i in range(len(line)):
        log_split = (line[i][:line[i].find(']') + 1]).split()
        date_log =( log_split[0]).removeprefix('[')
        time_log = (log_split[1]).removesuffix(']')
        if date_log == date:
            if time_log > time:
                return i
    
    return len(line)
 
for i in range(len(lines_cmd)):
    cmd = (lines_cmd[i]).split()
    if (str(cmd[0]) == 'DELETE'):
        del lines_log[int(cmd[1])-1]
    else:
        date_time = lines_cmd[i][lines_cmd[i].find('['): lines_cmd[i].find(']') +1]
        line = findLine(date_time, lines_log)
        string = cmd[1] + " " +cmd[2] +" "+ (' '.join(cmd[3:])) + "\n"
        lines_log.insert(line, string)

with open(r'Practice\Milestone2\M2_ProcessedLogFile.txt', 'w') as processed_file:
    processed_file.writelines(lines_log)