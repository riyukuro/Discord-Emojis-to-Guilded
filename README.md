# Discord-Emojis-to-Guilded
Easily move discord emojis to guilded.gg.

## Installation
Requires [Python 3](https://www.python.org/).

After python is installed, clone the repository or download the [ZIP](https://github.com/riyukuro/Discord-Emojis-to-Guilded/archive/refs/heads/main.zip) and then extract.
- Note: You may need to run `pip install requests` if you you are using a fresh install of python or if havent used it in another project before.

## Usage
1. Navigate to the directory where you downloaded the files through command prompt or powershell (Terminal on Mac/Linux) (ex. `cd C:\users\xxxx\downloads\Discord-Emojis-to-Guilded-main` or `Shift+Right Click` inside of the folder and click `open command window here`) and type `python discord-emoji-converter.py` or `python3 discord-emoji-converter.py` in command prompt or terminal.
2. Enter your discord token.

To get your Discord Token: **(Note: DO NOT SHARE YOUR TOKEN WITH ANYONE)**
-  Open the Discord desktop app or login on the Discord website here
-  Open the Chrome Dev Tools with the keyboard shortcut (F12 or Ctrl + Shift + I)
-  Go to the Network tab
-  Click the XHR button to filter to XHR requests only
-  Do any action in Discord like opening a channel
-  Click the science request that shows up in the list
-  Go to the Headers tab
-  Find authorization under Request Headers and copy your token (make sure you copy the entire token and don't copy any spaces)

3. Enter the Discord Server ID(s). 
- To get this: Type `?` or right click the server icon of the server you want to take the emotes from and click `Copy ID`.
- For multiple servers at once seperate them by a comma. (ex. `779528208566845440, 779415495106494484, 779113451456692246`)

4. Enter a name. (This will be the file name and otherwise doesn't matter)

Note: If there are more than 50 emotes on the server the file will be split into parts.

## To Use the Emote Pack
1. Upload the .json files somewhere. (Pastebin or copy the .json files to a discord server, right click the file, and copy link)
2. Open the emotes page on your Guilded.gg server.
3. Click `import an external emote pack`
4. Paste the url to the .json file.
