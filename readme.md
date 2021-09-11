![banner](assets/banner.png)

onlinepls is a discord bot that can remotely start, stop and show status of minecraft servers easily, all from discord.

# Features
- start/stop commands
- systemd intergration
- tmux intergration
- status commands
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
mkdir ~/.config/systemd/
mkdir ~/.config/systemd/user

cd ~/.local/share/
git clone https://github.com/daniel071/onlinepls.git; cd onlinepls
mv .env-template .env

# Optional: If you want systemd intergration
mv onlinepls.service ~/.config/systemd/user
systemctl --user enable onlinepls

## systemd commands you can run to manage the service
# systemctl --user start onlinepls
# systemctl --user stop onlinepls
# systemctl --user enable onlinepls
# systemctl --user disable onlinepls
# systemctl --user status onlinepls
```
Now edit the .env file (with an editor of your choice, eg `nano .env`) and fill it in with the information you gathered previously.

### Headless mode: Tmux

**Make sure you installed tmux through your package manager for this to work**

If set to run the server in the background, it will use *tmux*.
Run `tmux a -t mc` in your terminal to access the server at any time.
Press Ctrl and B. Then let go. Then press one of these keys to perform an action
- `%` : Create a split screen horizontally
- `"` : Create a split screen vertically
- `d` : Detach from shell - server will continue to run in the background

Want more info? Have a look at [this guide](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)

## MacOS + Windows
Should work on these operating systems, just make sure to replace the gnome-terminal command in `main.py` with cmd or other equivalent, and add it to your startup apps.

# Troubleshooting
- `Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions` If you got this error, make sure the bot has corrent permissions (it needs embed, send and recieve perms)
- Java cannot find server jar: Make sure that your start script is using an absolute path (e.g. `/home/daniel/Minecraft/start.sh`) instead of a relative path (e.g. `./start.sh`)
-  `gnome-terminal: Unable to init server: Could not connect: Connection refused` Make sure you ran the systemd service as your user (--user)
- `The unit file, source configuration file or drop-ins of onlinepls.service changed on disk.` Run `systemctl --user daemon-reload`
