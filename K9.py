# Inteligent Wordlist Generator
#
# By: K9
# Goblin Wordlist Generator
# Version: 2.0
#
#
##################

import itertools


ban = '''

                                                    '''

print('''\033[91m

     ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
     ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
     ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   
     ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   
     ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   
      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                               		 
                     \033[93mK9  (\033[96mHACKS\033[93m) 
''')
print('''\033[92m

$$\   $$\  $$$$$$\  $$$$$$$$\ $$\   $$\ $$\ 
$$ | $$  |$$  __$$\ \____$$  |$$ |  $$ |\__|
$$ |$$  / $$ /  $$ |    $$  / $$ |  $$ |$$\ 
$$$$$  /  \$$$$$$$ |   $$  /  $$$$$$$$ |$$ |
$$  $$<    \____$$ |  $$  /   \_____$$ |$$ |
$$ |\$$\  $$\   $$ | $$  /          $$ |$$ |
$$ | \$$\ \$$$$$$  |$$  /           $$ |$$ |
\__|  \__| \______/ \__/            \__|\__|
                                            
                                            
                                                
''')


scale = input('\033[36m[!] provide a size scale [eg: "4 to 8" = 4:8] : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[36m[?] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
	first_name = str(input("\n\033[36m[*] First Name: "))
	last_name = str(input("\n\033[36m[*] Last Name: "))
	birthday = str(input("\n\033[36m[*] Birth day: "))
	month = str(input("\n\033[36m[*] Month: "))
	year = str(input("\n\033[36m[*] Year: "))
	chrs = first_name + last_name + birthday + month + year
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[36m[!] Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[36m[?] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
if input('\n\033[36m[?] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
if input('\n\033[36m[?] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()
