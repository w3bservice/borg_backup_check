#!/usr/bin/python
import json
import datetime
from subprocess import Popen,PIPE
import sys


def get_json(borgpath=None):
    borg = Popen(["sudo","/usr/local/bin/borg", "info", borgpath, "--json", "--last", "1"], stdout=PIPE, stderr=PIPE)
    output, err = borg.communicate()
    if err:
        print(err)
        sys.exit(1)
    return json.loads(output)


def get_mertics(path):
    data = get_json(path)
    now = datetime.datetime.now()
    backupdate = datetime.datetime.strptime(data['archives'][0]['end'],"%Y-%m-%dT%H:%M:%S.%f")
    diff = now - backupdate
    if not diff > datetime.timedelta(1):
        print (data['archives'][0]['duration'])
    else:
        print (0)


if __name__ == "__main__":
    path = sys.argv[1]
    get_mertics(path)