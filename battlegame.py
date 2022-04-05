#characters
wizard = "Sir Bastion the Wizard"
elf = "Gantar the Wood Elf"
human = "Philip of Stover Human"
orc = "Snotlout the Orc from Hibernia"
dwarf = "Thorin the problem child `Dwarf"
#character hp
wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300
orc_hp = 250
dwarf_hp = 242
#character damage
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 140
orc_damage = 75 * 2 
dwarf_damage = 150

## dragon is just for fun can be found at https://ascii.co.uk/art/dragon  ###
while True:
    print("                                        ____________ ")
    print("                             (`-..________....---''\ ____..._.-`")
    print("                              \\`._______.._,.---'''     ,' ")
    print("                              ; )`.      __..-'`-.      / ")
    print("                             / /     _.-' _,.;;._ `-._,'")
    print("                            / /   ,-' _.-'  //   ``--._``._")
    print("                          ,','_.-' ,-' _.- (( =-    -. `-._`-._____")
    print("                        ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.")
    print("                    |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.")
    print("  _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._")
    print(",',)---' /|)          `     `      ``-.   `     /     /     `     `-.")
    print("\_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.")
    print("\_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )")
    print("           `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__")
    print("                   ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   ")
    print("                                                      ``--------..._``--.__")
    print(" #############################################################################")
    print(" #############################################################################")
    print(" ##      Welcome Mortal select a character below to challenge me with       ##")
    print(" ## 1) Sir Bastion the Wizard                 HP:70 ATK:150                 ##")
    print(" ## 2) Gantar the Wood Elf                    HP:100 ATK:100                ##")
    print(" ## 3) Philip of Stover Human                 HP:150 ATK:20                 ##")
    print(" ## 4) Snotlout the Orc from Hibernia         HP:250 ATK:75 *2              ##")
    print(" ## 5) Thorin the Probelm child Dwarf         HP:205 ATK:150                ##")
    print(" ##         Press 6 to show your cowardice and leave my cave                ##")
    print(" #############################################################################")
    print(" #############################################################################")
   # chooseing characters
    character = input("Choose your character:")
    if character == "1":    
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character =="3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif character == "5":
        character = dwarf
        my_hp = dwarf_hp
        my_damage = dwarf_damage
        break
    elif character == "6":
        print("Your cowardice is now known return when you are ready to shed your mortal shell ")
        quit() 
    
    else:
        print ("Unknown Character")
