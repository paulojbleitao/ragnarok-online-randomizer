# Ragnarok Online Randomizer

A randomizer for [rAthena](https://github.com/rathena/rathena) servers.

---

### Running

You will need `python` and `pip`.

First install the dependencies with `pip install -r requirements.txt`. Then do `python randomizer.py` after editing `config.json` with your preferred settings.

### Settings

The `config.json` file contains the settings used by the randomizer. Below is the specification of each setting.

```json
// config.json
{
    "rathenaPath": "path/to/rAthena",
    "seed": null,
    "preRe": true,
    "mobs": {
        "levelRange": -1,
        "shuffleMVPs": false
    },
    "drops": {
        "keepCards": false,
        "sameCategory": false
    }
}
```

| Setting | Type | Description |
| ------- | ---- | ----------- |
| rathenaPath | string | The absolute path to your rAthena directory. |
| seed | string, int, float or null | The randomizer's seed; set it as null for a random seed. |
| preRe | boolean | True for pre-renewal servers, false for renewal servers. |
| mobs: levelRange | int | When levelRange is set, a mob will only be replaced by mobs within a certain rage. For example, with a levelRange of 10, a level 40 mob will only be replaced by mobs with levels between 30 and 50.  |
| mobs: shuffleMVPs | boolean | If true, removes MVPs from the general randomization pool and randomizes MVPs only between themselves. For example, a Poring won't be able to be replaced with a Baphomet, but a Baphomet could be replaced by a Valkyrie.  |
| drops: keepCards | boolean | If true, doesn't randomize card drops and doesn't add them to the randomization pool. |
| drops: sameCategory | boolean | If true, keeps the item randomizations to their own categories. For example, equipments will only be replaced by equipments. |
