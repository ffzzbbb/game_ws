import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wlc/game_ws/src/xiao_wang/install/xiao_wang'
