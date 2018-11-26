import shlex
import time
import os
import errno

from subprocess import Popen, PIPE


class Result:
    pass


def cmd(command):
    result = Result()

    try:
        p = Popen(shlex.split(command), stdin=PIPE, stdout=PIPE, stderr=PIPE)

    except OSError as err:
        result.exit_code = 253    # define as you want
                                  # in my case, 253 is OSError 
                                  # like FileNotFound or something
        result.stderr = err
        return result

    except Exception as err
        result.exit = 254         # same as above
                                  # in my case, 254 is Unknown.
        result.stderr = err
        return result

    (stdout, stderr) = p.communicate()

    result.exit_code = p.returncode
    result.stdout = stdout
    result.stderr = stderr
    result.command = command

    if p.returncode != 0:
        print 'Error executing command [%s]' % command
        print 'stderr: [%s]' % stderr
        print 'stdout: [%s]' % stdout

    return result

