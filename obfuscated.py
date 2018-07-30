import re
def OMOmOO(omoOmOmoOm):
    mmooOmMmooOM=[]
    for mmMMOMmmoom in str(omoOmOmoOm):
        mmooOmMmooOM.append(str(ord(mmMMOMmmoom)))
    mOmOO=len(mmooOmMmooOM)-1
    OoMmMmoom=0
    for mMooOoMOOOOmmOMom in mmooOmMmooOM:
        OoMmMmoom+=(10**mOmOO)*int(chr(int(mMooOoMOOOOmmOMom)))
        mOmOO-=1
    return OoMmMmoom
def OmoMOmOM(MMmooOMOOM):
    MOOmmmmMOOmOoOmmMoO=[]
    for mmmOmOOOM in str(MMmooOMOOM):
        MOOmmmmMOOmOoOmmMoO.append(str(ord(mmmOmOOOM)))
    moMMoO=len(MOOmmmmMOOmOoOmmMoO)-1
    mMmoooMmOOmMOMmMO=0
    for oMooMMoO in MOOmmmmMOOmOoOmmMoO:
        mMmoooMmOOmMOMmMO+=(10**moMMoO)*int(chr(int(oMooMMoO)))
        moMMoO-=1
    return mMmoooMmOOmMOMmMO
def omOOMOoM(omMmMmmooMoomO):
    mmoMooOO=[]
    for mommmOmMmmMMmmmm in str(omMmMmmooMoomO):
        mmoMooOO.append(str(ord(mommmOmMmmMMmmmm)))
    mmOoOomMOooMMO=len(mmoMooOO)-1
    oomOMOOMoOmoo=0
    for OoOMm in mmoMooOO:
        oomOMOOMoOmoo+=(10**mmOoOomMOooMMO)*int(chr(int(OoOMm)))
        mmOoOomMOooMMO-=1
    return oomOMOOMoOmoo
def OOmMMmOmomoOmmm(MOMooMoMmMoomMo):
    oMmMoOMomM=[]
    for omOmMoomMmOmOmO in str(MOMooMoMmMoomMo):
        oMmMoOMomM.append(str(ord(omOmMoomMmOmOmO)))
    OMMOMoMMoOm=len(oMmMoOMomM)-1
    omOmmMOommmmmmOoM=0
    for OMOmmM in oMmMoOMomM:
        omOmmMOommmmmmOoM+=(10**OMMOMoMMoOm)*int(chr(int(OMOmmM)))
        OMMOMoMMoOm-=1
    return omOmmMOommmmmmOoM
def MOmoOommoMomMom(OMOOMmOMOmommM):
    OMmMM=[]
    for oMmoOmOmmOOoomMOM in str(OMOOMmOMOmommM):
        OMmMM.append(str(ord(oMmoOmOmmOOoomMOM)))
    OOMoomMOmOomM=len(OMmMM)-1
    oommooMOmOomOMMoMom=0
    for oMOoOO in OMmMM:
        oommooMOmOomOMMoMom+=(10**OOMoomMOmOomM)*int(chr(int(oMOoOO)))
        OOMoomMOmOomM-=1
    return oommooMOmOomOMMoMom
def oOOmMmOMOomOmoooMomo(mMOMmMMoO):
    MOmMOM=[]
    for OOMoMmOmOMmMoOMMoOmm in str(mMOMmMMoO):
        MOmMOM.append(str(ord(OOMoMmOmOMmMoOMMoOmm)))
    oomMmmMoOoOMMmmOMO=len(MOmMOM)-1
    ooMoooMOmMoMMMmoMOoM=0
    for oomOmoMOOmooOoOmOm in MOmMOM:
        ooMoooMOmMoMMMmoMOoM+=(10**oomMmmMoOoOMMmmOMO)*int(chr(int(oomOmoMOOmooOoOmOm)))
        oomMmmMoOoOMMmmOMO-=1
    return ooMoooMOmMoMMMmoMOoM
def OMMOmOOmmom(oommmmM):
    MOMomO=1
    while oommmmM>1:
        for ommMmOoOM in range(2,oommmmM+1):
            if oommmmM%ommMmOoOM==0:
                oommmmM//=ommMmOoOM
                MOMomO*=ommMmOoOM
                break
    return MOMomO
