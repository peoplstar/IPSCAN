Hacking by using python
====================
   
### This time, I will study hacking using Python. Before studying hacking, you will learn the basics of computer architecture.
###   It is very important to observe the change in the register value when hacking.
### This is for study purposes, and behaviors that cause disadvantages by actually using it on others can be legally punished, so please use a virtual machine to practice.
-------------------
> **<h3>IP SCAN</h3>**

���̽㿡�� ���������� �ϱ� ���� ip scan�� ���ٵ�, �̸� �̿��ϱ� ���� ����� `pip install netaddr pyping`�� ��ġ�ϰڽ��ϴ�.
��ĵ�� ����Ʈ ����Ʈ�� �����ϱ⿡ �ռ� �ڽ��� ȣ��Ʈ�� ��ε�ĳ��Ʈ�� �����ϰڽ��ϴ�.      
   
__python version3 �̻󿡼��� `pyping`�� ����Ϸ��� `locustion`��� �ͱ��� �߰� ��Ű���� ��ġ�ؾ��ϹǷ� `os`����� �̿��� pingCheck �Լ��� ���� ������ ���̴�.__   

---
 ���� ����ӽ��� ip�� �̿��Ͽ� ���� `iplist` = 192.168.203.0 ~ 192.168.203.255 ������ Ȯ���� ���̴�.   
�Ҵ�� IP�� __����ݸ���ũ ����__ �� �����ϸ�
`iplist = '192.168.203.0/24` �� �Ѵ�.
0�� ~ 255���� �ּҸ� Ȯ���ϱ� ���� `for`���� �̿��Ͽ� �˻��Ѵ�.   
�ش� �������� ȣ��Ʈ�� ����ִ����� Ȯ���ϱ� ���� ping ���� Ȯ���ϴ�.
```python
import netaddr
import pingCheck as pc

#isUp(host) : pingCheck Function

iplist = "192.168.203.0/24"
path = "C:/Users/asxz3/OneDrive/���� ȭ��/IPScan/"

iplist_file = open(path+"iplist.txt", "w", encoding="utf8")
for ip in netaddr.IPNetwork(iplist):
    if pc.isUp(str(ip)):
        iplist_file.write("Alive Host :" + str(ip) + "\n")
```
�ش� �ڵ�� �̿��ϰ� �Ǹ� �ӵ��� ����� ���� ���� �� �� �ִ�.   
���� ȿ������ ���̱� ���� Thread�� �̿� �� ���̴�.

> **<h3>IP SCAN_v2</h3>**   

���� ���� ���̳�, ������ ������ �� �� ���� ������ ���� �Ϻ����� �ʴ�.