import subprocess
import datetime

# 添加所有修改
subprocess.run(["git", "add", "."], check = True)

# 设置提交说明，格式为 Site updated: 2006-01-02 15:04:05
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = "Site updated: " + current_time
print(commit_message)

# 提交
subprocess.run(["git", "commit", "-m", commit_message], check = True)

# 推送到master分支上，并设置为追踪source分支
subprocess.run(["git", "push", "-u", "origin", "master:source"], check = True)