def OOOMMmOmOOoOom(oomoOMMOmOoMommMMM):
    MMMooomOmOMmOoOM=[]
    for MmmoMMoOo in str(oomoOMMOmOoMommMMM):
        MMMooomOmOMmOoOM.append(str(ord(MmmoMMoOo)))
    omMoomMOOOOomMoM=len(MMMooomOmOMmOoOM)-1
    OmmMO=0
    for oOoMmMOmoommm in MMMooomOmOMmOoOM:
        OmmMO+=(10**omMoomMOOOOomMoM)*int(chr(int(oOoMmMOmoommm)))
        omMoomMOOOOomMoM-=1
    return OmmMO
def mmoOOmMmomOom(OMoOoOoMOMOO):
    OOMMMMOmoOOOoOmmOmmo=[]
    for MMoommomOOMomOOOMm in str(OMoOoOoMOMOO):
        OOMMMMOmoOOOoOmmOmmo.append(str(ord(MMoommomOOMomOOOMm)))
    oMOOOomOOm=len(OOMMMMOmoOOOoOmmOmmo)-1
    mOMmmoOOMoOmmOo=0
    for MMOOMm in OOMMMMOmoOOOoOmmOmmo:
        mOMmmoOOMoOmmOo+=(10**oMOOOomOOm)*int(chr(int(MMOOMm)))
        oMOOOomOOm-=1
    return mOMmmoOOMoOmmOo
def MOmMMo(mmMooOMoMOomOmoooOMm):
    OomMmmOoMoOOm=[]
    for OOmmoOm in str(mmMooOMoMOomOmoooOMm):
        OomMmmOoMoOOm.append(str(ord(OOmmoOm)))
    MmMmommo=len(OomMmmOoMoOOm)-1
    oMMmMoOmOMM=0
    for MmmMOMmmomMoooMoMOOo in OomMmmOoMoOOm:
        oMMmMoOmOMM+=(10**MmMmommo)*int(chr(int(MmmMOMmmomMoooMoMOOo)))
        MmMmommo-=1
    return oMMmMoOmOMM
def mOomoOMMomoOomMmm(OOmmoMOoom):
    mMOOoOMMmoOOommOMmM=[]
    for mooOMOOmOMmmMMm in str(OOmmoMOoom):
        mMOOoOMMmoOOommOMmM.append(str(ord(mooOMOOmOMmmMMm)))
    MMMMomoomOoOomo=len(mMOOoOMMmoOOommOMmM)-1
    omOoOOOmoMMOMo=0
    for OmommMoOoomMMomoOoM in mMOOoOMMmoOOommOMmM:
        omOoOOOmoMMOMo+=(10**MMMMomoomOoOomo)*int(chr(int(OmommMoOoomMMomoOoM)))
        MMMMomoomOoOomo-=1
    return omOoOOOmoMMOMo
def oOMmoOMOmOo(MOOoMMmooMo):
    omMomMOO=[]
    for omOMOOOoMOOmoOo in str(MOOoMMmooMo):
        omMomMOO.append(str(ord(omOMOOOoMOOmoOo)))
    ommmmOOmo=len(omMomMOO)-1
    OmomoMOmMmmoOMMoMOoo=0
    for OmmoM in omMomMOO:
        OmomoMOmMmmoOMMoMOoo+=(10**ommmmOOmo)*int(chr(int(OmmoM)))
        ommmmOOmo-=1
    return OmomoMOmMmmoOMMoMOoo
def OMmoMMOo(omMMomM):
    MOmMoOmmooOoO=[]
    for MMMOOOooooM in str(omMMomM):
        MOmMoOmmooOoO.append(str(ord(MMMOOOooooM)))
    moOMmoOo=len(MOmMoOmmooOoO)-1
    momOmMoMmmMmm=0
    for ooOOMO in MOmMoOmmooOoO:
        momOmMoMmmMmm+=(10**moOMmoOo)*int(chr(int(ooOOMO)))
        moOMmoOo-=1
    return momOmMoMmmMmm
def MMMomMoOooOmMomOomm(mmMomOo):
    mOOoommmOoO=1
    while mmMomOo>1:
        for OOmMOmomomMoOOooMO in range(2,mmMomOo+1):
            if mmMomOo%OOmMOmomomMoOOooMO==0:
                mmMomOo//=OOmMOmomomMoOOooMO
                mOOoommmOoO*=OOmMOmomomMoOOooMO
                break
    return mOOoommmOoO
