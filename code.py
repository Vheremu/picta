import os
from PIL import Image, ImageDraw,ImageFont



fontsfolder='C:\Windows\Fonts'
tahomaFont = ImageFont.truetype(os.path.join(fontsfolder, 'STENCIL.ttf'), 70)
impactFont = ImageFont.truetype(os.path.join(fontsfolder, 'impact.ttf'), 90)
sitkaFont = ImageFont.truetype(os.path.join(fontsfolder, 'Sitka.ttc'), 70)
def a1(firstname,surname,houseaddress,townaddress,inviterpost,invitee,inviteesurname,invitationpost,invitationpostid,token,date):
    im1=Image.open('m3.png')
    width,height=im1.size
    print(width,height)
    draw1 = ImageDraw.Draw(im1)
    draw1.text((150, 100), 'Invitation Letter', fill='black', font=impactFont)
    draw1.text((1240, 300), firstname+' '+surname, fill='black', font=tahomaFont)
    draw1.text((1240,375 ), 'The '+inviterpost, fill='black', font=tahomaFont)
    draw1.text((1240, 450), 'Picta Affiliate Program', fill='black', font=tahomaFont)
    draw1.text((1240, 525), houseaddress, fill='black', font=tahomaFont)
    draw1.text((1240, 600), townaddress, fill='black', font=tahomaFont)
    
    verdanabFont = ImageFont.truetype(os.path.join(fontsfolder, 'verdanab.ttf'), 50)
    draw1.text((1240, 725), date, fill='black', font=verdanabFont)
    draw1.text((150, 825), 'Dear '+invitee+' '+inviteesurname, fill='black', font=sitkaFont)
    draw1.text((150, 950), 'Ref : Invitation for membership with Picta Affiliate Program.', fill='black', font=tahomaFont)
    draw1.text((150, 1100), 'You are invited by '+firstname+' for membership with Picta Affiliate Program.You ', fill='black', font=verdanabFont)
    draw1.text((150, 1150), 'have been invited as a '+invitationpost+', the number '+invitationpostid+' highest', fill='black', font=verdanabFont)
    draw1.text((150,1200), 'rank from the President who is number 1 rank. Your rank comes with all the  ', fill='black', font=verdanabFont)
    draw1.text((150, 1250), 'benefits of being a '+invitationpost+' with Picta Affiliate Program.', fill='black', font=verdanabFont)
    draw1.text((150, 1350), 'To begin as '+invitationpost+', you have been given token '+token+'.', fill='black', font=verdanabFont)
    draw1.text((150, 1400), 'You have to either buy an add with your token or list your own add with your ', fill='black', font=verdanabFont)
    draw1.text((150, 1450), 'Token on our website www.picta.com/ap. Your account will be upgraded  ', fill='black', font=verdanabFont)
    draw1.text((150, 1500), ',and you will be able to make money from sales with the add you bought ', fill='black', font=verdanabFont)
    draw1.text((150, 1550), 'or listed, as well as from commissions coming from sales from your own ', fill='black', font=verdanabFont)
    draw1.text((150, 1600), 'recruitments! You will report to, myself '+firstname+' '+surname+' for more information.', fill='black', font=verdanabFont)
    draw1.text((150, 1700), 'Buying an Add means you can earn money by selling products that are ', fill='black', font=verdanabFont)
    draw1.text((150, 1750), 'advertised on the add with our affiliate marketing program.Listing  your add  ', fill='black', font=verdanabFont)
    draw1.text((150, 1800), 'means you will make money when your products or service are sold with our sales ', fill='black', font=verdanabFont)
    draw1.text((150, 1850), 'based affiliate program. You can withdraw your earned income via Ecocash, ', fill='black', font=verdanabFont)
    draw1.text((150, 1900), 'Zipit or Innbucks. Buying or Listing an Add costs $5 only. ', fill='black', font=verdanabFont)
    draw1.text((150, 2000), 'Congradulations for reading through my letter. Joining Picta Affiliate  ', fill='black', font=verdanabFont)
    draw1.text((150, 2050), 'is the next step towards earning your extra money. We have a policy in ', fill='black', font=verdanabFont)
    draw1.text((150, 2100), 'which all members are given the right to be promoted to higher ranks, given', fill='black', font=verdanabFont)
   
    draw1.text((150, 2150), 'that they have have achieved their specified targets and the ranks are  ', fill='black', font=verdanabFont)

    draw1.text((150, 2200), 'available. All members have the right to monthly  allowances as well as a', fill='black', font=verdanabFont)
    
    draw1.text((150, 2250), 'yearly bonus, given that specified targets are achieved and the funds are', fill='black', font=verdanabFont)
   
    draw1.text((150, 2300), 'available. ', fill='black', font=verdanabFont)
  
    draw1.text((150, 2400), 'Your Faithfully', fill='black', font=verdanabFont)
    
    draw1.text((150, 2600), 'The '+inviterpost+', Picta Affiliate Program  ', fill='black', font=verdanabFont)
    
    draw1.text((150, 2500), firstname+' '+surname, fill='black', font=verdanabFont)
    draw1.text((120, 3000), 'Invitation Code: '+token, fill='black', font=impactFont)
    draw1.text((120, 3100), 'Website Link:www.picta.com/ap ', fill='black', font=impactFont)
    
    im1.save('static/invitationletters/m3.png')
