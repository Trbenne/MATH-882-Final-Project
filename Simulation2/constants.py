
# Action types / Attacker msgs
AMSG_SCAN = 0
AMSG_EXPLORE = 1
AMSG_INSPECT = 2
AMSG_SEND = 3
AMSG_FOCUSNEXT = 4
AMSG_FOCUSPREV = 5

# Server replies / Server msgs
NONE = 0
# SMSG_INVALID = 1
OPENPORT = 1
SMSG_FILELIST = 2
SMSG_FILEEDGES = 3
SMSG_VULNLIST = 4
SMSG_FLAG = 5
SMSG_FILEFOCUS = 6

# Action list
AMSG_TYPES = [AMSG_SCAN,AMSG_EXPLORE,AMSG_INSPECT,AMSG_SEND,AMSG_FOCUSNEXT,AMSG_FOCUSPREV]
N_AMSG = len(AMSG_TYPES)


# Files
N_VISIBLEFILES = 4
N_HIDDENFILES = 2

STRING_VISIBLEFILES = ['index.html', 'submit.js', 'form.php', 'index2.html', 'pay.js', 'about.php', 'login.js', 'users.db']
STRING_HIDDENFILES = ['robots.txt', '.passd']
STRING_ALLFILES = STRING_VISIBLEFILES + STRING_HIDDENFILES

# Vulnerable params
N_VULNPARAMS = 4
VULN_UNKOWN = 0
VULN_OPEN = 1
VULN_CLOSED = 2

VISIB_PUBLIC = 0
VISIB_HIDDEN = 1

STATE_FILEVISIBILITY = 0
STATE_FILETYPE = 1
STATE_NLINKS = 2
STATE_EXPLORED = 3
STATE_VULNPARAM1 = 4
STATE_VULNPARAM2 = 5
STATE_VULNPARAM3 = 6
STATE_VULNPARAM4 = 7

ACTION_SCAN = 0
ACTION_EXPLORE = 1
ACTION_INSPECT = 2
ACTION_SEND_PARAM1 = 3
ACTION_SEND_PARAM2 = 4
ACTION_SEND_PARAM3 = 5
ACTION_SEND_PARAM4 = 6
ACTION_FOCUS_NEXT = 7
ACTION_FOCUS_PREV = 8

# 
N_STATES = 8
N_ACTIONS = 9
