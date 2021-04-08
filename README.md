Hacking by using python
====================
   
### This time, I will study hacking using Python. Before studying hacking, you will learn the basics of computer architecture.
###   It is very important to observe the change in the register value when hacking.
### This is for study purposes, and behaviors that cause disadvantages by actually using it on others can be legally punished, so please use a virtual machine to practice.
-------------------
> **<h3>IP SCAN</h3>**

파이썬에서 정보수집을 하기 위해 ip scan을 할텐데, 이를 이용하기 위한 모듈을 `pip install netaddr pyping`로 설치하겠습니다.
스캔할 사이트 리스트를 구성하기에 앞서 자신의 호스트를 브로드캐스트로 구성하겠습니다.      
   
__python version3 이상에서는 `pyping`을 사용하려면 `locustion`라는 것까지 추가 패키지를 설치해야하므로 `os`모듈을 이용해 pingCheck 함수를 따로 구현할 것이다.__   

---
 현재 가상머신의 ip를 이용하여 변수 `iplist` = 192.168.203.0 ~ 192.168.203.255 구간을 확인할 것이다.   
할당된 IP는 __서브넷마스크 내용__ 을 인지하며
`iplist = '192.168.203.0/24` 로 한다.
0번 ~ 255번의 주소를 확인하기 위해 `for`문을 이용하여 검색한다.   
해당 구간내에 호스트가 살아있는지를 확인하기 위해 ping 으로 확인하다.
```python
import netaddr
import pingCheck as pc

#isUp(host) : pingCheck Function

iplist = "192.168.203.0/24"
path = "C:/Users/asxz3/OneDrive/바탕 화면/IPScan/"

iplist_file = open(path+"iplist.txt", "w", encoding="utf8")
for ip in netaddr.IPNetwork(iplist):
    if pc.isUp(str(ip)):
        iplist_file.write("Alive Host :" + str(ip) + "\n")
```
해당 코드로 이용하게 되면 속도가 상당히 느린 것을 알 수 있다.   
더욱 효율성을 높이기 위해 Thread를 이용 할 것이다.

> **<h3>IP SCAN_v2</h3>**   

현재 구현 중이나, 쓰레드 내에서 알 수 없는 오류로 인해 완벽하지 않다.