import csv
pyes=0
pno=0
def Bayes(data,item,col):
    N=len(data)   
    noc=0
    yesc=0    
    for row in data:
        if row[-1]=='yes':
            yesc+=1
        else:
            noc+=1 
            
    global pyes,pno                   
    pyes=yesc/N
    pno=noc/N
    itemy=0
    itemn=0
    for row in data:
        if row[col]==item:
            if row[-1]=='yes':
                itemy+=1
            else:
                itemn+=1   
    py=itemy/yesc 
    pn=itemn/noc    
    return py,pn   


def getData(file):
    
    csv_file = csv.reader(open(file))    
    data = []
    print(".........Traine data...........")
    for row in csv_file:
        data.append(row)
        print(row)        
    return data

def main():
    file = "C:/Users/Admin/Desktop/CAR.csv"
    data = getData(file)
    print("enter ur car specifaction?")
    x,y,z=input().split()
    p1y,p1n=Bayes(data[1:],x,0)
    p2y,p2n=Bayes(data[1:],y,1)
    p3y,p3n=Bayes(data[1:],z,2)
    
    resy=p1y*p2y*p3y*pyes
    resn=p1n*p2n*p3n*pno
    print(".......probality of ur car stolen =", resy)  
    
    print(".......probality of ur car not stolen =", resn)
    
    if(resy>resn):
        print(" UR CAR STOLEN CHANCE MORE>>>>>>>>>>>>>>")
    else:
        
        print(" UR CAR  STOLEN CHANCE LESS>>>>>>>>>>>>>>")

main()
    
