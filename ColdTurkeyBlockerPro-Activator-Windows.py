'''
** For Windows Systems Only **.
>> TO ACTIVATE THE COLD TURKEY BLOCKER RUN THIS PYTHON FILE AS FOLLOWS:

1. Move the file to "C:/ProgramData/Cold Turkey"
2. Open Terminal, cd to the folder and run "python3 ColdTurkeyBlocker-Pro.py"
3. Close Cold Turkey, Reopen it and Enjoy! (If it Doesn't Work Restart your PC and Enjoy!!!)
'''

import json
import sqlite3
import os

DB_PATH = "C:/ProgramData/Cold Turkey/data-app.db"


def activate():

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        s = c.execute("SELECT value FROM settings WHERE key = 'settings'").fetchone()[0]
        dat = json.loads(s)

        if dat["additional"]["proStatus"] != "pro":
            dat["additional"]["proStatus"] = "pro"
            print("You are now a Cold Turkey Pro user.\nPlease close Cold Turkey Blocker and run again it.")
            c.execute("""UPDATE settings SET value = ? WHERE "key" = 'settings'""", (json.dumps(dat),))
            conn.commit()

        else:
            print("Looks like your copy of Cold Turkey Blocker is already activated.")
            print("Deactivating it")
