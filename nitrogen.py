import os, pyfiglet, string, numpy, requests
from pystyle import Colors, Write
from time import sleep

class NitroGen():
    def __init__(self):
        pass
        
    def title(self, content):
        try:
            os.system(f"title {content}")
        except:
            pass

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
            
    def updateScreen(self, valid, invalid):
        self.clear()
        Write.Print(pyfiglet.figlet_format('k e n z o'), Colors.green_to_white, interval=0)
        Write.Print(f'Valid : {valid} | Invalid : {invalid}', Colors.green_to_white, interval= 0)

    #checks if nitro link is valid or not.
    valid = 0
    invalid = 0
    valid = []
    def checker(self, nitro:str):
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)
        if response.status_code == 200:
            self.valid += 1
            self.valid.append()
        else:
            self.invalid += 1
        self.updateScreen(self.valid, self.invalid)

    #generates nitro link
    def generate(self, num):
        chars = []
        chars[:0] = string.ascii_letters + string.digits
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"
                self.checker(url)
            except:
                pass

    def exit(self):
        sleep(2)
        for c in reversed(range(1, 4)):
            self.clear()
            Write.Print(f'[!] Exiting in {c}', Colors.green_to_white)
            sleep(1)
        exit()


    def main(self):
        self.title('[Nitro Generator] Made by kxnzx - Ver 1.0')
        Write.Print('Loading...', Colors.green_to_white, interval=0.0001)
        sleep(1)
        self.clear()
        Write.Print(pyfiglet.figlet_format('k x n z x', font="gothic__"), Colors.green_to_white, interval=0)
        Write.Print('Made by: knxzx#7093', Colors.green_to_white, interval=0.0001)
        print('')
        try:
            num = Write.Input("[?] Amount > ", Colors.green_to_white)
            num = int(num)    
        except:
            Write.Print('[!] Input needs to be a number. Exiting...', Colors.green_to_white)
            exit()
        self.generate(num)
        Write.Print(f"Results:", Colors.green_to_white)
        Write.Print(f"\nValid: {len(self.valid)}", Colors.green_to_white)
        Write.Print(f"\nInvalid: {self.invalid}", Colors.green_to_white)
        Write.Print(f"\nValid Codes: {', '.join(self.valid)}", Colors.green_to_white)
        print('')
        Write.Input("The end! Press Enter 5 times to close the program.", Colors.green_to_white)
        [input(i) for i in range(5, 1, -1)]
        self.exit()

mainapp = NitroGen()
mainapp.main()