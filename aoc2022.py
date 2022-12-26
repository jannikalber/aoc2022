import sys
import datetime
import os

if __name__ == "__main__":
	script = None
	
	if len(sys.argv) == 2:
		if os.path.exists(f"day{sys.argv[1]}.py"):
			script = f"day{sys.argv[1]}"
	else:
		day = datetime.datetime.now().day
		if os.path.exists(f"day{day}b.py"):
			script = f"day{day}b"
		elif os.path.exists(f"day{day}a.py"):
			script = f"day{day}a"
	
	if script is not None:
		print(f"\033[1m\033[36m*** Running {script}... ***\033[0m\n")
		start = datetime.datetime.now()
		__import__(script)
		diff = datetime.datetime.now() - start
		print(f"\n\033[1m\033[92m*** Took {diff} ***\033[0m")
	else:
		print("\033[1m\033[91m*** No script found to be run ***\033[0m", file=sys.stderr)
