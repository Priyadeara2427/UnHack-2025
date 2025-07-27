with open(r'Unhack2025_LogoscopeDatasets\Milestone3\M3_LogFile1.txt', 'r') as log_file1:
    lines1 = log_file1.readlines()

with open(r'Unhack2025_LogoscopeDatasets\Milestone3\M3_LogFile2.txt', 'r') as log_file2:
    lines2 = log_file2.readlines()

lines = []
i = j = 0
n1 = len(lines1)
n2 = len(lines2)

while i < n1 and j < n2:
    if lines1[i] == lines2[j]:
        i += 1
        j += 1
    else:
        date_time1 = lines1[i][lines1[i].find('['): lines1[i].find(']') +1]
        date_time2 = lines2[j][lines2[j].find('['): lines2[j].find(']') +1]
        if (date_time1 == date_time2):
            insert = "REPLACE " + str(i+ 1) +" "
            con = lines2[j][lines2[j].find(']') + 2:]
            lines.append(insert + con )
            i += 1
            j += 1
        else:
            if (i < n1 and j < n2):
                date_time1_2 = lines1[i+1][lines1[i+1].find('['): lines1[i+1].find(']') +1]
                if (date_time1_2 == date_time2):
                    insert = "DELETE " + str(i+1) +"\n"
                    lines.append(insert)
                    i += 1
                else:
                    insert = "INSERT " + lines2[j]
                    lines.append(insert)
                    j += 1

 
with open(r'Practice\Milestone3\M3_Output.txt', 'w') as output_file:
    output_file.writelines(lines)