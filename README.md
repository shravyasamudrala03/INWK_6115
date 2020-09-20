# INWK_6115
Problem Statement:
Assume you have received a number of LSPs with router IDs of neighbors. Based on the smallest numerical value:
1.	Select a Backup Designated Router (BDR)
2.	Promote it to Designated Router (DR) and 
3.	Select again a BDR based on the same principle 
Note: As for as the datatype value of ID of router is concerned, you may use loopback address or any other format that can be compared.
Tips: Doing comparison of IDs, finding the lowest value, Updating variable values.



Summary of the Analysis:
From the problem statement, a Backup Designated(BDR) and Designated Router(DR) must be selected from a list of Router IDs (Router IDs are in the form of IP Address). The smallest ID is selected as Designated Router and second smallest as BDR.
But first BDR is selected, then it is promoted to DR and again a BDR is selected based on smallest value.


Test Plan:
Enter the no. of IP Address you want to enter: 6
192.168.1.5
192.168.1.34
192.168.1.3
192.168.1.10
192.168.1.15
192.168.1.20
Expected Result:
Based on the principle of smallest no.
Designated Router is 192.168.1.3
Backup Designated Router is 192.168.1.5