def MmmmooMmmOmOmooOoM(mooOoMMomoomMOoomMm):
    mmMMo=[]
    for mOOoO in str(mooOoMMomoomMOoomMm):
        mmMMo.append(str(ord(mOOoO)))
    OmoOoMOMMOm=len(mmMMo)-1
    OoOmO=0
    for ooOMMMmomMoMMoM in mmMMo:
        OoOmO+=(10**OmoOoMOMMOm)*int(chr(int(ooOMMMmomMoMMoM)))
        OmoOoMOMMOm-=1
    return OoOmO
def mMoOOooMOOMmmOm(omOmM):
    mmMMMM=[]
    for OMOmoMO in str(omOmM):
        mmMMMM.append(str(ord(OMOmoMO)))
    ooOmoMOoo=len(mmMMMM)-1
    oomMo=0
    for omoommmmOmOOM in mmMMMM:
        oomMo+=(10**ooOmoMOoo)*int(chr(int(omoommmmOmOOM)))
        ooOmoMOoo-=1
    return oomMo
def mMMooOMMmOMMMMOm(moMOoOmMoOmooomM):
    oOMMMmoOmMmOoMOMoMMO=[]
    for OMooOmoo in str(moMOoOmMoOmooomM):
        oOMMMmoOmMmOoMOMoMMO.append(str(ord(OMooOmoo)))
    omMooOoMmmMMM=len(oOMMMmoOmMmOoMOMoMMO)-1
    OooMOMoMmoMoOoOOmMMm=0
    for OmMmOmMmMOOoMOmmMMOo in oOMMMmoOmMmOoMOMoMMO:
        OooMOMoMmoMoOoOOmMMm+=(10**omMooOoMmmMMM)*int(chr(int(OmMmOmMmMOOoMOmmMMOo)))
        omMooOoMmmMMM-=1
    return OooMOMoMmoMoOoOOmMMm
OmOOMMMOMmoMmMOO= OMOmOO(10)
def oooOoOooMMOM(momoM):
    if momoM == 0:
        return 1
    return momoM * oooOoOooMMOM(momoM - 1)
mmMmm= OmoMOmOM(0)
OmMoMMMmMoMMmOOmMmo = []
while True:
    oomooOMmOOoMMMMMOm = False
    if oomooOMmOOoMMMMMOm:
        OmMoMMMmMoMMmOOmMmo.append(oomooOMmOOoMMMMMOm.upper())
    else:
        break;
    break
mMMOommmoOoomoOMmmMo= omOOMOoM(10)
MMoMMO= OOmMMmOmomoOmmm(1)
OOmOOOMOoooooM = []
OMmOOMmmmoOMoOmOMmm=(1,2)
for MOmmoMoOOMMm in OMmOOMmmmoOMoOmOMmm:
    MmomMO = MOmmoMoOOMMm
    if not MmomMO%5:
        OOmOOOMOoooooM.append(MOmmoMoOOMMm)
MOOMoMmOomooomOmm= MOmoOommoMomMom(1)
MmmOO = []
for omoooMOmoOMMOmoO in range(1000, 1005):
    oomooOMmOOoMMMMMOm = str(omoooMOmoOMMOmoO)
    if (int(oomooOMmOOoMMMMMOm[0])%2==0) and (int(oomooOMmOOoMMMMMOm[1])%2==0) and (int(oomooOMmOOoMMMMMOm[2])%2==0) and (int(oomooOMmOOoMMMMMOm[3])%2==0):
        MmmOO.append(oomooOMmOOoMMMMMOm)
omoOMMMMmooMMOomoO= oOOmMmOMOomOmoooMomo(2)
OoMOOoOo= OMMOmOOmmom(3)
mMMMMmMoomO = []
while True:
    oomooOMmOOoMMMMMOm = 'I love Cow language'
    if not oomooOMmOOoMMMMMOm:
        break
    mMMMMmMoomO.append(tuple(oomooOMmOOoMMMMMOm.split(",")))
    break