#combat
print("You have chosen the character: "+ character)
print ("Your Health is " , my_hp)
print ("Your damage is" , my_damage)
print ("Dragon health is", dragon_hp)
#end game senario
while True:
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage
    print("The", character, "damaged the Dragon!")
    print ("The dragons hp is", dragon_hp)
    if dragon_hp <= 0:
        print("The dragon has lost the battle!")
        print("YYYYYYY       YYYYYYY                                     WWWWWWWW                           WWWWWWWW iiii    ")               
        print("Y:::::Y       Y:::::Y                                     W::::::W                           W::::::Wi::::i   ")               
        print("Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W iiii       ")             
        print("Y::::::Y     Y::::::Y                                     W::::::W                           W::::::W              ")          
        print ("YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::Wiiiiiiinnnn  nnnnnnnn ")   
        print("    Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::W i:::::in:::nn::::::::nn  ")
        print("    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::W   i::::in::::::::::::::nn ")
        print("     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W    i::::inn:::::::::::::::n")
        print( "     Y:::::::Y   o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W     i::::i  n:::::nnnn:::::n")
        print("       Y:::::Y    o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W      i::::i  n::::n    n::::n ")
        print("       Y:::::Y    o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W       i::::i  n::::n    n::::n")
        print("       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W        i::::i  n::::n    n::::n ")
        print("       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W        i::::::i n::::n    n::::n")
        print("    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W         i::::::i n::::n    n::::n ")
        print("    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W          i::::::i n::::n    n::::n ")
        print("    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW           iiiiiiii nnnnnn    nnnnnn")
        break
    print ("The dragon strikes", character)
    print("Your hp is", my_hp)
    if my_hp <= 0:
        print("Dragon kills", character)
        print("DDDDDDDDDDDDD                                                                                                     WWWWWWWW                           WWWWWWWW iiii                                    ")
        print("D::::::::::::DDD                                                                                                  W::::::W                           W::::::Wi::::i                                   ")
        print("D:::::::::::::::DD                                                                                                W::::::W                           W::::::W iiii                                    ")
        print("DDD:::::DDDDD:::::D                                                                                               W::::::W                           W::::::W                                         ")
        print("D:::::D    D:::::D rrrrr   rrrrrrrrr   aaaaaaaaaaaaa     ggggggggg   ggggg   ooooooooooo   nnnn  nnnnnnnn          W:::::W           WWWWW           W:::::Wiiiiiiinnnn  nnnnnnnn        ssssssssss      ")
        print("D:::::D     D:::::Dr::::rrr:::::::::r  a::::::::::::a   g:::::::::ggg::::g oo:::::::::::oo n:::nn::::::::nn          W:::::W         W:::::W         W:::::W i:::::in:::nn::::::::nn    ss::::::::::s  ")
        print("D:::::D     D:::::Dr:::::::::::::::::r aaaaaaaaa:::::a g:::::::::::::::::go:::::::::::::::on::::::::::::::nn         W:::::W       W:::::::W       W:::::W   i::::in::::::::::::::nn ss:::::::::::::s ")
        print("D:::::D     D:::::Drr::::::rrrrr::::::r         a::::ag::::::ggggg::::::ggo:::::ooooo:::::onn:::::::::::::::n         W:::::W     W:::::::::W     W:::::W    i::::inn:::::::::::::::ns::::::ssss:::::s")
        print("D:::::D     D:::::D r:::::r     r:::::r  aaaaaaa:::::ag:::::g     g:::::g o::::o     o::::o  n:::::nnnn:::::n          W:::::W   W:::::W:::::W   W:::::W     i::::i  n:::::nnnn:::::n s:::::s  ssssss ")
        print("D:::::D     D:::::D r:::::r     rrrrrrraa::::::::::::ag:::::g     g:::::g o::::o     o::::o  n::::n    n::::n           W:::::W W:::::W W:::::W W:::::W      i::::i  n::::n    n::::n   s::::::s      ")
        print("D:::::D     D:::::D r:::::r           a::::aaaa::::::ag:::::g     g:::::g o::::o     o::::o  n::::n    n::::n            W:::::W:::::W   W:::::W:::::W       i::::i  n::::n    n::::n      s::::::s   ")
        print("D:::::D    D:::::D  r:::::r          a::::a    a:::::ag::::::g    g:::::g o::::o     o::::o  n::::n    n::::n             W:::::::::W     W:::::::::W        i::::i  n::::n    n::::nssssss   s:::::s ")
        print("DDD:::::DDDDD:::::D r:::::r          a::::a    a:::::ag:::::::ggggg:::::g o:::::ooooo:::::o  n::::n    n::::n              W:::::::W       W:::::::W        i::::::i n::::n    n::::ns:::::ssss::::::s")
        print("D:::::::::::::::DD  r:::::r          a:::::aaaa::::::a g::::::::::::::::g o:::::::::::::::o  n::::n    n::::n               W:::::W         W:::::W         i::::::i n::::n    n::::ns::::::::::::::s ")
        print("D::::::::::::DDD    r:::::r           a::::::::::aa:::a gg::::::::::::::g  oo:::::::::::oo   n::::n    n::::n                W:::W           W:::W          i::::::i n::::n    n::::n s:::::::::::ss  ")
        print("DDDDDDDDDDDDD       rrrrrrr            aaaaaaaaaa  aaaa   gggggggg::::::g    ooooooooooo     nnnnnn    nnnnnn                 WWW             WWW           iiiiiiii nnnnnn    nnnnnn  sssssssssss    ")
        print("                                                                  g:::::g                                                                                                                             ")
        print("                                                      gggggg      g:::::g                                                                                                                             ")
        print("                                                      g:::::gg   gg:::::g                                                                                                                             ")
        print("                                                      g::::::ggg:::::::g                                                                                                                             ")
        print("                                                        gg:::::::::::::g                                                                                                                              ")
        print("                                                           ggg::::::ggg                                                                                                                                ")
        print("                                                             gggggg                                                                                                                           ")
        break
