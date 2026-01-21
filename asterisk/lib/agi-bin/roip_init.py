#!/usr/bin/env python3
import sys
import time
import uuid

def agi_read():
    env = {}
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        key, val = line.split(":", 1)
        env[key.strip()] = val.strip()
    return env
def agi_set(var, val):
    sys.stdout.write(f'SET VARIABLE {var} "{val}"\n')
    sys.stdout.flush()
    sys.stdin.readline()

if __name__=="__main__":
    # Retorna Ambiente AGI
    env = agi_read()

    # Retorna Parametro do grupo
    group = sys.argv[1] if len(sys.argv) > 1 else "00"

    # Identificadores
    user = env.get("agi_callerid", "unkown")
    channel = env.get("agi_channel", "unkown")
    session_id = str(uuid.uuid4())
    start_ts = str(int(time.time()))

    # Settando variaveis no canal
    agi_sett("SESSION_ID", session_id)
    agi_sett("ROIP_GROUP", group)
    agi_sett("ROIP_USER", user)
    agi_sett("ROIP_START_TS", start_ts)
    agi_sett("ROIP_CHAN", channel)

    # Log basico
    agi_verbose(f"ROIP INIT | session={session_id} user={user} group={group}", 2)

    sys.exit(0)
