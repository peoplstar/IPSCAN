import netaddr
import pingCheck as pc

#isUp(host) : pingCheck Function

iplist = "192.168.203.0/24"
path = "C:/Users/asxz3/OneDrive/바탕 화면/IPScan/"
#print(pc.isUp("192.168.203.128"))

iplist_file = open(path + "iplist.txt", "w", encoding="utf8")
for ip in netaddr.IPNetwork(iplist):
    if pc.isUp(str(ip)):
        iplist_file.write("Alive Host :" + str(ip) + "\n")

iplist_file.close()
