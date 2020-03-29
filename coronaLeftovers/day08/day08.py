import requests
import socket
import struct

#req = requests.get("http://68.183.210.250:32779")

sck = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def move(stre,tau):
    i = 0
    j = -1            
    for ch in stre.replace("\n","").replace("   ","0").replace(" ","").replace("||","|"):
        if ch == '|': 
            j += 1
        elif ch == 'B':
            tau[i*3+j] = 'B'
        elif ch == 'P':
            tau[i*3+j] = 'P'
        elif ch != '0': 
            break
        if j == 2:
            j = -1
            i += 1

    print(tau)
    return tau

def move2(stre,tau):
    i = 0
    j = -1            
    for ch in stre.replace("\n","").replace("   ","0").replace(" ","").replace("||","|"):
        if ch == '|': 
            j += 1
        elif ch == 'B':
            tau[i*6+j] = 'B'
        elif ch == 'P':
            tau[i*6+j] = 'P'
        elif ch != '0': 
            break
        if j == 5:
            j = -1
            i += 1

    print(tau)
    return tau


def rec(socket):
    pack = sck.recv(256)
            
    stre = pack.decode()
    print(stre)
    return stre


def attack():
    try:
        sck.connect(("68.183.210.250",32780))

        tau = []

        i = 0
        j = 0
        for i in range(3):
            for j in range(3):
                tau.append('E')

        print(tau)

        pack = sck.recv(256)
            
        stre = pack.decode().replace("\n","n").replace(" ","")

        sck.send("Galahad\n".encode())

        pack = sck.recv(256)
            
        stre = pack.decode()
        print(stre[:-1])

        pack = sck.recv(256)
            
        stre = pack.decode()
        print(stre)
        #print("stre.replace",stre.replace("\n","").replace("   ","0").replace(" ","").replace("||","|"))
            
        tau = move(stre,tau)

        sck.send("0,0".encode())   
            
        stre = rec(sck)
        tau = move(stre,tau)
        print(tau)
        if tau[1] == 'B' or tau[2] == 'B':
            sck.send("1,0".encode())
            stre = rec(sck)
            tau = move(stre,tau)
            if tau[6] == 'E':
                sck.send("2,0".encode())
                stre = rec(sck)
            else:
                sck.send("1,1".encode())
                stre = rec(sck)
                tau = move(stre,tau)
                if tau[5] == 'E':
                    sck.send("1,2".encode())
                    stre = rec(sck)
                else:
                    sck.send("2,2".encode())
                    stre = rec(sck)
        elif tau[3] == 'B' or tau[6] == 'B':
            sck.send("0,1".encode())
            stre = rec(sck)
            tau = move(stre,tau)
            if tau[2] == 'E':
                sck.send("0,2".encode())
                stre = rec(sck)
            else:
                sck.send("1,1".encode())
                stre = rec(sck)
                tau = move(stre,tau)
                if tau[7] == 'E':
                    sck.send("2,1".encode())
                    stre = rec(sck)
                else:
                    sck.send("2,2".encode())
                    stre = rec(sck)
        elif tau[4] != 'B':
            sck.send("1,1".encode())
            stre = rec(sck)
            tau = move(stre,tau)
            if tau[8] == 'E':
                sck.send("2,2".encode())
                stre = rec(sck)
            else:
                if tau[2] == 'E':
                    sck.send("0,2".encode())
                    stre = rec(sck)
                    tau = move(stre,tau)
                    if tau[1] == 'E':
                        sck.send("0,1".encode())
                        stre = rec(sck)
                    else:
                        sck.send("2,0".encode())
                        stre = rec(sck)
                else:
                    sck.send("1,2".encode())
                    stre = rec(sck)
                    tau = move(stre,tau)
                    if tau[3] == 'E':
                        sck.send("1,0".encode())
                        stre = rec(sck)
        else:
            sck.send("0,1".encode())
            stre = rec(sck)
            tau = move(stre,tau)
            if tau[2] == 'E':
                sck.send("0,2".encode())
                stre = rec(sck)
    
    except BrokenPipeError:
        print("dw")

def attack2():
    try:
        sck.connect(("68.183.210.250",32781))

        tau = []

        i = 0
        j = 0
        for i in range(6):
            for j in range(6):
                tau.append('E')

        print(tau)

        pack = sck.recv(256)
            
        stre = pack.decode().replace("\n","n").replace(" ","")

        sck.send("Galahad\n".encode())

        pack = sck.recv(256)
            
        stre = pack.decode()
        print(stre[:-1])

        pack = sck.recv(256)
            
        stre = pack.decode()
        print(stre)

        i = 0
        j = 0

        while True:
            sck.send((str(i) + "," + str(j)).encode())
            j += 1
            if j == 6:
                j = 0
                i += 1
            stre = rec(sck)
            tau = move(stre,tau)
    except BrokenPipeError:
        print("dw")

attack2()
