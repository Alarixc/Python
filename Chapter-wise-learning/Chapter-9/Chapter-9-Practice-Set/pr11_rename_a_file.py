import os
old="sample.txt"
new="renamed_by_python.txt"
with open(old) as f:
    content=f.read()

with open(new,"w") as f:
    f.write(content)

os.remove(old)  #os.system('rm file') could probably try this too!(maybe)
