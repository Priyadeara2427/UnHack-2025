import re
with open(r'Practice\Milestone2\M2_ProcessedLogFile.txt', 'r') as log_file:
    lines_log = log_file.readlines()

login_pattern = r"User\s+'([^']+)'\s+logged in"

users = {}
for line in lines_log:
    if "logged in" in line:  # Check if it's a login event
        match = re.search(login_pattern, line)
        if match:
            user_id = match.group(1)
            if user_id in users:
                users[user_id] += 1
            else:
                users[user_id] = 1


with open(r'Practice\Milestone2\M2_Output.txt', 'w') as output_file:
    for user, count in users.items():
        output_file.write(f"{user}: {count}")
        output_file.write("\n")
