# from emailSpoofDetection import emailSpoofDetection
# import sys
# from termcolor import cprint, colored

    
# try:
#     file_path=sys.argv[1]

#     emailDomain = input(colored('enter the email domain: ', 'yellow'))
#     with open(file_path, 'r') as header:
#         analysis = emailSpoofDetection(header, emailDomain)
#         if analysis:
#             print(' ')
#             cprint('No spoofing detected!', 'yellow')
#         else:
#             print(' ')
#             cprint('email spoofing detected!', 'red')

# except FileNotFoundError:
#     print(' ')
#     cprint("file not found...", 'red')
# except IndexError:
#     print(' ')
#     cprint('wrong parameters...', 'red')
# except KeyboardInterrupt:
#     print(' ')



import sys

def email_spoof_detection(file_path, email_domain):
    with open(file_path, 'r') as header:
        header_content = header.read()
        if email_domain in header_content:
            print(' ')
            print('Подделок не обнаружено!')
        else:
            print(' ')
            print('Обнаружена подделка электронной почты!')

if len(sys.argv) != 3:
    print(' ')
    print('Использование: python spoof.py <путь_к_файлу> <домен_электронной_почты>')
    sys.exit(1)

file_path = sys.argv[1]
email_domain = sys.argv[2]

email_spoof_detection(file_path, email_domain)