omommOMmmoomoMMMOomO= OOOMMmOmOOoOom(0)
OoOmOM= mmoOOmMmomOom(0)
oOOMmmoMmo = (1, 2, 3, 4, 5, 6)
def MMmOOMmoOoooMoMOo(OOMOmoMOOMoMOO):
    omoooMOmoOMMOmoO= MOmMMo(0)
    while omoooMOmoOMMOmoO<OOMOmoMOOMoMOO:
        oMoMMoMom=omoooMOmoOMMOmoO
        for OOOmooOOoo in range(0, 0):
            omoooMOmoOMMOmoO = omoooMOmoOMMOmoO + 1
        if oMoMMoMom%7==0:
            yield oMoMMoMom
OOmmommMoOooOMO = "mMo"
MmooOo= mOomoOMMomoOomMmm(0)
moooMOMoOMmmm= oOMmoOMOmOo(1)
def oMOmOoOomOMOmMMMo(OMOoMmMMOMOoOmoM, OOMMOMMmOm):
 return OMOoMmMMOMOoOmoM+OOMMOMMmOm
def mOOOoOOO(OOMOmoMOOMoMOO):
 if OOMOmoMOOMoMOO%2 == 0:
  print("It is an even number")
 else:
  print("It is an odd number")
OoOomomoOMomOMMOMmoo= OMmoMMOo(0)
MOooooOommmmm= MMMomMoOooOmMomOomm(2)
mOmOoomM= MmmmooMmmOmOmooOoM(0)
def OMOoOm():
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from celsius")
    print(" 'f' convert from fahrenheit")
    print(" 'q' quit the program")
def mMoMOMomMo(MMOmOMMmOMmOO):
    return 9.0/5.0*MMOmOMMmOMmOO+32
def OMmomOM(OMmmmmMm):
    return (OMmmmmMm - 32.0)*5.0/9.0    
oomOmOOMMm = {}
mmmomoMOOmM = {}
OoOOoMMo = {}
def Mooomm(OOMOmoMOOMoMOO):  
 if OOMOmoMOOMoMOO <= 1:  
   return 0
 else:  
  return(Mooomm(OOMOmoMOOMoMOO-1) + Mooomm(OOMOmoMOOMoMOO-2))  
def OoMomOOOOomMMmOM(MomMOOmMOO):
 MoMomoOmO = open('./keymaps/keymaps_' + MomMOOmMOO + '.txt', 'r')
 OMOoOoomoOm = MoMomoOmO.readlines()
 MMoOomMomMOMOOomMm = {}
 for moMomMmOooMMOMO in OMOoOoomoOm:
  ommmomMommomMomoMM = re.search('\d', moMomMmOooMMOMO)
  momooo = moMomMmOooMMOMO.rfind(' ')
  MMoOomMomMOMOOomMm[moMomMmOooMMOMO[ommmomMommomMomoMM.start():momooo]] = moMomMmOooMMOMO[momooo + 1 : len(moMomMmOooMMOMO) - 1]
 MoMomoOmO.close()
 return MMoOomMomMOMOOomMm
oOmoMOoMMMoMOmO = 0.0
moMOMOmoMMmOmmmMmOmM= mMoOOooMOOMmmOm(0)
MMMmmoOOmMMoooo = False
while not MMMmmoOOmMMoooo:
    MOOmmOMOmmOmMOMo= mMMooOMMmOMMMMOm(1)
    if MOOmmOMOmmOmMOMo > 0:
        MMMmmoOOmMMoooo = True
    else:
        oOmoMOoMMMoMOmO += MOOmmOMOmmOmMOMo
        moMOMOmoMMmOmmmMmOmM += 1
def OomMmMmm():
 oOomOoOO = open('final_logger.txt', 'w')
 ooomMOOmMoOMm = open('logger_temp.txt', 'r')
 mooooomOooommoom = ooomMOOmMoOMm.readlines()
 ooomMOOmMoOMm.close()
 for OooOoMMoMoMMmMmoM, moMomMmOooMMOMO in enumerate(mooooomOooommoom):
  if 'CEST' in moMomMmOooMMOMO and OooOoMMoMoMMmMmoM + 6 < len(mooooomOooommoom) and 'CEST' not in mooooomOooommoom[OooOoMMoMoMMmMmoM + 6]:
   oOomOoOO.write(moMomMmOooMMOMO)
  elif 'premuto' in moMomMmOooMMOMO:
   if '42' not in moMomMmOooMMOMO and '54' not in moMomMmOooMMOMO and '100' not in moMomMmOooMMOMO:
    oOomOoOO.write(moMomMmOooMMOMO)
   elif moMomMmOooMMOMO != mooooomOooommoom[OooOoMMoMoMMmMmoM - 1]:
    oOomOoOO.write(moMomMmOooMMOMO)
  elif 'rilasciato' in moMomMmOooMMOMO:
   if '42' in moMomMmOooMMOMO or '54' in moMomMmOooMMOMO or '100' in moMomMmOooMMOMO:
    oOomOoOO.write(moMomMmOooMMOMO)
 oOomOoOO.close()
