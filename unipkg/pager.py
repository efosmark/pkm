import subprocess
from typing import Optional, Callable

CMD_PAGER = ['/usr/bin/less', '--chop-long-lines', '--RAW-CONTROL-CHARS', '--use-color', '--quit-at-eof', '--quit-if-one-screen',  '--redraw-on-quit ', '--tilde', '-c']

def paged_subprocess(*args, modify_line:Optional[Callable[[str],str]]=None):
    p1 = subprocess.Popen(*args, stdout=subprocess.PIPE, text=True)
    p2 = subprocess.Popen(CMD_PAGER, stdin=subprocess.PIPE, text=True)
    if p1.stdout is not None and p2.stdin is not None:
        for line in p1.stdout:
            if modify_line is not None:
                line = modify_line(line)
            p2.stdin.write(line)
            p2.stdin.flush()
        p1.stdout.close()
        p2.stdin.close()
    return p2