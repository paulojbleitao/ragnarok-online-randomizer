import random
from util import navigate_directories
from pathlib import Path

def is_mvp(mob_entry):
    return 'MvpExp' in mob_entry and mob_entry['MvpExp'] > 0

def randomize_mob_file(filepath, mob_list, filtered_mob_list, config):
    level_range = config['levelRange']
    # maybe find a better name for this? shuffleMVPs means that MVPs will only be randomized between MVPs
    shuffle_mvps = config['shuffleMVPs']

    file = open(filepath)
    new_file = []
    for line in file:
        new_line = line.split('\t')
        # ignore comment lines, blank lines
        if line.startswith('//') or line == '\n': continue
        # make sure to keep script lines
        if not 'monster' in line or len(new_line) != 4: new_file.append(line); continue

        suitable_mobs = filtered_mob_list

        mob_id = int(new_line[3].split(',')[0])
        mob_entry = next(filter(lambda mob: mob['Id'] == mob_id, mob_list))
        if level_range >= 0:
            mob_level = mob_entry['Level']
            suitable_mobs = list(filter(lambda mob: mob_level - level_range <= mob['Level'] <= mob_level + level_range, suitable_mobs))
        if shuffle_mvps and is_mvp(mob_entry):
            # cursed: for now, if an MVP is not available in the specified level range,
            # choose between any MVPs that haven't been picked yet
            temp_suitable_mobs = list(filter(is_mvp, suitable_mobs))
            if len(temp_suitable_mobs) == 0: temp_suitable_mobs = list(filter(is_mvp, filtered_mob_list))
            suitable_mobs = temp_suitable_mobs
        elif shuffle_mvps and not is_mvp(mob_entry):
            suitable_mobs = list(filter(lambda mob: not is_mvp(mob), suitable_mobs))

        random_mob = random.choice(suitable_mobs)
        if shuffle_mvps and is_mvp(mob_entry):
            filtered_mob_list.remove(random_mob) # should guarantee every mvp is available

        new_line[2] = random_mob['Name']
        id_part = new_line[3].split(',')
        id_part[0] = str(random_mob['Id'])
        new_line[3] = ','.join(id_part)
        new_file.append('\t'.join(new_line))
    file.close()

    file = open(filepath, 'w')
    for line in new_file:
        print(line, end='', file=file)
    file.close()

def randomize_mobs(rathena_path, mob_db, config):
    mob_list = mob_db['Body']
    filtered_mob_list = list(filter(lambda mob: 'BaseExp' in mob and 'Drops' in mob, mob_list))
    mob_files = navigate_directories(Path(f'{rathena_path}/npc/pre-re/mobs/'), [])
    for file in mob_files:
        randomize_mob_file(file, mob_list, filtered_mob_list, config)
