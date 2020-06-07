import checkers
from pullers.pastebin import Pastebin
from time import time, sleep
import json
import database.postgres as pg


pg = pg.PgConn()

while True:
    records = None
    start_time = time()
    pb = Pastebin()
    records = pb.scrape_records(100)
    for r in records:
        new_record = pg.check_for_record(r['key'])
        print("checking record {}".format(r['key']))
        if new_record:
            raw_data = pb.scrape_raw_data(r['scrape_url'])
            rule = checkers.process_rules(raw_data)
            if rule:
                pg.insert_record(r['key'], rule, json.dumps(r))

    pg.close_conn()

    end_time = time()
    elapsed_time = end_time - start_time

    if elapsed_time <= 60:
        sleep(int(round(60 - elapsed_time)))
