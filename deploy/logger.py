# Colors from blender build scripts
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def err(e):
  print(bcolors.WARNING + e + bcolors.ENDC)

def info(i):
  print(bcolors.OKBLUE + i + bcolors.ENDC)

def success(i):
  print(bcolors.OKGREEN + i + bcolors.ENDC)