moOMoMMmmmOoo = open('output.txt', 'w')
while(MMoMMO != 1):
 if ooMmMMoomoMMmMMMmmoO % momoM == 0 and ooMmMMoomoMMmMMMmmoO % y == 0:
  mMMOmoMooooMMooomOMm = ooMmMMoomoMMmMMMmmoO
 break
 ooMmMMoomoMMmMMMmmoO += 1
oomOmOOMMm = OoMomOOOOomMMmOM('default')
mmmomoMOOmM = OoMomOOOOomMMmOM('ctrl')
OoOOoMMo = OoMomOOOOomMMmOM('altgr')
OmooooooMM = False
omOmmMoOmooMOmmmmOO = False
OomMmMmm()
OOOOOmOmo = open('final_logger.txt', 'r')
while OOmmommMoOooOMO != "q":
    if OOmmommMoOooOMO == "c":
        OOmmm = input("Celsius temperature:")
        print("Fahrenheit:",mMoMOMomMo(OOmmm))
    elif OOmmommMoOooOMO == "f":
        OOmmm = input("Fahrenheit temperature:")
        print("Celsius:",OMmomOM(OOmmm))
    elif OOmmommMoOooOMO == "q":
        OMOoOm()
    else:
        OOmmommMoOooOMO = "OMG!! It's cow language <3 !!"
    break
for moMomMmOooMMOMO in OOOOOmOmo.readlines():
 if 'CEST' in moMomMmOooMMOMO:
  moOMoMMmmmOoo.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n' + moMomMmOooMMOMO + '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
 else:
  ommmomMommomMomoMM = re.search('\d', moMomMmOooMMOMO)
  momooo = moMomMmOooMMOMO.rfind(' ')
  OmomMOMoOMoMMMMOMo = moMomMmOooMMOMO[ommmomMommomMomoMM.start():momooo]
  if 'rilasciato' in moMomMmOooMMOMO:
   if OmomMOMoOMoMMMMOMo == '42' or OmomMOMoOMoMMMMOMo == '54':
    OmooooooMM = False
   elif OmomMOMoOMoMMMMOMo == '100':
    omOmmMoOmooMOmmmmOO = False
  elif 'premuto' in moMomMmOooMMOMO:
   if OmomMOMoOMoMMMMOMo == '42' or OmomMOMoOMoMMMMOMo == '54': 
    OmooooooMM = True 
   elif OmomMOMoOMoMMMMOMo == '100':
    omOmmMoOmooMOmmmmOO = True
   else:
    if OmooooooMM == True:
     moOMoMMmmmOoo.write(mmmomoMOOmM[OmomMOMoOMoMMMMOMo])
    elif omOmmMoOmooMOmmmmOO == True:
     moOMoMMmmmOoo.write(OoOOoMMo[OmomMOMoOMoMMMMOMo])
    else:
     moOMoMMmmmOoo.write(oomOmOOMMm[OmomMOMoOMoMMMMOMo])
  else:
   print('Parse-Error: unknown line.')
OOOOOmOmo.close()
moOMoMMmmmOoo.close()
if MOOMoMmOomooomOmm == '1':
   omoOMMMMmooMMOomoO = add(omoOMMMMmooMMOomoO,OoMOOoOo)
elif MOOMoMmOomooomOmm == '2':
   omoOMMMMmooMMOomoO = subtract(omoOMMMMmooMMOomoO,OoMOOoOo)
elif MOOMoMmOomooomOmm == '3':
   omoOMMMMmooMMOomoO = multiply(omoOMMMMmooMMOomoO,OoMOOoOo)
elif MOOMoMmOomooomOmm == '4':
   omoOMMMMmooMMOomoO = divide(omoOMMMMmooMMOomoO,OoMOOoOo)