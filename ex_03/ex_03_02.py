sh=input('enter hours:');
sr=input('enter rate:');
try:
    fh=float(sh);
    fr=float(sr);
except:
    print("Error, please enter numeric input")
    quit();
if fh>40:
    #print('overtime');
    reg=fh*fr ;
    otp=(fh-40)*(fr*0.5);
    #print(reg,otp)
    xp=reg+otp
else:
    #print('regular time')

    xp=fh*fr;


print('pay',xp);
