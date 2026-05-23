def dhurandhar():
    i = True 
    while i == True:
        print("\nAvailable roles are:-\n'Hamza Ali Mazari' , 'Major Iqbal'")
        asking_user_char = input("what do you want to play as a --> ").title().strip()
        
        if asking_user_char == "Hamza Ali Mazari":
            print("<----select your mission------>")
            mission1 = input("Facing uzair baloch after his brother's death--> ").strip().lower()
            mission2 = input("Facing SP chaudihiry aslam after you betrayed him ---> ").strip().lower()
            mission3 = input("Taking over KARACHI-->").strip().lower()
            
            # --- HAMZA: MISSION 1 ---
            if mission1 == "yes":
                print("OK")
                print("your mission starts from now")
                print("your main target is to gain or maintain Uzair baloche's trust ")
                trust = 100
                option_for_mainchar_mission_1 = {
                    1: "nothing will happen uzair ",
                    2: "i know who has killed him ",
                    3: "we will kill that chaudhiry!!!"
                }
                uzair = {
                    1: "uzair:- 'we wll kill that person who has killed my brotheer!!!!'",
                    2: "uzair:- 'so you know who killed my brother'",
                    3: "uzair:- 'how do you know the SP haz killed my brother,because no one was there'"
                }

                print("Uzair is crying because of his brothers death ")
                print("you have to maintain uzair's trust if the level reaches 25 he will catch you")
                print("\nOptions are:-")
                print(f"1: {option_for_mainchar_mission_1[1]}")
                print(f"2: {option_for_mainchar_mission_1[2]}")
                print(f"3: {option_for_mainchar_mission_1[3]}")
                
                talk1 = input("\nWrite which option you want to take (1/2/3): ")
                if talk1 == "1": 
                    print(uzair[1])
                    print("trust level:---", trust)
                    print("you have successfully maintained the trust level")
                    print("----w__i__n----")
                    i = False
                elif talk1 == "2":
                    print(uzair[2])
                    print("trust level :--", trust - 50)
                    print("uzair is doubting you now. Stay safe!")
                    print("----w__i__n----")
                    i = False
                elif talk1 == "3":
                    print(uzair[3])
                    print("trust level:--", trust - 80)
                    print("uzair has killed you")
                    print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
                    i = False
                else:
                    print("wrong input entered")
            
            # --- HAMZA: MISSION 2 ---
            elif mission2 == "yes":
                anger_level = 60
                char_option = {
                    1: "i have another plan ",
                    2: "it was not the right time",     
                    3: "i have another and better plan "
                }
                sp = {
                    1: "why you have betrayed me!!!!!!!!",
                    2: "what is your plan ", 
                    3: "that was the perfect plan "
                }
                print("you have to maintain his anger level")
                print("your mission starts from now")
                print(sp[1])
                print("anger level:---", anger_level)
                print("\nOptions are:-")
                print(f"1: {char_option[1]}")
                print(f"2: {char_option[2]}")
                print(f"3: {char_option[3]}")
                
                talk2 = input("\nWrite which option you want to take (1/2/3): ")
                if talk2 == "1":
                    print("it was the perfect plan!!!!!")
                    print("anger level:---", anger_level + 60)
                    print("_______D_E_A_D______")
                    print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
                    i = False
                elif talk2 == "2":
                    print("it was")
                    print("anger level:---", anger_level + 40)
                    print("_______D_E_A_D______")
                    print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
                    i = False
                elif talk2 == "3":
                    print(sp[2])
                    print("anger level:---", anger_level - 30)
                    print("----w__i__n----")
                    i = False
                else:
                    print("wrong input entered")
                    
            # --- HAMZA: MISSION 3 ---
            elif mission3 == "yes":
                print("in this mission you have to escape from iqbal ")
                weapon_hamza = {
                    1: "hammer",
                    2: "chain",
                    3: "knife"
                }
                print("major iqbal has an empty gun")
                print("which weapon will you take?")
                print(f"1: {weapon_hamza[1]}")
                print(f"2: {weapon_hamza[2]}")
                print(f"3: {weapon_hamza[3]}")
                
                talk3 = input("\nWrite which option you want to take (1/2/3): ")
                if talk3 == "1":
                    print("major has killed you ")
                    print("_______D_E_A_D______")
                    print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
                    i = False
                elif talk3 == "2":
                    print("you and major are injured, so technically you win ")
                    print("----w__i__n----")
                    i = False
                elif talk3 == "3":  
                    print("major has hit you on your head and you are unconscious now ")
                    print("_______D_E_A_D______")
                    print("--------DEAD----------\n--G_A_M_E ---O_V_E_R--")
                    i = False            
                else:
                    print("wrong input entered")
            else:
                print("\nYou didn't select any mission. Returning to role selection...")

        # --- ROLE: MAJOR IQBAL ---
        elif asking_user_char == "Major Iqbal":
            mission4 = input("Killing Hamza in mosque (yes/no):-- ").lower().strip()
            mission5 = input("Planing Mumbai bomb blast (yes/no):-- ").lower().strip()
            mission6 = input("Escapping froom Hamza (yes/no):-- ").lower().strip()
            
            # --- MAJOR IQBAL: MISSION 4 ---
            if mission4 == "yes":
                print("You are sitting in a chair waiting for him.")
                print("Major:- We will succeed in our mission! (giving a speech to your members)")
                
                hamza1 = {
                    1: "Hi Major.",
                    2: "I want to tell you something. You will not succeed in your plan.",
                    3: "You will not stay alive!!!!."
                }
                iqabl1 = {
                    1: "Hi Hamza.",
                    2: "What... hmm... I think before that you will die soon.",
                    3: "You shoot your gun! Hamza tries to dodge, but one bullet hits his hand."
                }
                
                print(hamza1[1])
                print(iqabl1[1])
                print(hamza1[2])
                print(iqabl1[2])
                print(hamza1[3])
                print(iqabl1[3])
                
                print("\n---------PHASE 2--------- ")
                print("Hamza is running.")
                choice = input("Will you run to catch him (yes/no):-- ").lower().strip()
                
                if choice == "yes":
                    print("You are running.")
                    print("You are now in an abandoned area. Be careful, he can kill you here.")
                    print("You heard a sound behind the bushes.")
                    shoot = input("Will you shoot in the bushes (yes/no):-- ").lower().strip()
                    
                    if shoot == "yes":
                        print("There was a dog.")
                        choice1 = input("Will you go close to the dog (yes/no):-- ").lower().strip()
                        
                        if choice1 == "yes":
                            print("You are going close to the dog.")
                            print("Shit! Hamza shot you from a long distance.")
                            choice2 = input("You have two choices: surrender or shoot Hamza. You only have one bullet left! (shoot/surrender):-- ").lower().strip()

                            if choice2 == "surrender":
                                print("Iqbal:- I surrender.")
                                print("Hamza is coming close to you.")
                                choice3 = input("Shoot your last bullet or wait for Hamza to come closer? (shoot/stay):-- ").lower().strip()
                                choice4 = input("Where will you aim? (liver/leg/head):-- ").lower().strip()
                                
                                if choice4 == "liver":
                                    choice5 = input("You shot him in the liver! He is badly injured and you are out of ammo.\nKill him or let him recover? (kill/recover):-- ").lower().strip()
                                    if choice5 == "kill":
                                        print("----w__i__n----")
                                        i = False
                                    elif choice5 == "recover":
                                        print("Hamza recovered and overpowered you.\n-------GAME OVER-------")
                                        i = False
                                else:
                                    print("Your shot missed or didn't stop him!\n-------GAME OVER-------")
                                    i = False
                                        
                            elif choice2 == "shoot":
                                print("You shot at Hamza! That was your last bullet.")
                                print("Luckily, Hamza is injured by that bullet, allowing you to secure the area!")
                                print("----w__i__n----")
                                i = False
                                
                        elif choice1 == "no":
                            print("You backed away from the dog, but lost track of Hamza.")
                            print("-------GAME OVER-------")
                            i = False
                                
                    elif shoot == "no":  
                        print("There was a dog. You chose safety, but Hamza escaped.")
                        print("-------GAME OVER-------")
                        i = False
                        
                elif choice == "no":
                    print("----w__i__n----\nThat was the best choice.")
                    i = False

            # --- MAJOR IQBAL: MISSION 5 (NEW) ---
            elif mission5 == "yes":
                print("\n--------- MISSION 5: THE MUMBAI CONSPIRACY ---------")
                print("Major Iqbal, your operatives are in position across Mumbai.")
                print("The blueprints are laid out. Intelligence reports increased security.")
                
                m5_choice1 = input("Do you deploy the main blast units at the Sea Port or the Central Station? (port/station):-- ").lower().strip()
                
                if m5_choice1 == "station":
                    print("\nCentral Station security is impenetrable! Your team gets intercepted by anti-terror squads.")
                    print("The local police tracer loops back directly to your safehouse coordinates.")
                    m5_sub = input("Do you stand your ground and fight, or burn the files and evacuate? (fight/evacuate):-- ").lower().strip()
                    
                    if m5_sub == "evacuate":
                        print("\nYou successfully burned the evidence and slipped out into the shadows just in time.")
                        print("The mission failed, but you survived to plot another day.")
                        print("----w__i__n----")
                        i = False
                    else:
                        print("\nYou are completely outnumbered. Elite forces breach the room.")
                        print("_______D_E_A_D______\n-------GAME OVER-------")
                        i = False
                        
                elif m5_choice1 == "port":
                    print("\nThe Sea Port operation goes perfectly. The diversion draws all local forces away.")
                    print("Suddenly, your tracking feed detects a digital breach. Someone is uploading a counter-virus.")
                    print("It's Hamza! He's trying to brick your detonation server from a remote uplink.")
                    
                    m5_choice2 = input("Do you try to trace Hamza's location or push the detonation override immediately? (trace/override):-- ").lower().strip()
                    
                    if m5_choice2 == "override":
                        print("\nDetonation complete. The harbor erupts into chaos, completing your objective.")
                        print("However, because you didn't look for Hamza, he tracks your signature and pins your position.")
                        print("You achieved your goal, but you are now a hunted man.")
                        print("----w__i__n----")
                        i = False
                    elif m5_choice2 == "trace":
                        print("\nYou successfully trace the signal to an old warehouse near the docks.")
                        print("You corner Hamza before he can stop your server. You force him to retreat!")
                        print("The operation succeeds flawlessly with zero loose ends left behind.")
                        print("----w__i__n----")
                        i = False
                    else:
                        print("Hesitation cost you everything. Hamza shuts down the grid. You are captured.")
                        print("-------GAME OVER-------")
                        i = False

            # --- MAJOR IQBAL: MISSION 6 (NEW) ---
            elif mission6 == "yes":
                print("\n--------- MISSION 6: THE GREAT ESCAPE ---------")
                print("The tables have turned. Hamza's strike team has surrounded your compound.")
                print("Alarms are blaring. Smoke fills the corridors as the outer security gate collapses.")
                
                m6_choice1 = input("Do you attempt to escape through the subterranean sewer line or take the armored SUV in the garage? (sewer/suv):-- ").lower().strip()
                
                if m6_choice1 == "suv":
                    print("\nYou slam on the gas and smash through the front barricade!")
                    print("But Hamza was waiting with a rocket launcher. The vehicle takes a direct hit.")
                    print("_______D_E_A_D______\n-------GAME OVER-------")
                    i = False
                    
                elif m6_choice1 == "sewer":
                    print("\nYou navigate the dark, wet underground pipelines in complete silence.")
                    print("You emerge near the riverbanks just as dawn breaks, but you hear footsteps behind you.")
                    print("It's Hamza alone, blocking your path to the getaway boat with his weapon drawn.")
                    
                    m6_choice2 = input("Your primary gun is jammed. Do you throw a smoke grenade to blind him, or lunge at him with your tactical knife? (smoke/knife):-- ").lower().strip()
                    
                    if m6_choice2 == "smoke":
                        print("\nThe area is completely blanketed in thick, white phosphorus smoke.")
                        print("Hamza fires blindly into the mist, missing you completely.")
                        print("You jump onto the speed boat, fire up the engine, and disappear across the water network.")
                        print("Major Iqbal has successfully broken the net!")
                        print("----w__i__n----")
                        i = False
                    elif m6_choice2 == "knife":
                        print("\nYou try to close the distance, but Hamza's reaction speed is superior.")
                        print("He counters your wrist movement, disarms you, and secures your arrest.")
                        print("-------GAME OVER-------")
                        i = False
                    else:
                        print("Standing frozen in the open makes you an easy target. Hamza takes the shot.")
                        print("_______D_E_A_D______\n-------GAME OVER-------")
                        i = False
            else:
                print("\nYou didn't select any mission. Returning to role selection...")
dhurandhar()     
from unittest.mock import patch
# Assuming your game code is in a file named dhurandhar.py
from dhurandhar import dhurandhar

# 1. Define a list of inputs you want to test automatically
test_inputs = ["Major Iqbal", "yes", "no", "no"]

# 2. This 'patch' replaces input() with your list item-by-item
@patch('builtins.input', side_effect=test_inputs)
def run_automatic_test(mocked_input):
    print(f"--- STARTING AUTOMATED TEST WITH INPUTS: {test_inputs} ---")
    try:
        dhurandhar()
    except StopIteration:
        # This catches the game when it runs out of inputs
        print("\n--- TEST FINISHED SUCCESSFULLY ---")

# Run the test
run_automatic_test()           