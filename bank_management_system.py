1
2
3
4
5
6
7
8
9
10
11
print("************************************************************")
print("========== WELCOME TO ITSOURCECODE BANKING SYSTEM ==========")
print("************************************************************")
print("========== (a). Open New Client Account ============")
print("========== (b). The Client Withdraw a Money ============")
print("========== (c). The Client Deposit a Money ============")
print("========== (d). Check Clients &amp; Balance ============")
print("========== (e). Quit ============")
print("************************************************************")
 
EnterLetter = input("Select a Letter from the Above Box menu : ")
The Code Below, Which is for the Client Registration Account
if EnterLetter == "a":
print(" Letter a is Selected by the Client")
NumberOfClient = eval(input("Number of Clients : "))
u = u + NumberOfClient

if u &gt; 7:
print("\n")
print("Client registration exceed reached or Client registration too low")
u = u - NumberOfClient
else:
while disk1 &lt;= u:
name = input("Write Your Fullname : ")
NamesOFClients.append(name)
pin = str(input("Please Write a Pin to Secure your Account : "))
ClientPins.append(pin)
ClientBalance = 0
ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances.append(ClientBalance)
print("\nName=", end=" ")
print(NamesOFClients[disk2])
print("Pin=", end=" ")
print(ClientPins[disk2])
print("Balance=", "P", end=" ")
print(ClientBalances[disk2], end=" ")
disk1 = disk1 + 1
disk2 = disk2 + 1
print("\nYour name is added to Client Table")
print("Your pin is added to Client Table")
print("Your balance is added to Client Table")
print("----New Client account created successfully !----")
print("\n")
print("Your Name is Available on the Client list now : ")
print(NamesOFClients)
print("\n")
print("Note! Please remember the Name and Pin")
print("========================================")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
if EnterLetter == "a":
print(" Letter a is Selected by the Client")
NumberOfClient = eval(input("Number of Clients : "))
u = u + NumberOfClient
 
