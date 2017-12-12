import os
import time
while(True):
	process_list = []
	c = os.popen("nvidia-smi")
	t = c.read()
	t = t.replace("\n","")
	t = t.replace("|","")
	t = t.replace("-","")
	t = t.replace("=","")
	t = t.replace("+","")
	t = t.replace("/","")
	t = t.split()
	i = t.index('Usage') + 2
	while(i<len(t)-1):
		process_list.append(t[i])
		i = 5 + i
	for process in process_list:
		if(process_list.count(process)>1):
			os.system("kill -9 "+process)
			#print("kill -9 "+process)
	time.sleep(300)
