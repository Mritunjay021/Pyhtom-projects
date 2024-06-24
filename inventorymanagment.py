import json
import time

fd=open("Records.json",'r')
js=fd.read()
fd.close()
sale=""

record=json.loads(js)

print("-"*15+"MENU"+"-"*15)

for key in record.keys():
    print(key,":",record[key]["Name"],"\t|",record[key]["Price"],"\t|",record[key]["Quantity"])

print("-"*34)

ui_name=input("Enter your name")
ui_mail=input("Enter your mail")
ui_num=input("Enter your contact number")
ui_pr=str(input("Enter the product id"))
ui_qn=int(input("Enter the product quantity"))

if(ui_qn<=record[ui_pr]["Quantity"]):
    print("Name        :",record[ui_pr]["Name"])
    print("Price       :",record[ui_pr]["Price"])
    print("Quantiy     :",ui_qn)

    print("-"*34)

    cg=record[ui_pr]["Price"]*ui_qn*0.09
    sg=record[ui_pr]["Price"]*ui_qn*0.18
    
    print("CGST 9% of Amount: ",round(cg,2),"$")
    print("SGST 18% of Amount:",round(sg,2),"$")
    print("Total Amount      :",record[ui_pr]["Price"]*ui_qn,"$")
    print("Billing Amount    :",(record[ui_pr]["Price"]*ui_qn+cg+sg),"$")

    print("-"*34)
    sales ='1'+","+ui_name+","+ui_mail+","+ui_num+","+ui_pr+","+record[ui_pr]["Name"]+","+str(record[ui_pr]["Quantity"])+","+str(record[ui_pr]["Price"])+","+str(record[ui_pr]["Price"]*ui_qn+cg+sg)+","+time.ctime()+"\n"
    record[ui_pr]["Quantity"]=record[ui_pr]["Quantity"]-ui_qn

else:
    print("Sorry not enough quantity in the inventory.")
    print("Quantity in the inventory:-",record[ui_pr]["Quantity"])
    ch=input("Enter Y/y to purchase the product")
    print("-"*34)
    if(ch=="Y" or ch=="y"):
        print("Name        :",record[ui_pr]["Name"])
        print("Price       :",record[ui_pr]["Price"])
        print("Quantiy     :",record[ui_pr]["Quantity"])

        print("-"*34)
        cg=record[ui_pr]["Price"]*record[ui_pr]["Quantity"]*0.09
        sg=record[ui_pr]["Price"]*record[ui_pr]["Quantity"]*0.18
    
        print("CGST 9% of Amount: ",round(cg,2),"$")
        print("SGST 18% of Amount:",round(sg,2),"$")
        print("Total Amount      :",record[ui_pr]["Price"]*record[ui_pr]["Quantity"],"$")
        print("Billing Amount    :",(record[ui_pr]["Price"]*record[ui_pr]["Quantity"]+cg+sg),"$")

        sales ='1'+","+ui_name+","+ui_mail+","+ui_num+","+ui_pr+","+record[ui_pr]["Name"]+","+str(record[ui_pr]["Quantity"])+","+str(record[ui_pr]["Price"])+","+str(record[ui_pr]["Price"]*record[ui_pr]["Quantity"]+cg+sg)+","+time.ctime()+"\n"
        print("-"*34)
        record[ui_pr]["Quantity"]=0

print("Thank you!!")

fd=open("Sales.txt","a")
fd.write(sales)
fd.close()

js=json.dumps(record)
fd=open("Records.json","w")
fd.write(js)
fd.close()