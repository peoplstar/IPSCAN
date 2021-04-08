import netaddr
import pingCheck_v2 as pc
#isUp(host) : pingCheck_v2 Function

iplist = "192.168.203.0/24"
path = "C:/Users/asxz3/OneDrive/바탕 화면/IPScan/"

iplist_file = open(path+"iplist_v2.txt", "w", encoding="utf8")

for ip in netaddr.IPNetwork(iplist):
    ip = str(ip)
    if pc.isUp(ip):
        th = pc.threading.Thread(target = pc.isUp(ip), args = (ip,))
        th.start()
        pc.threads.append(th)
        iplist_file.write("Alive Host :" + ip + "\n")

for j in pc.threads:
    j.join()

iplist_file.close()