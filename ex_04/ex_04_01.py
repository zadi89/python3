def computepay(hours,rate) :
    if hours>40:
    #print('overtime');
        reg=hours*rate ;
        otp=(hours-40)*(rate*0.5);
    #print(reg,otp)
        pay=reg+otp
    else:
        #print('regular time')
        pay=hours*rate;

    #print('pay',pay);
    return pay

sh=input('enter hours:');
sr=input('enter rate:');
fh=float(sh);
fr=float(sr);

xp=computepay(fh,fr);

print('Pay',xp)
