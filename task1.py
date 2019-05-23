def input_page(fr):
        fw=open("test.txt","w")
        count=0
        pagestart= input("enter the starting page number")
        pagend=input("enter the last page number")
        for word in range(0,(25*pages),+1):
        count+=1
        if count>=(25*pages) and count<=(25*pageend):
                for j in i:
                        if j=='o' or j=='0':
                                j='0'
                        elif j=='e' or j=='E':
                                j='3'
                        elif j=='i' or j=='I'
                                j='1'
