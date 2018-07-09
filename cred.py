
O=10
A=9
B=8
C=7
D=6
suma=0
vale=0
    

o=int(input("Enter the no of sem:"))
for i in range(o):
    list=[]
    n= int(input("Enter the no of subjects:"))
    for i in range(n):
        name=input("Enter the name of subject:")
        sub_credit=int(input("enter the credits for that subject:"))
        list.insert(i, sub_credit)
    print ("The credit's are:", list)
    fine=[]
    for i in range(n):
        grde=int(input("enter the Grade for that subject rspectively"))
        fine.insert(i, grde)
    print ("The lists replaced with grade value", fine)
    li=[]
    for i in range(n):
        val=list[i]*fine[i]
        li.insert(i, val)
    print ("list for credit*grade for each subject", li)
    k=sum(li)
    m=sum(list)
    print("k")
    print("m")
    totalgpa=float(k)/float(m)
    grde_point=round(totalgpa,2)
    print("The GPA for current Semester is:", grde_point)
    suma=suma+k
    vale=vale+m
tot_crd=float(suma)/float(vale)
cgpas=round(tot_crd,2)
print("The CGPA for sem is:", cgpas)



    
        


    
