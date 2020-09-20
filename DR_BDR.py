from ipaddress import IPv4Address
BDR = 0
DR =0
Routerid = []
n = int(input("Enter the no. of IP Address you want to enter: "))
for i in range(0,n):
    ele = IPv4Address(input())
    Routerid.append(ele)
Routerid = sorted(Routerid)
BDR = Routerid[0]
DR = BDR
Routerid = sorted(Routerid)
BDR = Routerid[1]
print("Designated Router",DR)
print("Border Designated Router",BDR)

