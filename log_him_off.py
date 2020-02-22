import subprocess
import re
import os
import ctypes
import sys

# Enter here the name of the user you want to log off. (Lower)
USER = ""


def log_off(username = USER):
	"""Logging off the user by the name of the USER variable."""
	output = str(subprocess.check_output(r"C:\Windows\Sysnative\quser.exe")).split("\\r\\n")

	for line in output:
		if username in line.lower():
			user_line = line

	userid = re.findall(r"\d", user_line)[0]

	os.system(f"C:\\Windows\\Sysnative\\logoff.exe {userid}")


def is_admin():
	"""Tries to run the program with admin permissions. Should pop a UAC windows in most PC's preferences."""
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except Exception as e:
		return False


def main():
	if is_admin():
		if not USER:
			USER = input("Enter username ->")
		log_off(USER)

	else:
		# Re-run the program with admin rights
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


if __name__ == "__main__":
	main()