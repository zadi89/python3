sh=input('enter hours:');
sr=input('enter rate:');
fh=float(sh);
fr=float(sr);

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
