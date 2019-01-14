#!/usr/bin/env python3

import os
import sys
import argparse
import sqlite3
import json

parser = argparse.ArgumentParser(description='Export IPhone SMS messages to Sailfish OS Commhistory json format')
parser.add_argument('db_path', help='Path to sms.db')
parser.add_argument('output_json', help='Output json')

def exportJSON(db_path, output_json):
    conn = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_COLNAMES)
    conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
    cursor = conn.cursor()

    cursor.execute('SELECT rowid as handle_id, id as `to`, "sms" as type FROM handle')
    handles = []
    for handle in cursor.fetchall():        
        cursor.execute("""SELECT
            strftime('%Y-%m-%dT%H:%M:%fZ', substr(date, 1, 9) + 978307200, 'unixepoch') as `date`,
            case when is_from_me = 0 then "in" else "out" end as direction,
            text
            from message
            where handle_id = ?""",
            (handle['handle_id'],))
        handle['messages'] = cursor.fetchall()
        if len(handle['messages']):
            handles.append(handle)

    with open(output_json, 'w') as outfile:
        json.dump(handles, outfile, indent=4)

if __name__ == '__main__':
    args = parser.parse_args()
    if not os.path.exists(args.db_path):
        print('File does not exist', file=sys.stderr)
        sys.exit(1)
    exportJSON(args.db_path, args.output_json)
