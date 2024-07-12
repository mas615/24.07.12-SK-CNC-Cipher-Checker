#© 2024 MaJunYoung akwns615@gmail.com v4
import subprocess, sys, re
print("☆ SK C&C Security Team - Cipher Checker 2024 WITH nmap ☆")
secures = ["TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
           "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256"]
def cipher_check(command):
    temp = subprocess.check_output(command, shell=True, text=True)

    a = temp.split("\n")
    for i in a:
        if " - A" in i or " - B" in i or " - C" in i or " - D" in i or " - F" in i:
            i = re.sub(r" - .", "", i)
            if any(secure in i for secure in secures):
                print(i, "-- [SECURE]")
            else:
                print(i, "-- [WEEK]")
        else:
            print(i)

if len(sys.argv) < 2:
    print('사용법 : python cipher.py [URL] -p [PORT]')
    sys.exit(1)

#com = "nmap --script ssl-enum-ciphers sk.wd3.myworkdayjobs.com -p 443"
del sys.argv[0]
com ="nmap --script ssl-enum-ciphers "
for i in sys.argv:
    com += i+" "
cipher_check(com)