with open(r'Unhack2025_LogoscopeDatasets\Milestone1\M1_CommandFile.txt', 'r') as command_file:
        lines_cmd = command_file.readlines()

with open(r'Unhack2025_LogoscopeDatasets\Milestone1\M1_LogFile.txt', 'r') as log_file:
        lines_log = log_file.readlines()

for i in range(len(lines_cmd)):
        new_content_split = lines_cmd[i].split()
        new_command = new_content_split[2:]
        replace_line = int(new_content_split[1]) - 1
        new_command = ' '.join(new_command)
        timeline = lines_log[replace_line][:lines_log[replace_line].find(']')+1]
        lines_log[replace_line] = timeline + " " + new_command + "\n"


with open (r'Practice\Milestone1\M1_ProcessedLogFile.txt', 'w') as write_file:
        write_file.writelines(lines_log)
