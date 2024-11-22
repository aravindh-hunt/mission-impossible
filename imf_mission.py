import random
import time

def agent_name():
    global name
    global codename
    name = input("Could you please tell your name: ")
    codename = input("Please enter your code name: ")


def verification(name, codename):
    if (name in ['Ethan', 'Hunt', 'Ethan_Hunt']) and (codename == 'Bravo_Echo'):
        print(f"""
        Verification successful
        Agent_Name: Ethan_Hunt
        Code_Name: Bravo_Echo
        Role: Team Leader
        Good to see you, Mr. Hunt!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':

            ethan_m1 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves the recovery of the NOC list, which contains the true identities of all IMF agents. A mole within the IMF has stolen the list and intends to sell it to the highest bidder, posing a catastrophic threat to global security.

                Your mission objectives are as follows:
                1. Prove your innocence after being framed for the deaths of your team.
                2. Retrieve the stolen NOC list.
                3. Expose the mole within the IMF.

                You will operate with limited support, as your usual contacts may be compromised. Trust no one and utilize your unique skills to complete this mission.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_m2 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves the recovery of a deadly virus known as Chimera, which has fallen into the hands of a rogue IMF operative, Sean Ambrose. Ambrose intends to auction the virus to the highest bidder, posing a catastrophic threat to global security.

                Your mission objectives are as follows:
                1. Gain the trust of Ambrose and his inner circle.
                2. Locate and secure the Chimera virus.
                3. Neutralize Ambrose and dismantle his operation.

                You will have the support of your trusted team members, Luther Stickell and Benji Dunn, who will provide technical and field support. Additionally, Nyah Nordoff-Hall, who has a past with Ambrose, will assist you in gaining access to his network.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_m3 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves the rescue of captured agent Lindsey Farris and the recovery of a dangerous weapon called the "Rabbit's Foot." Lindsey has been taken by ruthless arms dealer Owen Davian, who possesses the Rabbit's Foot.

                Your mission objectives are as follows:
                1. Rescue agent Lindsey Farris.
                2. Secure the Rabbit's Foot.
                3. Protect your fiancée, Julia, from Davian's plans.

                You will have the support of your trusted team members, Luther Stickell and Benji Dunn. Utilize their expertise to overcome Davian's defenses and succeed in your mission.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_m4 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves preventing nuclear war by stopping Russian extremist, Kurt Hendricks, who has initiated a plan to detonate nuclear missiles.

                Your mission objectives are as follows:
                1. Infiltrate Hendricks' network.
                2. Intercept the launch codes for the nuclear missiles.
                3. Prevent the detonation and avert global catastrophe.

                You will have the support of Jane Carter, William Brandt, and Benji Dunn. Together, you must operate without IMF backup and utilize your skills to stop Hendricks.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_m5 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves dismantling the Syndicate, an international rogue organization aiming to create a new world order through acts of terror.

                Your mission objectives are as follows:
                1. Uncover the existence of the Syndicate.
                2. Team up with MI6 agent Ilsa Faust.
                3. Bring down the Syndicate's leader, Solomon Lane.

                You will have the support of your trusted team members, including Benji Dunn, Luther Stickell, and William Brandt. Navigate a series of deadly traps and thwart the Syndicate's plans.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_m6 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves preventing a nuclear catastrophe by stopping rogue ex-IMF agents who have stolen plutonium and plan to detonate nuclear bombs.

                Your mission objectives are as follows:
                1. Retrieve the stolen plutonium.
                2. Thwart the plan to detonate nuclear bombs.
                3. Reunite with allies and navigate personal dilemmas to ensure success.

                You will have the support of your trusted team members, including Benji Dunn, Luther Stickell, and Ilsa Faust. Face the challenges ahead with resilience and determination.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_m7 = ("""
            Good morning, Mr. Hunt. Your mission, should you choose to accept it, involves uncovering and stopping a threat posed by a powerful rogue AI network.

                Your mission objectives are as follows:
                1. Navigate a world of espionage and betrayal.
                2. Dismantle the rogue AI network.
                3. Prevent the AI from falling into the wrong hands and being weaponized.

                You will have the support of your trusted team members, including Benji Dunn, Luther Stickell, and Ilsa Faust. Trust your instincts and utilize your team's expertise to neutralize this unprecedented danger.

                As always, should you or any member of your IMF team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ethan.
            """)

            ethan_mission = [ethan_m1, ethan_m2, ethan_m3, ethan_m4, ethan_m5, ethan_m6, ethan_m7]

            random_mission = random.choice(ethan_mission)
            print(random_mission)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")
    elif (name in ['Ilsa', 'Faust', 'Ilsa_Faust']) and (codename == 'Blitz'):
        print(f"""
        Verification successful
        Agent_Name: Ilsa_Faust
        Code_Name: Blitz
        Role: Field Agent
        Good to see you, Ms. Faust!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':

            ilsa_m1 = ("""
            Good morning, Ms. Faust. Your mission, should you choose to accept it, involves dismantling the Syndicate, an international rogue organization aiming to create a new world order through acts of terror.

                Your mission objectives are as follows:
                1. Uncover the existence of the Syndicate.
                2. Gather intelligence on their operations.
                3. Eliminate their leader, Solomon Lane.

                You will collaborate with Ethan Hunt and his IMF team. Use your expertise to navigate complex environments and neutralize this threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ilsa.
            """)

            ilsa_m2 = ("""
            Good morning, Ms. Faust. Your mission, should you choose to accept it, involves preventing a nuclear catastrophe planned by a group of rogue ex-IMF agents who have acquired plutonium.

                Your mission objectives are as follows:
                1. Retrieve the stolen plutonium.
                2. Thwart the plan to detonate nuclear bombs.
                3. Neutralize the rogue agents and secure the plutonium.

                You will have the support of Ethan Hunt and his IMF team. Utilize your skills and training to ensure the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ilsa.
            """)

            ilsa_m3 = ("""
            Good morning, Ms. Faust. Your mission, should you choose to accept it, involves uncovering and stopping a powerful AI network that has gone rogue and poses a significant threat to global security.

                Your mission objectives are as follows:
                1. Infiltrate the rogue AI network.
                2. Dismantle the AI's control systems.
                3. Prevent the AI from being weaponized.

                You will collaborate with Ethan Hunt and his IMF team. Trust your instincts and employ your technical prowess to neutralize this unprecedented threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Ilsa.
            """)

            ilsa_mission = [ilsa_m1, ilsa_m2, ilsa_m3]

            random_mission_ilsa = random.choice(ilsa_mission)
            print(random_mission_ilsa)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")



    elif (name in ['Luther', 'Stickell', 'Luther_Stickell']) and (codename == 'Phantom'):
        print(f"""
        Verification successful
        Agent_Name: Luther_Stickell
        Code_Name: Phantom
        Role: Tech Specialist
        Good to see you, Mr. Stickell!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':

            luther_m1 = ("""
            Good morning, Mr. Stickell. Your mission, should you choose to accept it, involves supporting Ethan Hunt in preventing the theft of the NOC list, which contains the true identities of all IMF agents.

                Your mission objectives are as follows:
                1. Assist in intercepting the stolen NOC list.
                2. Provide technical support to uncover the mole within the IMF.
                3. Ensure the list does not fall into enemy hands.

                You will work closely with Ethan Hunt, utilizing your expertise in cybersecurity and operations. Your technical skills are crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Luther.
            """)

            luther_m2 = ("""
            Good morning, Mr. Stickell. Your mission, should you choose to accept it, involves preventing nuclear war by supporting Ethan Hunt in stopping Russian extremist Kurt Hendricks, who plans to detonate nuclear missiles.

                Your mission objectives are as follows:
                1. Provide technical support for intercepting the launch codes.
                2. Assist in navigating the team's infiltration operations.
                3. Ensure all technical systems are secure to prevent the detonation.

                You will operate alongside Ethan Hunt, Jane Carter, and William Brandt. Your expertise in cybersecurity and field operations is vital to stopping this threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Luther.
            """)

            luther_m3 = ("""
            Good morning, Mr. Stickell. Your mission, should you choose to accept it, involves dismantling the Syndicate, an international rogue organization aiming to create a new world order through acts of terror.

                Your mission objectives are as follows:
                1. Provide technical and operational support to gather intelligence on the Syndicate.
                2. Assist Ethan Hunt and Ilsa Faust in their field missions.
                3. Ensure secure communication and data encryption during operations.

                You will collaborate with Ethan Hunt, Benji Dunn, and Ilsa Faust. Your skills in cybersecurity and technical operations are essential to dismantling the Syndicate.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Luther.
            """)

            luther_m4 = ("""
            Good morning, Mr. Stickell. Your mission, should you choose to accept it, involves preventing a nuclear catastrophe by supporting Ethan Hunt in stopping rogue ex-IMF agents who have stolen plutonium.

                Your mission objectives are as follows:
                1. Provide technical support to locate the stolen plutonium.
                2. Assist in thwarting the plan to detonate nuclear bombs.
                3. Ensure secure communication and technical operations during the mission.

                You will work closely with Ethan Hunt, Benji Dunn, and Ilsa Faust. Your expertise in cybersecurity and operations is crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Luther.
            """)

            luther_m5 = ("""
            Good morning, Mr. Stickell. Your mission, should you choose to accept it, involves uncovering and stopping a powerful AI network that has gone rogue and poses a significant threat to global security.

                Your mission objectives are as follows:
                1. Provide technical support to infiltrate the rogue AI network.
                2. Assist in dismantling the AI's control systems.
                3. Ensure secure communication and technical operations during the mission.

                You will collaborate with Ethan Hunt, Benji Dunn, and Ilsa Faust. Your technical prowess and expertise in cybersecurity are essential to neutralizing this unprecedented threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Luther.
            """)

            luther_mission = [luther_m1, luther_m2, luther_m3, luther_m4, luther_m5]

            random_mission_luther = random.choice(luther_mission)
            print(random_mission_luther)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")


    elif (name in ['Benji', 'Dunn', 'Benji_Dunn']) and (codename == 'Wizen'):
        print(f"""
        Verification successful
        Agent_Name: Benji_Dunn
        Code_Name: Wizen
        Role: Field Agent
        Good to see you, Mr. Dunn!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':

            benji_m1 = ("""
            Good morning, Mr. Dunn. Your mission, should you choose to accept it, involves providing critical tech support to Ethan Hunt's team during the recovery of the "Rabbit's Foot," a dangerous weapon in the possession of arms dealer Owen Davian.

                Your mission objectives are as follows:
                1. Ensure secure communication and technical support for the team.
                2. Assist in tracking and intercepting the Rabbit's Foot.
                3. Provide real-time hacking and surveillance support as needed.

                You will be operating remotely, utilizing your technical expertise to support the team in the field. Your skills are crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Benji.
            """)

            benji_m2 = ("""
            Good morning, Mr. Dunn. Your mission, should you choose to accept it, involves preventing nuclear war by supporting Ethan Hunt's team in stopping Russian extremist Kurt Hendricks, who plans to detonate nuclear missiles.

                Your mission objectives are as follows:
                1. Provide technical support for intercepting the launch codes.
                2. Assist in the team's infiltration operations with advanced surveillance and hacking.
                3. Ensure all technical systems are secure to prevent the detonation.

                You will operate alongside Ethan Hunt, Jane Carter, and William Brandt. Your expertise in technology and field operations is vital to stopping this threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Benji.
            """)

            benji_m3 = ("""
            Good morning, Mr. Dunn. Your mission, should you choose to accept it, involves dismantling the Syndicate, an international rogue organization aiming to create a new world order through acts of terror.

                Your mission objectives are as follows:
                1. Provide technical and operational support to gather intelligence on the Syndicate.
                2. Assist Ethan Hunt and Ilsa Faust in their field missions with hacking and surveillance.
                3. Ensure secure communication and data encryption during operations.

                You will collaborate with Ethan Hunt, Luther Stickell, and Ilsa Faust. Your skills in technology and field operations are essential to dismantling the Syndicate.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Benji.
            """)

            benji_m4 = ("""
            Good morning, Mr. Dunn. Your mission, should you choose to accept it, involves preventing a nuclear catastrophe by supporting Ethan Hunt in stopping rogue ex-IMF agents who have stolen plutonium.

                Your mission objectives are as follows:
                1. Provide technical support to locate the stolen plutonium.
                2. Assist in thwarting the plan to detonate nuclear bombs.
                3. Ensure secure communication and technical operations during the mission.

                You will work closely with Ethan Hunt, Luther Stickell, and Ilsa Faust. Your expertise in technology and field operations is crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Benji.
            """)

            benji_m5 = ("""
            Good morning, Mr. Dunn. Your mission, should you choose to accept it, involves uncovering and stopping a powerful AI network that has gone rogue and poses a significant threat to global security.

                Your mission objectives are as follows:
                1. Provide technical support to infiltrate the rogue AI network.
                2. Assist in dismantling the AI's control systems.
                3. Ensure secure communication and technical operations during the mission.

                You will collaborate with Ethan Hunt, Luther Stickell, and Ilsa Faust. Your technical prowess and expertise in cybersecurity are essential to neutralizing this unprecedented threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Benji.
            """)

            benji_mission = [benji_m1, benji_m2, benji_m3, benji_m4, benji_m5]

            random_mission_benji = random.choice(benji_mission)
            print(random_mission_benji)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")


    elif (name in ['William', 'Brandt', 'William_Brandt']) and (codename == 'Sentry'):
        print(f"""
        Verification successful
        Agent_Name: William_Brandt
        Code_Name: Sentry
        Role: Analyst
        Good to see you, Mr. Brandt!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':

            brandt_m1 = ("""
            Good morning, Mr. Brandt. Your mission, should you choose to accept it, involves preventing nuclear war by supporting Ethan Hunt's team in stopping Russian extremist Kurt Hendricks, who plans to detonate nuclear missiles.

                Your mission objectives are as follows:
                1. Provide tactical support for intercepting the launch codes.
                2. Assist in the infiltration of high-security locations.
                3. Ensure the team's safety and coordinate field operations.

                You will operate alongside Ethan Hunt, Jane Carter, and Benji Dunn. Your expertise in field operations and tactical planning is vital to stopping this threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Brandt.
            """)

            brandt_m2 = ("""
            Good morning, Mr. Brandt. Your mission, should you choose to accept it, involves dismantling the Syndicate, an international rogue organization aiming to create a new world order through acts of terror.

                Your mission objectives are as follows:
                1. Provide tactical and operational support to gather intelligence on the Syndicate.
                2. Assist Ethan Hunt and Ilsa Faust in field missions.
                3. Ensure secure communication and coordination during operations.

                You will collaborate with Ethan Hunt, Luther Stickell, and Benji Dunn. Your skills in field operations and tactical planning are essential to dismantling the Syndicate.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Brandt.
            """)

            brandt_m3 = ("""
            Good morning, Mr. Brandt. Your mission, should you choose to accept it, involves preventing a nuclear catastrophe by supporting Ethan Hunt in stopping rogue ex-IMF agents who have stolen plutonium.

                Your mission objectives are as follows:
                1. Provide tactical support to locate the stolen plutonium.
                2. Assist in thwarting the plan to detonate nuclear bombs.
                3. Ensure secure communication and coordination during the mission.

                You will work closely with Ethan Hunt, Luther Stickell, and Benji Dunn. Your expertise in field operations and tactical planning is crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Brandt.
            """)

            brandt_mission = [brandt_m1, brandt_m2, brandt_m3]

            random_mission_brandt = random.choice(brandt_mission)
            print(random_mission_brandt)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")


    elif (name in ['Jane', 'Carter', 'Jane_Carter']) and (codename == 'Phoenix'):
        print(f"""
        Verification successful
        Agent_Name: Jane_Carter
        Code_Name: Phoenix
        Role: Field Agent
        Good to see you, Ms. Carter!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':
            print("""
            Good morning, Ms. Carter. Your mission, should you choose to accept it, involves preventing nuclear war by supporting Ethan Hunt's team in stopping Russian extremist Kurt Hendricks, who plans to detonate nuclear missiles.

                Your mission objectives are as follows:
                1. Provide tactical and field support for the team.
                2. Assist in the infiltration of high-security locations.
                3. Ensure the team's safety and coordinate field operations.

                You will operate alongside Ethan Hunt, William Brandt, and Benji Dunn. Your expertise in field operations is vital to stopping this threat.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Jane.
            """)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")


    elif (name in ['Zhen', 'Lei', 'Zhen_Lei']) and (codename == 'Phoenix'):
        print(f"""
        Verification successful
        Agent_Name: Zhen_Lei
        Code_Name: Phoenix
        Role: Field Agent
        Good to see you, Ms. Lei!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':
            print("""
            Good morning, Ms. Lei. Your mission, should you choose to accept it, involves supporting Ethan Hunt's team during the recovery of the "Rabbit's Foot," a dangerous weapon in the possession of arms dealer Owen Davian.

                Your mission objectives are as follows:
                1. Provide tactical and field support to the team.
                2. Assist in tracking and intercepting the Rabbit's Foot.
                3. Ensure the team's safety during the mission.

                You will operate alongside Ethan Hunt, Luther Stickell, and Declan Gormley. Your skills in field operations are crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Zhen.
            """)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")


    elif (name in ['Declan', 'Gormley', 'Declan_Gormley']) and (codename == 'Sentry'):
        print(f"""
        Verification successful
        Agent_Name: Declan_Gormley
        Code_Name: Sentry
        Role: Field Agent
        Good to see you, Mr. Gormley!
        We have a mission for you, a really important mission.
        """)
        status = input("Are you interested in it? 'YES' or 'NO' - ")
        if status.upper() == 'YES':
            print("""
            Good morning, Mr. Gormley. Your mission, should you choose to accept it, involves providing critical support to Ethan Hunt's team during the recovery of the "Rabbit's Foot," a dangerous weapon in the possession of arms dealer Owen Davian.

                Your mission objectives are as follows:
                1. Provide tactical and technical support for the team.
                2. Assist in tracking and intercepting the Rabbit's Foot.
                3. Ensure the team's safety and coordination during the mission.

                You will operate alongside Ethan Hunt, Luther Stickell, and Zhen Lei. Your skills in field operations and technical support are crucial to the success of this mission.

                As always, should you or any member of your team be caught or killed, the Secretary will disavow any knowledge of your actions. This message will self-destruct in five seconds. Good luck, Declan.
            """)

        elif status.upper() == 'NO':
            print(f"Nice to meet you, {name}. We will inform you about our next mission soon.")
            print("This message will self-destruct in five seconds.")


    else:
        print("""
          ██████████   ACCESS DENIED   ██████████
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
         ████ Unauthorized Access Attempt ████
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
         ░░ This alert will self-destruct in five seconds. ░░

        """)



agent_name()
verification(name, codename)

time.sleep(5)

print(r"""

     _.-^^---....,,--       

 _--                  --_  

<                        >)

|                         |

 \._                   _./ 

    `--. . , ; .--'     

          | |   |        

       .-=||  | |=-.   

       `-=#$%&%$#=-'   

          | ;  :|     

  _____.,-#%&$@%#&#~,._____

           BOOM!

            """)
