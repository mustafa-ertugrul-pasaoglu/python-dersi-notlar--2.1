def bmi_hesap(kilo,boy) :

bmi = kilo / (boy/100)**2 

if(bmi<18) :
    print("zayıf")
if(bmi<25) :
    print("normal")
if(bmi<35) :
    print("kilolu")        