if u &gt; 7:
print("\n")
print("Client registration exceed reached or Client registration too low")
u = u - NumberOfClient
else:
while disk1 &lt;= u:
name = input("Write Your Fullname : ")
NamesOFClients.append(name)
pin = str(input("Please Write a Pin to Secure your Account : "))
ClientPins.append(pin)
ClientBalance = 0
ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances.append(ClientBalance)
print("\nName=", end=" ")
print(NamesOFClients[disk2])
print("Pin=", end=" ")
print(ClientPins[disk2])
print("Balance=", "P", end=" ")
print(ClientBalances[disk2], end=" ")
disk1 = disk1 + 1
disk2 = disk2 + 1
print("\nYour name is added to Client Table")
print("Your pin is added to Client Table")
print("Your balance is added to Client Table")
print("----New Client account created successfully !----")
print("\n")
print("Your Name is Available on the Client list now : ")
print(NamesOFClients)
print("\n")
print("Note! Please remember the Name and Pin")
print("========================================")
 
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
The Code Below, Which is for the Client withdraw an Amount
elif EnterLetter == "b":<br>    v = 0<br>    print(" letter b is Selected by the Client")<br>    while v &lt; 1:<br>        w = -1<br>        name = input("Please Insert a name : ")<br>        pin = input("Please Insert a pin : ")<br>        while w &lt; len(NamesOFClients) - 1:<br>            w = w + 1<br>            if name == NamesOFClients[w]:<br>                if pin == ClientPins[w]:<br>                    v = v + 1<br>                    print("Your Current Balance:", "P", end=" ")<br>                    print(ClientBalances[w], end=" ")<br>                    print("\n")<br>                    ClientBalance = (ClientBalances[w])<br>                    ClientWithdrawal = eval(input("Insert value to Withdraw : "))<br>                    if ClientWithdrawal &gt; ClientBalance:<br>                        deposition = eval(input(<br>                            "Please Deposit a higher Value because your Balance mentioned above is not enough : "))<br>                        ClientBalance = ClientBalance + deposition<br>                        print("Your Current Balance:", "P", end=" ")<br>                        print(ClientBalance, end=" ")<br>                        ClientBalance = ClientBalance - ClientWithdrawal<br>                        print("-\n")<br>                        print("----Withdraw Successfully!----")<br>                        ClientBalances[w] = ClientBalance<br>                        print("Your New Balance: ", "P", ClientBalance, end=" ")<br>                        print("\n\n")<br>                    else:<br>                        ClientBalance = ClientBalance - ClientWithdrawal<br>                        print("\n")<br>                        print("----Withdraw Successfully!----")<br>                        ClientBalances[w] = ClientBalance<br>                        print("Your New Balance: ", "P", ClientBalance, end=" ")<br>                        print("\n")<br>        if v &lt; 1:<br>            print("Your name and pin does not match!\n")<br>            break<br>    mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
1
elif EnterLetter == "b":<br>    v = 0<br>    print(" letter b is Selected by the Client")<br>    while v &lt; 1:<br>        w = -1<br>        name = input("Please Insert a name : ")<br>        pin = input("Please Insert a pin : ")<br>        while w &lt; len(NamesOFClients) - 1:<br>            w = w + 1<br>            if name == NamesOFClients[w]:<br>                if pin == ClientPins[w]:<br>                    v = v + 1<br>                    print("Your Current Balance:", "P", end=" ")<br>                    print(ClientBalances[w], end=" ")<br>                    print("\n")<br>                    ClientBalance = (ClientBalances[w])<br>                    ClientWithdrawal = eval(input("Insert value to Withdraw : "))<br>                    if ClientWithdrawal &gt; ClientBalance:<br>                        deposition = eval(input(<br>                            "Please Deposit a higher Value because your Balance mentioned above is not enough : "))<br>                        ClientBalance = ClientBalance + deposition<br>                        print("Your Current Balance:", "P", end=" ")<br>                        print(ClientBalance, end=" ")<br>                        ClientBalance = ClientBalance - ClientWithdrawal<br>                        print("-\n")<br>                        print("----Withdraw Successfully!----")<br>                        ClientBalances[w] = ClientBalance<br>                        print("Your New Balance: ", "P", ClientBalance, end=" ")<br>                        print("\n\n")<br>                    else:<br>                        ClientBalance = ClientBalance - ClientWithdrawal<br>                        print("\n")<br>                        print("----Withdraw Successfully!----")<br>                        ClientBalances[w] = ClientBalance<br>                        print("Your New Balance: ", "P", ClientBalance, end=" ")<br>                        print("\n")<br>        if v &lt; 1:<br>            print("Your name and pin does not match!\n")<br>            break<br>    mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
The Code Below, Which is for the Client Deposit an Amount
elif EnterLetter == "c":
print("Letter c is selected by the Client")
x = 0
while x &lt; 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w &lt; len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
x = x + 1
print("Your Current Balance: ", "P", end=" ")
print(ClientBalances[w], end=" ")
ClientBalance = (ClientBalances[w])
print("\n")
ClientDeposition = eval(input("Enter the value you want to deposit : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances[w] = ClientBalance
print("\n")
print("----Deposition successful!----")
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if x &lt; 1:
print("Your name and pin does not match!\n")
break
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
elif EnterLetter == "c":
print("Letter c is selected by the Client")
x = 0
while x &lt; 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w &lt; len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
x = x + 1
print("Your Current Balance: ", "P", end=" ")
print(ClientBalances[w], end=" ")
ClientBalance = (ClientBalances[w])
print("\n")
ClientDeposition = eval(input("Enter the value you want to deposit : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances[w] = ClientBalance
print("\n")
print("----Deposition successful!----")
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if x &lt; 1:
print("Your name and pin does not match!\n")
break
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
The Code Below, which is for the Checking the Clients and Balances
elif EnterLetter == "d":
print("Letter d is selected by the Client")
w = 0
print("Client name list and balances mentioned below : ")
print("\n")
while w &lt;= len(NamesOFClients) - 1:
print("-&gt;.Customer =", NamesOFClients[w])
print("-&gt;.Balance =", "P", ClientBalances[w], end=" ")

print("\n")
w = w + 1
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
1
2
3
4
5
6
7
8
9
10
11
12
elif EnterLetter == "d":
print("Letter d is selected by the Client")
w = 0
print("Client name list and balances mentioned below : ")
print("\n")
while w &lt;= len(NamesOFClients) - 1:
print("-&gt;.Customer =", NamesOFClients[w])
print("-&gt;.Balance =", "P", ClientBalances[w], end=" ")
 
print("\n")
w = w + 1
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
The Code Below, Which is for the exit of Banking System
elif EnterLetter == "e":
print("letter e is selected by the client")
print("Thank you for using our banking system!")
print("\n")
print("Thank You and Come again")
print("God Bless")
break
else:
print("Invalid option selected by the Client")
print("Please Try again!")

mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
1
2
3
4
5
6
7
8
9
10
11
12
elif EnterLetter == "e":
print("letter e is selected by the client")
print("Thank you for using our banking system!")
print("\n")
print("Thank You and Come again")
print("God Bless")
break
else:
print("Invalid option selected by the Client")
print("Please Try again!")
 
mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
Complete source code of the Bank Management System
You are free to copy and execute this code to your computer.

NamesOFClients = ['Jomhel Dulla', 'Benny Salde', 'Jeremy Eriman', 'Given Bariacto', 'Carlan Pelobello', 'Ryan Manaay', 'Daniel Bandiola']
ClientPins = ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
ClientBalances = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 7
u = 0
while True:
# os.system("cls")
print("************************************************************")
print("========== WELCOME TO ITSOURCECODE BANKING SYSTEM ==========")
print("************************************************************")
print("========== (a). Open New Client Account ============")
print("========== (b). The Client Withdraw a Money ============")
print("========== (c). The Client Deposit a Money ============")
print("========== (d). Check Clients &amp; Balance ============")
print("========== (e). Quit ============")
print("************************************************************")

EnterLetter = input("Select a Letter from the Above Box menu : ")
if EnterLetter == "a":
print(" Letter a is Selected by the Client")
NumberOfClient = eval(input("Number of Clients : "))
u = u + NumberOfClient

if u &gt; 7:
print("\n")
print("Client registration exceed reached or Client registration too low")
u = u - NumberOfClient
else:
while disk1 &lt;= u:
name = input("Write Your Fullname : ")
NamesOFClients.append(name)
pin = str(input("Please Write a Pin to Secure your Account : "))
ClientPins.append(pin)
ClientBalance = 0
ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances.append(ClientBalance)
print("\nName=", end=" ")
print(NamesOFClients[disk2])
print("Pin=", end=" ")
print(ClientPins[disk2])
print("Balance=", "P", end=" ")
print(ClientBalances[disk2], end=" ")
disk1 = disk1 + 1
disk2 = disk2 + 1
print("\nYour name is added to Client Table")
print("Your pin is added to Client Table")
print("Your balance is added to Client Table")
print("----New Client account created successfully !----")
print("\n")
print("Your Name is Available on the Client list now : ")
print(NamesOFClients)
print("\n")
print("Note! Please remember the Name and Pin")
print("========================================")

mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "b":
v = 0
print(" letter b is Selected by the Client")
while v &lt; 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w &lt; len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
v = v + 1
print("Your Current Balance:", "P", end=" ")
print(ClientBalances[w], end=" ")
print("\n")
ClientBalance = (ClientBalances[w])
ClientWithdrawal = eval(input("Insert value to Withdraw : "))
if ClientWithdrawal &gt; ClientBalance:
deposition = eval(input(
"Please Deposit a higher Value because your Balance mentioned above is not enough : "))
ClientBalance = ClientBalance + deposition
print("Your Current Balance:", "P", end=" ")
print(ClientBalance, end=" ")
ClientBalance = ClientBalance - ClientWithdrawal
print("-\n")
print("----Withdraw Successfully!----")
ClientBalances[w] = ClientBalance
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n\n")
else:
ClientBalance = ClientBalance - ClientWithdrawal
print("\n")
print("----Withdraw Successfully!----")
ClientBalances[w] = ClientBalance
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if v &lt; 1:
print("Your name and pin does not match!\n")
break
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "c":
print("Letter c is selected by the Client")
x = 0
while x &lt; 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w &lt; len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
x = x + 1
print("Your Current Balance: ", "P", end=" ")
print(ClientBalances[w], end=" ")
ClientBalance = (ClientBalances[w])
print("\n")
ClientDeposition = eval(input("Enter the value you want to deposit : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances[w] = ClientBalance
print("\n")
print("----Deposition successful!----")
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if x &lt; 1:
print("Your name and pin does not match!\n")
break
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "d":
print("Letter d is selected by the Client")
w = 0
print("Client name list and balances mentioned below : ")
print("\n")
while w &lt;= len(NamesOFClients) - 1:
print("-&gt;.Customer =", NamesOFClients[w])
print("-&gt;.Balance =", "P", ClientBalances[w], end=" ")

print("\n")
w = w + 1
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
elif EnterLetter == "e":
print("letter e is selected by the client")
print("Thank you for using our banking system!")
print("\n")
print("Thank You and Come again")
print("God Bless")
break
else:
print("Invalid option selected by the Client")
print("Please Try again!")

mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
NamesOFClients = ['Jomhel Dulla', 'Benny Salde', 'Jeremy Eriman', 'Given Bariacto', 'Carlan Pelobello', 'Ryan Manaay', 'Daniel Bandiola']
ClientPins = ['0001', '0002', '0003', '0004', '0005', '0006', '0007']
ClientBalances = [10000, 20000, 30000, 40000, 50000, 60000, 70000]
ClientDeposition = 0
ClientWithdrawal = 0
ClientBalance = 0
disk1 = 1
disk2 = 7
u = 0
while True:
# os.system("cls")
print("************************************************************")
print("========== WELCOME TO ITSOURCECODE BANKING SYSTEM ==========")
print("************************************************************")
print("========== (a). Open New Client Account ============")
print("========== (b). The Client Withdraw a Money ============")
print("========== (c). The Client Deposit a Money ============")
print("========== (d). Check Clients &amp; Balance ============")
print("========== (e). Quit ============")
print("************************************************************")
 
EnterLetter = input("Select a Letter from the Above Box menu : ")
if EnterLetter == "a":
print(" Letter a is Selected by the Client")
NumberOfClient = eval(input("Number of Clients : "))
u = u + NumberOfClient
 
if u &gt; 7:
print("\n")
print("Client registration exceed reached or Client registration too low")
u = u - NumberOfClient
else:
while disk1 &lt;= u:
name = input("Write Your Fullname : ")
NamesOFClients.append(name)
pin = str(input("Please Write a Pin to Secure your Account : "))
ClientPins.append(pin)
ClientBalance = 0
ClientDeposition = eval(input("Please Insert a Money to Deposit to Start an Account : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances.append(ClientBalance)
print("\nName=", end=" ")
print(NamesOFClients[disk2])
print("Pin=", end=" ")
print(ClientPins[disk2])
print("Balance=", "P", end=" ")
print(ClientBalances[disk2], end=" ")
disk1 = disk1 + 1
disk2 = disk2 + 1
print("\nYour name is added to Client Table")
print("Your pin is added to Client Table")
print("Your balance is added to Client Table")
print("----New Client account created successfully !----")
print("\n")
print("Your Name is Available on the Client list now : ")
print(NamesOFClients)
print("\n")
print("Note! Please remember the Name and Pin")
print("========================================")
 
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "b":
v = 0
print(" letter b is Selected by the Client")
while v &lt; 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w &lt; len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
v = v + 1
print("Your Current Balance:", "P", end=" ")
print(ClientBalances[w], end=" ")
print("\n")
ClientBalance = (ClientBalances[w])
ClientWithdrawal = eval(input("Insert value to Withdraw : "))
if ClientWithdrawal &gt; ClientBalance:
deposition = eval(input(
"Please Deposit a higher Value because your Balance mentioned above is not enough : "))
ClientBalance = ClientBalance + deposition
print("Your Current Balance:", "P", end=" ")
print(ClientBalance, end=" ")
ClientBalance = ClientBalance - ClientWithdrawal
print("-\n")
print("----Withdraw Successfully!----")
ClientBalances[w] = ClientBalance
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n\n")
else:
ClientBalance = ClientBalance - ClientWithdrawal
print("\n")
print("----Withdraw Successfully!----")
ClientBalances[w] = ClientBalance
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if v &lt; 1:
print("Your name and pin does not match!\n")
break
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "c":
print("Letter c is selected by the Client")
x = 0
while x &lt; 1:
w = -1
name = input("Please Insert a name : ")
pin = input("Please Insert a pin : ")
while w &lt; len(NamesOFClients) - 1:
w = w + 1
if name == NamesOFClients[w]:
if pin == ClientPins[w]:
x = x + 1
print("Your Current Balance: ", "P", end=" ")
print(ClientBalances[w], end=" ")
ClientBalance = (ClientBalances[w])
print("\n")
ClientDeposition = eval(input("Enter the value you want to deposit : "))
ClientBalance = ClientBalance + ClientDeposition
ClientBalances[w] = ClientBalance
print("\n")
print("----Deposition successful!----")
print("Your New Balance: ", "P", ClientBalance, end=" ")
print("\n")
if x &lt; 1:
print("Your name and pin does not match!\n")
break
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
elif EnterLetter == "d":
print("Letter d is selected by the Client")
w = 0
print("Client name list and balances mentioned below : ")
print("\n")
while w &lt;= len(NamesOFClients) - 1:
print("-&gt;.Customer =", NamesOFClients[w])
print("-&gt;.Balance =", "P", ClientBalances[w], end=" ")
 
print("\n")
w = w + 1
mainMenu = input(" Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_ ")
elif EnterLetter == "e":
print("letter e is selected by the client")
print("Thank you for using our banking system!")
print("\n")
print("Thank You and Come again")
print("God Bless")
break
else:
print("Invalid option selected by the Client")
print("Please Try again!")
 
mainMenu = input("Press Enter Key to go Back to Main Menu to Conduct Another Transaction or Quit_")
