class SubfieldsInAI():
    def subfields():
        print("Sub-fields in AI are:\nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
SubfieldsInAI.subfields()

class OddEvenClass():
    def OddEven():
        number=int(input("Enter a number: "))
        if(number%2==1):
            print(number,"is Even Number")
        else:
            print(number,"is Odd Number")
OddEvenClass.OddEven()

class eligibilityformarriage():
    def Eligible():
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        if(gender=="Male" and age<21):
            print("Not Eligible")
            message="Not Eligible"
        elif(gender=="Male" and age>=21):
            print("Eligible")
            message="Eligible"
        elif(gender=="Female" and age<18):
            print("Not Eligible")
            message="Not Eligible"
        elif(gender=="Female" and age>=18):
            print("Eligible")
            message="Eligible"
        return message
eligibilityformarriage.Eligible()

class FindPercentage():
    def percentage():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= "))
        Subject5=int(input("Subject5= "))
        total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total: ",total)
        result=(total/500)*100
        print("Percentage: ",result)
FindPercentage.percentage()

class triangle():
    def triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        Area=(height*breadth)/2
        print("Area of Triangle: ",Area)
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        Perimeter=height1+height2+breadth
        print("Perimeter of Triangle: ",Perimeter)
triangle.triangle()
