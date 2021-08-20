![banner](assets/banner.png)

onlinepls is a discord bot that can remotely start, stop and show status of minecraft servers easily, all from discord.

# Features
- start/stop commands
- systemd intergration
- (coming soon) status commands
- (coming soon) easy installation

# Installation
1. Follow the guide [here](https://discordpy.readthedocs.io/en/stable/discord.html) to create a discord bot account. Make sure to get the token of the bot.
2. Make sure your server start script is using an absolute path (e.g. `/home/daniel/Minecraft/start.sh`) instead of a relative path (e.g. `./start.sh`)
3. Edit your `server.properties` file. Set `enable-rcon=true` to true and `rcon.password=` to a password of your choice
4. Enable developer mode in discord (go to user settings > advanced > developer mode)
5. Then, right click on a user you wish to be an admin and click 'Copy ID'


## Linux
Automated installation script coming soon ™

**Manual install**
```sh
# Main files
sudo su
cd /etc/
git clone https://github.com/daniel071/onlinepls.git; cd onlinepls
mv .env-template .env

# Optional: If you want systemd intergration
mv onlinepls.service /lib/systemd/system/onlinepls.service
systemctl daemon-reload
systemctl enable onlinepls

## systemd commands you can run to manage the service
# systemctl start onlinepls
# systemctl stop onlinepls
# systemctl enable onlinepls
# systemctl disable onlinepls
```
Now edit the .env file (with an editor of your choice, eg `nano .env`) and fill it in with the information you gathered previously.

## MacOS + Windows
Should work on these operating systems, just make sure to replace the gnome-terminal command in `main.py` with cmd or other equivalent, and add it to your startup apps.

# Troubleshooting
- `Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions` If you got this error, make sure the bot has corrent permissions (it needs embed, send and recieve perms)
- Java cannot find server jar: Make sure that your start script is using an absolute path (e.g. `/home/daniel/Minecraft/start.sh`) instead of a relative path (e.g. `./start.sh`)
