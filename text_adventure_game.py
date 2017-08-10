start = '''
You wake up, change and get ready to go to work.
'''
input_var = input("What's your name?")

print(start)
print("Type 'train' to take the train to work or 'walk' to walk to work.")

while (1>0):
    user_input = input()
    if user_input == "train":
        print("You get on the train. Luckily, there is an open seat! You sit down next to a woman about your age and immedieatley pull out your phone and begin scrolling through instagram. You are distracted by a voice coming from the woman besides you. She is asking, 'Have we met before?' You are in the mood for talking. Type 'respond' to talk to the stranger or 'ignore' to continue scrolling through your phone in peace.")
        while (1>0):
            user_input = input()
            if user_input == "ignore":
                print("You ignore the woman. You notice her get to her feet suddently and insults you. You look up in confusion and discover it was your old college friend! Before you can say anything, she crosses to the adjacent cart and disappears. You continue on to work in a foul mood, upset to have lost the chance to catch up with an old friend. At work, one of your co-workers is in a bad mood and insults you for not finishing your paperwork fast enough. You are already upset and ready to retaliate. Type 'insult' to curse your co-worker out, or 'breath' to take a deep breath and ignore your co-worker.")
                while (1>0):
                    user_input = input()
                    if user_input == "insult":
                        print("You begin to curse out your co-worker, however your boss happens to walk by just in time to catch you! Your boss fires you for innappropriate work language. Now you have no job. Sucks to be you.")
                        break
                    elif user_input == "breath":
                        print("You take a deep breath and ignore your co-worker's insults. Your boss overhears your co-worker and fires them immedieatley! As a reward for your calm attitude in a stressful situation, your boss promotes you!")
                        break
                    else:
                        print("I don't understand. Type 'insult' to curse your co-worker out, or 'breath' to take a deep breath and ignore your co-worker.")
                        continue
                break
            elif user_input == "respond":
                print("You look up in confusion. She seems vaugley continue. The woman goes on to explain that both of you went to the same grade school! You were in the same third grade class! You begin to chat and have a great morning ride catching up with your chlildhood friend. You exchange numbers. You continue on to work. When you check your phone after work, you see a text from your friend inviting you to dinner. Type 'accept' to go to dinner with your friend or 'decline' to eat alone at home.")
                while (1>0):
                    user_input = input()
                    if user_input == "accept":
                        print("You go out to dinner and reconnect with your friend! Now you have reestablished a friendship that will surley last for a long time.")
                        break
                    elif user_input == "decline":
                        print("You say no to her offer and go home to eat alone.")
                        break
                    else:
                        print("I don't understand. Type 'accept' to go out to dinner with your friend and 'decline' to eat at home.")
                        continue
                break
            else:
                print("I don't understand. Type 'respond' to talk to the woman or 'ignore' to ignore her.")
                continue
        break
    elif user_input == "walk":
        print("You decide to walk to work. It is a nice sunny morning. You are walking peacfully when you notice someone hurry pass you. You watch as their wallet drops out of their bag and onto the cement. The person runs off and is almost down the block by the time you approach the wallet. Type 'pick' to pick the wallet up, 'chase' to run down the street and return the wallet to the stranger, or 'leave' to ignore the wallet and continue on to work.")
        while (1>0):
            user_input = input()
            if user_input == "pick":
                print("You pick up the wallet but you're not in the mood to get your work clothes sweaty by chasing down the stranger. You put the wallet in your pocket and plan to search for contact information after work. You continue on to work, but stop at a coffee shop to grab breakfast. You reach into your bag and realize you forgot your wallet! Thinking back to the stranger's wallet, you wonder if you should use their credit card to buy breakfast since you're very hungry. Type 'use' to use the stranger's wallet, or 'not' to go hungry.")
                while (1>0):
                    user_input = input()
                    if user_input == "not":
                        print("You decide to skip breakfast. After all, it's not your money! You continue to work and are happily surprised to see your co-worker brought donuts for the office! You have a great day and return the wallet to the stranger after work.")
                        break
                    elif user_input == "use":
                        print("You buy your coffee and pastry and continue on to work. Midway through the day, the police break down the office doors. They arrest you for credit-card theft. You go to jail and lose your job. Wow. That sucks.")
                        break
                    else:
                        print("I don't understand. Type 'not' to go hungry and 'use' to buy breakfast with the stranger's credit card.")
                        continue
                break
            elif user_input == "chase":
                print("You pick up the wallet and sprint down the street towards the stranger. The light just turned green, but there are no cars in sight! The stranger is getting away! Type 'cross' to cross the street now or 'wait' to wait for the light to turn red.")
                while (1>0):
                    user_input = input()
                    if user_input == "cross":
                        print("You rush across the street just as a semi-truck rounds the corner! Before you could process what was happening, honking filled your ears and everything went black. RIP " + input_var)
                        break
                    elif user_input == "wait":
                        print("You wait for the light to turn red and then cross. You continue to run and catch the stranger, who has stopped to look through their bag in horror. You approach them and expain how you found their wallet! The stranger sighed in relief and thanked you, offering to take you out for breakfast out of gratitude. Type 'yes' to go to breakfast with the lady, or 'no' to continue to work.")
                        while (1>0):
                            user_input = input()
                            if user_input == "yes":
                                print("You agree to go to breakfast with the lady. You have a great time and proceed to work, full and happy.")
                                break
                            elif user_input == "no":
                                print("The stranger insists on handing you $20 as a thank you. You are greatful and continue on to work in a good mood, happy to have helped and especially happy for the monetary compensation ;)")
                                break
                            else:
                                print("I don't understand. Type 'yes' to go to breakfast with the stranger or 'no' to continue to work.")
                                continue
                        break
                    else:
                        print("I don't understand. Type 'cross' to cross the street or 'wait' to wait for the red light.")
                        continue
                break
            elif user_input == "leave":
                print ("You continue on your way to work, ignoring the wallet.")
                break
            else:
                print("I don't understand. Type 'pick' to pick the wallet up, 'chase' to run down the street and return the wallet to the stranger, or 'leave' to ignore the wallet and continue on to work.")
                continue
        break
    else:
        print ("I don't understand. Type 'train' to take the train to work or 'walk' to walk to work.")
        continue