def a2(firstname='tinashe',surname='vheremu',houseaddress='23rd ave falsetead road marlbreign',townaddress='marbrough harare',inviterpost='lieutenant',invitee='johani',inviteesurname='manyowa',invitationpost='member',invitationpostid='8',token='23456',date='20/04/24'):
    im1=Image.open('m3.png')
    width,height=im1.size
    print(width,height)
    draw1 = ImageDraw.Draw(im1)
    draw1.text((150, 100), 'Invitation Letter', fill='black', font=impactFont)
    draw1.text((1240, 300), firstname+' '+surname, fill='black', font=tahomaFont)
    draw1.text((1240,375 ), 'The '+inviterpost, fill='black', font=tahomaFont)
    draw1.text((1240, 450), 'Picta Affiliate Program', fill='black', font=tahomaFont)
    draw1.text((1240, 525), houseaddress, fill='black', font=tahomaFont)
    draw1.text((1240, 600), townaddress, fill='black', font=tahomaFont)
    
    verdanabFont = ImageFont.truetype(os.path.join(fontsfolder, 'verdanab.ttf'), 50)
    draw1.text((1240, 725), date, fill='black', font=verdanabFont)
    draw1.text((150, 825), 'Dear '+invitee+' '+inviteesurname, fill='black', font=sitkaFont)
    draw1.text((150, 950), 'Ref : Invitation for membership with Picta Affiliate Program.', fill='black', font=tahomaFont)
    draw1.text((150, 1100), 'You are invited by '+firstname+' for membership with Picta Affiliate Program.You ', fill='black', font=verdanabFont)
    draw1.text((150, 1150), 'have been invited as a '+invitationpost+', the number '+invitationpostid+' highest', fill='black', font=verdanabFont)
    draw1.text((150,1200), 'rank from the President who is number 1 rank. Your rank comes with all the  ', fill='black', font=verdanabFont)
    draw1.text((150, 1250), 'benefits of being a'+invitationpost+' with Picta Affiliate Program.', fill='black', font=verdanabFont)
    draw1.text((150, 1350), 'To begin as '+invitationpost+', you have been given token '+token+'.', fill='black', font=verdanabFont)
    draw1.text((150, 1400), 'You have to \n either buy an add with your token or list your own add with your ', fill='black', font=verdanabFont)
    draw1.text((150, 1450), 'Token on our website www.picta.com/ap. You account will be upgraded  ', fill='black', font=verdanabFont)
    draw1.text((150, 1500), ',and you will be able to make money from the add you bought as well as from ', fill='black', font=verdanabFont)
    draw1.text((150, 1550), 'commissions coming from your own recruitments! You will report to your ', fill='black', font=verdanabFont)
    draw1.text((150, 1600), 'recruiter, myself '+firstname+' '+surname+' for more information.', fill='black', font=verdanabFont)
    draw1.text((150, 1700), 'Buying an Add means you can earn money by selling products that are ', fill='black', font=verdanabFont)
    draw1.text((150, 1750), 'advertised on the add with our affiliate marketing program. You can withdraw ', fill='black', font=verdanabFont)
    draw1.text((150, 1800), 'your earned income via Ecocash, Zipit or Innbucks. Buying an Add costs $5', fill='black', font=verdanabFont)
    draw1.text((150, 1900), 'Listing  your add means you will make money when your products or services ', fill='black', font=verdanabFont)
    draw1.text((150, 1950), 'are sold with our sales based affiliate program. You can withdraw your earned', fill='black', font=verdanabFont)
    draw1.text((150, 2000), 'income via Ecocash, Zipit and Innbucks.Listing your Add costs $5.', fill='black', font=verdanabFont)
    draw1.text((150, 2100), 'Congradulations for reading through my letter. Joining Picta Affiliate  ', fill='black', font=verdanabFont)
    draw1.text((150, 2150), 'is the next step towards earning your extra money. We have a policy in ', fill='black', font=verdanabFont)
    draw1.text((150, 2200), 'which all members are given the right to be promoted to higher ranks given', fill='black', font=verdanabFont)
   
    draw1.text((150, 2250), 'that they have have achieved their specified targets and the ranks are  ', fill='black', font=verdanabFont)

    draw1.text((150, 2300), 'available. All members have the right to monthly  allowances as well as a', fill='black', font=verdanabFont)
    
    draw1.text((150, 2350), 'yearly bonus given that specified targets are achieved and the funds are', fill='black', font=verdanabFont)
   
    draw1.text((150, 2400), 'available. ', fill='black', font=verdanabFont)
  
    draw1.text((150, 2500), 'Your Faithfully', fill='black', font=verdanabFont)
    
    draw1.text((150, 2600), 'The '+inviterpost+', Picta Affiliate Program  ', fill='black', font=verdanabFont)
    
    draw1.text((150, 2700), firstname+' '+surname, fill='black', font=verdanabFont)
    draw1.text((120, 3000), 'Invitation Code: '+token, fill='black', font=impactFont)
    draw1.text((120, 3100), 'Website Link:www.picta.com/ap ', fill='black', font=impactFont)
    
    im1.save('m1.png')
a2()
def printpromo(image):
    im1=Image.open(image)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle((1500, 700, 2000, 1000), fill='red')
    draw1.text((1550, 710), 'Get 10% Off', fill='blue', font=tahomaFont)
    draw1.text((1550, 780), 'PROMO CODE', fill='white', font=tahomaFont)
    draw1.text((1550, 860), 'Your Code', fill='green', font=tahomaFont)
    draw1.text((1550, 930), 'Here!', fill='yellow', font=tahomaFont)
    return im1
    
    
    
    