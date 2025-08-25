class differentfunction():
    def triangle():
        Height=int(input("Height:"))
        leng=int(input("length:"))
        print("Area formula :(Height*Weight)/2")
        mull=(Height*leng)/2
        print("Area of triangle:",mull)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breath=int(input("Breath:"))
        print("perimeter formula: Height1+Height2+Breath")
        total=Height1+Height2+Breath
        print("perimeter of triangle:",total)
    

    def percentage() :
        sub1=int(input("Subject1 :"))
        sub2=int(input("Subject2 :")) 
        sub3=int(input("Subject3 :"))
        sub4=int(input("Subject4 :"))
        sub5=int(input("Subject5 :"))
        total=sub1+sub2+sub3+sub4+sub5
        print("Total",total)
        per=total/500*100
        print("Percentage : ",per)
    

    def Elegible():
        gen=str(input("Your gender: "))
        ag=int(input("Your Age: "))
        if(("male"==gen.lower()) & (ag>=21)):
            print("ElIGIBLE")
        elif(("female"==gen.lower()) & (ag>=18)):
            print(" ElIGIBLE")
        else:
            print(" NOT ElIGIBLE")
    

    def oddeven():
        num=int(input("Enter a number: "))
        if (num%2==0):
            print("52452 is  Even number")
        else:
            print("52452 is Odd number")
    

    def subfields():
        List=["machine language","neural network","robotics","vission","speech porcessing","natural language processing"]
        print("Sub-fields in AI are:")
        for lag in List:
            print(lag)