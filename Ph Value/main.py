import math
print("Do you want to calculate A: the pH value or B: the concentration of the substance")
auswahl = input()

if auswahl == "A":
    def ph_Wert():
        try:
                print("Specify the concentration of the substance")
                c = float(input())
                if c <= 0: 
                    print("The concentration must be greater than 0")
                    return
                formel = -math.log10(c)
                if formel <= 7:
                    print("It is an acidic solution")
                if formel >= 7:
                    print("It is a basic solution")
                if formel == 7:
                    print("It is a neutral solution")
                print("The pH value is",formel)
        except:
                print("Incorrect entry")
    ph_Wert()
    
if auswahl == "B":
    def konzentration():
        try:
                print("Specify the volume of a substance")
                V= float(input())
                
                Stoffmengefrage = input("Do you have the amount of substance Y/N?")
                if Stoffmengefrage == "Y":
                    print("Specify the amount of substance")
                    n = float(input())
                    formel_5 = n/V
                    print("The concentration is", formel_5,"mol")
                if Stoffmengefrage == "N":
                    print("Enter the mass")
                    m =float(input())
                    print("Enter the molar mass")
                    M= float(input())
                    formel_3 = m/M 
                    formel_4 = formel_3/V
                    print("is the amount of substance",formel_3,)
                    print("the concentration is", formel_4, "mol")
        except:
                    print("Incorrect entry")
    konzentration()
                    
                    
             