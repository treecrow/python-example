import os
import time

content = '我爱你，爱着你，就像老鼠爱大米…………'
while True:
    os.system('clear')
    print(content)
    time.sleep(0.2)
    content = content[1:]+content[0]
