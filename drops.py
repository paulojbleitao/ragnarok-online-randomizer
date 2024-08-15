import random
import yaml

def randomize_drops(rathena_path, mob_db, item_db):
    mob_list = mob_db['Body']
    every_item = item_db['equip'] + item_db['etc'] + item_db['usable']
    for mob in mob_list:
        if 'Drops' in mob:
            for drop in mob['Drops']:
                drop['Item'] = random.choice(every_item)['AegisName']
    mob_db['Body'] = mob_list
    mob_db_file = open(f'{rathena_path}/db/pre-re/mob_db.yml', 'w')
    print(yaml.dump(mob_db, Dumper=yaml.CDumper), file=mob_db_file)
    mob_db_file.close()
