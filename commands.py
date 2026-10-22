from main_page import command
import webbrowser as web
import os, msvcrt, time


def def_command():
    # ========= Sites =========
    if command == "youtube":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.youtube.com/")
        
    elif command == "web telegram":
        print(f"                                                                || open {command}.. ||")
        web.open("https://web.telegram.org/")
        
    elif command == "github":
        print(f"                                                                || open {command}.. ||")
        web.open("https://github.com/")
        
    elif command == "chatgpt":
        print(f"                                                                || open {command}.. ||")
        web.open("https://chatgpt.com/")
        
    elif command == "claude":
        print(f"                                                                || open {command}.. ||")
        web.open("https://claude.com/")
        
    elif command == "typerun":
        print(f"                                                                || open {command}.. ||")
        web.open("https://typerun.top/#eng_basic")
        
    elif command == "gmail":
        print(f"                                                                || open {command}.. ||")
        web.open("https://mail.google.com/")
        
    elif command == "virus total":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.virustotal.com/")
        
    elif command == "virustotal":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.virustotal.com/")
        
    elif command == "google":
        print(f"                                                                || open {command}.. ||")
        web.open("http://www.google.com/")
        
    elif command == "twitch":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.twitch.tv/")
        
    elif command == "kick":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.kick.com")
        
    elif command == "python":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.python.org")
        
    elif command == "jetbrains":
        print(f"                                                                || open {command}.. ||")
        web.open("https://www.jetbrains.com/")
        
    elif command == "web spotify":
        print(f"                                                                || open {command}.. ||")
        web.open("http://open.spotify.com/")
        
    elif command == "web soundcloud":
        print(f"                                                                || open {command}.. ||")
        web.open("https://soundcloud.com/")
        
    
    # ========= Apps =========
    elif command == "notepad":
        print(f"                                                                || open {command}.. ||")
        os.system("notepad.exe")
        
    elif command == "pycharm":
        print(f"                                                                || open {command}.. ||")
        os.system("start pycharm")
        
    elif command == "code":
        print(f"                                                                || open {command}.. ||")
        os.system("start code")
        
    elif command == "cmd":
        print(f"                                                                || open {command}.. ||")
        os.system("start cmd")
        
    elif command == "explorer":
        print(f"                                                                || open {command}.. ||")
        os.system("start explorer")
        
    elif command == "calculator":
        print(f"                                                                || open {command}.. ||")
        os.system("start calc")
        
    elif command == "calc":
        print(f"                                                                || open {command}.. ||")
        os.system("start calc")
        
    elif command == "chrome":
        print(f"                                                                || open {command}.. ||")
        os.system("start chrome")
        
    elif command == "discord":
        print(f"                                                                || open {command}.. ||")
        os.system("start discord:")
        
    elif command == "ds":
        print(f"                                                                || open {command}.. ||")
        os.system("start discord:")
        
    elif command == "telegram":
        print(f"                                                                || open {command}.. ||")
        os.system("start tg:")
        
    elif command == "tg":
        print(f"                                                                || open {command}.. ||")
        os.system("start tg:")
        
    elif command == "steam":
        print(f"                                                                || open {command}.. ||")
        os.system("start steam:")
        
    elif command == "visual studio":  
        print(f"                                                                || open {command}.. ||")
        os.system("start devenv")
        
    elif command == "vs":            
        print(f"                                                                || open {command}.. ||")
        os.system("start devenv")
        
    elif command == "vs code":  
        print(f"                                                                || open {command}.. ||")
        os.system("start code")
        
    elif command == "spotify":
        print(f"                                                                || open {command}.. ||")
        os.system("start spotify")
            
            
            
    # ========= help =========
    elif command == "help":
        print('\nTo open an app or website using a command, \nsimply enter its name. If you want to \nfind out the commands, type "commands".')
        print("                                                                || Press any key to close. ||")
        msvcrt.getch()

        
    # -------- commands ---------
    elif command == "commands":
        print("Here are all the existing commands.\n")
        print("help\ncommands\nlanguage\nadd an app\nadd a site\nyoutube\nweb telegram\ngithub\nchatgpt\nclaude\ntyperun\ngmail\nvirus total\ngoogle\ntwitch\nkick\npython\njetbrains\nweb spotify\nweb soundcloud\nnotepad\npycharm\ncode\ncmd\nexplorer\ncalculator\nchrome\ndiscord\ntelegram\nsteam\nvisual studio\nspotify\n")
        print("                                                                || Press any key to close. ||")
        msvcrt.getch()
        
    # ========= exit ========
    elif command == "exit":
        print("                                                                [!] exit...")
        time.sleep(1)
        exit
        
    elif command == "stop":
        print("                                                                [!] stop...")
        time.sleep(1)
        exit
        
        
    else:
        print("                                                                [!] unknown command..")
        print("                                                                || Press any key to close. ||")
        msvcrt.getch()