import random
import yaml

def randomize_drops(rathena_path, mob_db, item_db, config):
    keep_cards = config['keepCards']

    mob_list = mob_db['Body']
    every_item = item_db['equip'] + item_db['usable'] + item_db['etc']
    cards = list(filter(lambda item: item['AegisName'].endswith('_Card'), item_db['etc']))
    every_item_but_cards = item_db['equip'] + item_db['usable'] + list(filter(lambda item: item not in cards, item_db['etc']))

    for mob in mob_list:
        if 'Drops' in mob:
            for drop in mob['Drops']:
                if keep_cards and drop['Item'].endswith('_Card'): continue
                elif keep_cards: drop['Item'] = random.choice(every_item_but_cards)['AegisName']
                else: drop['Item'] = random.choice(every_item)['AegisName']
    mob_db['Body'] = mob_list
    mob_db_file = open(f'{rathena_path}/db/pre-re/mob_db.yml', 'w')
    print(yaml.dump(mob_db, Dumper=yaml.CDumper), file=mob_db_file)
    mob_db_file.close()
