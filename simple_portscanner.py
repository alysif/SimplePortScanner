import argparse
import time
import socket
from colorama import Fore, init

init()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--targetip", help="Target IP", required=True)
parser = vars(parser.parse_args())

def main():
    startTime = time.time()
    t_IP = socket.gethostbyname(parser['targetip'])
    print("[{}+{}] {}TARGET{}: {}{} {}".format(Fore.GREEN, Fore.WHITE, Fore.CYAN, Fore.YELLOW, Fore.GREEN, t_IP, Fore.WHITE))
    print("[{}+{}] {}STARTING SCAN IN HOST{}".format(Fore.GREEN, Fore.WHITE, Fore.RED, Fore.WHITE))
    for i in range(50, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.01)
        conn = s.connect_ex((t_IP, i))
        if(conn == 0):
            print("[{}+{}] {}PORT OPEN IN{}: {}{}:{}{}{}{}".format(Fore.GREEN, Fore.WHITE, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, t_IP, Fore.YELLOW, Fore.CYAN, str(i), Fore.WHITE))
        else:
            pass
            #print("[{}+{}] {}PORT CLOSE IN{}: {}{}:{}{}{}{}".format(Fore.GREEN, Fore.WHITE, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, t_IP, Fore.YELLOW, Fore.CYAN, str(i), Fore.WHITE))
        s.close()
    print("[{}+{}] {}TIME TAKEN{}: {}{}{}".format(Fore.GREEN, Fore.WHITE, Fore.RED, Fore.YELLOW, Fore.CYAN, time.time() - startTime, Fore.WHITE))
if __name__ == "__main__":
    main()