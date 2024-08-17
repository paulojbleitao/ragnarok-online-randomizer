import random
import yaml

def randomize_drops(rathena_path, mob_db, item_db, config):
    keep_cards = config['keepCards']
    same_category = config['sameCategory']

    item_dict = { item['AegisName']: item | { 'category': category } for category in item_db for item in item_db[category] }

    mob_list = mob_db['Body']
    every_item = item_db['equip'] + item_db['usable'] + item_db['etc']
    cards = list(filter(lambda item: item['AegisName'].endswith('_Card'), item_db['etc']))
    etc_with_no_cards = list(filter(lambda item: item not in cards, item_db['etc']))
    every_item_but_cards = item_db['equip'] + item_db['usable'] + etc_with_no_cards

    for mob in mob_list:
        if 'Drops' in mob:
            for drop in mob['Drops']:
                suitable_items = every_item
                item_category = item_dict[drop['Item']]['category']
                if keep_cards and drop['Item'].endswith('_Card'):
                    continue
                if same_category and keep_cards and item_category == 'etc':
                    suitable_items = etc_with_no_cards
                elif same_category:
                    suitable_items = item_db[item_category]
                elif keep_cards:
                    suitable_items = every_item_but_cards
                drop['Item'] = random.choice(suitable_items)['AegisName']
    mob_db['Body'] = mob_list
    mob_db_file = open(f'{rathena_path}/db/pre-re/mob_db.yml', 'w')
    print(yaml.dump(mob_db, Dumper=yaml.CDumper), file=mob_db_file)
    mob_db_file.close()
