#code here
Voda=str("082")
MTN=str("083")
CellC=str("084")
Voda2=str("076")
CellC2=str("062")
Vodacomtotal=0
MTNtotal=0
CellCtotal=0
for i in range (10):
	a=input("Enter your cellphone number")
	c=len(a)
	if c!=10:
		print("Error")
	else:
		if a[:3]==(Voda):
			print("Vodacom")
			Vodacomtotal=Vodacomtotal+1
		elif a[:3]==(MTN):
			print("MTN")
			MTNtotal=MTNtotal+1
		elif a[:3]==(CellC):
			print("CellC")
			CellCtotal=CellCtotal+1
		elif a[:3]==(Voda2):
			print("Vodacom")
			Vodacomtotal=Vodacomtotal+1
		elif a[:3]==(CellC2):
			print("CellC")
			CellCtotal=CellCtotal+1
		else:
			print("No service provider")
print("Vodacom total is", Vodacomtotal,"MTN total is", MTNtotal, "CellC total is", CellCtotal)
		
	
