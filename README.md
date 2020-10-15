# †hê Ɽǟɢǟռօʀӄɮð†
This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners....

This is the one and only official Raganrok Userbot made by [@HELLBOY_OP](https://t.me/HELLBOY_OP) Also join support channel and group :- https://t.me/Raganrok_Official Enjoy Your Bot!!💝


# The owner would not be responsible for any kind of bans due to the bot...


# For any query:-
### [Join Here For Any Query](https://t.me/Raganrok_official)

# FORK AT YOUR OWN RISK
## Installing

### The Easy Way

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Hellboy-Aaryan/Raganrok/)

Just click on the above button which will direct you to the deployment page of heroku..where you have to fill some required credentials..video tutorial will be released soon...

# Generate String Session From Below Links:-

### [String #1](https://Hellbot.hellboyop.repl.run)

### [String #2](https://Hellbot2.hellboyop.repl.run)

### Inspired by team #Cobra (Dark Cobra userbot..❤)

## Credits

1. [Dark Cobra](https://github.com/DARK-COBRA/DARKCOBRA/)
2. Uniborg
3. Friday
4. Cat userbot
5. Telebot
6. Paper plane userbot

Credit of the plugins goes to their respective owner

Once again aren't responsible for any account bans...!!

## Use on your own risk

## The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/HellBoy-Aaryan/Raganrok
cd Raganrok
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
