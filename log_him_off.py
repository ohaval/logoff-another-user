import subprocess
import re
import os
import ctypes
import sys

# The name of the user to log off
USER = ''


def log_off(user):
    output = subprocess.check_output(r"C:\Windows\System32\quser.exe").decode()

    user_line = ''
    for line in output.split('\r\n'):
        if user in line.lower():
            user_line = line
            break

    if not user_line:
        input('User wasn\'t found')
        return None

    userid = re.findall(r'\d', user_line)[0]
    command = f"C:\\Windows\\System32\\logoff.exe {userid}"
    return_code = os.system(command)
    print(return_code)


def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()


def main():
    if is_admin():
        print('[V] Admin Privileges')
        log_off(USER)

    else:
        # Re-run the program with admin rights
        print('[X] Admin Privileges')
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, __file__, None, 1)


if __name__ == '__main__':
    main()
