import netaddr
import os
import threading

iplist = "172.30.1.22/24"
threadLock = threading.Lock()
threads = []

path = "C:/Users/asxz3/OneDrive/바탕 화면/IPScan/"

iplist_file = open(path + "iplist_v2.txt", "w", encoding="utf8")


print("Start Scan")
def IPScan(ip):
    try:
        response = os.system("ping -n 1 " + ip)
        if not response:
            iplist_file.write("Alive Host :" + str(ip) + "\n")
            print("Network Active")
            threadLock.acquire()
            print("Alive Host  :" + str(ip))
            threaLock.release()
    except:
        pass

for ip in netaddr.IPNetwork(iplist):
    ip = str(ip)
    th = threading.Thread(target = IPScan, args = (ip,))
    th.start()
    threads.append(th)

for t in threads:
    t.join()

iplist_file.close()
print("End Scan")