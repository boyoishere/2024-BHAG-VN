# ---------------------------------
# Author: Boyo
# A parody job training game, mostly for the purpose of learning RenPy
# This is Boyo's BHAG 2024
# ---------------------------------
# variables
define n = 0
define view = 0
# ---------------------------------
label start:
    scene bg corpo
    show presenter normal
    show logo
    "[[ARF EXECUTIVES] Welcome to the ARF Security Awareness Training."
    jump travel
    "This training is essential for understanding the role of confidentiality--"
    "--and secure practices within our operations."
    "Noncompliance could endanger your position, our agents, and the lives we strive to protect."
    hide presenter normal
    show zilang avatar
    "In this training, you will assume the role of Agent Zilang,"
    "who is tasked with balancing the various aspects of secure practices."
    "Through the course of a typical workday, your decisions will shape not only his success--"
    "--but your own readiness to uphold ARF's standards as an incoming agent. Good luck."
# ---------------------------------
label intro:
    scene bg apartment with fade
    "(Default Android alarm)"
    "[[???] Mmm...Argh...Grrr....."
    "(Loud default Android alarm)"
    "(Click. Alarm stops.)"
    "[[ZILANG] Good morning."
    show zilang neutral
    "What should I have for breakfast?"
    hide zilang neutral
    show breakfast all
    menu intro0:
        "A bowl of Boy-O Crisp breakfast cereal":
            hide breakfast all
            show breakfast cereal
            "Boy-O Crisp breakfast cereal is my favorite brand of breakfast cereal."
            "You can get 4 large size boxes for only $4 right now at Walmart."
            hide breakfast cereal
        "A cup of Moogurt yogurt":
            hide breakfast all
            show breakfast yogurt
            "Never liked this brand, but it's I suppose it's healthy."
            hide breakfast yogurt
    show zilang neutral
    "{i}While devouring your cold, bite-sized, barely healthy breakfast, you turn on the TV.{/i}"
    hide zilang neutral
    show cut news
    "[[NEWS ANCHOR] 47%% of Washington firms has suffered data breach,"
    "resulting in severe financial loss this year."
    "The FBI has issued an urgent announcement advising heightened caution when navigating--"
    hide cut news
    show zilang neutral
    "[[ZILANG] Oh boy! It's almost 8:00. I better head off now."
# ---------------------------------
label travel:
    scene bg travel with fade
    show zilang neutral
    "(Ringtone) {i}You receive a call from your coworker, Pint.{/i}"
    show collegue call
    "[[PINT] Zilang, Beaverton station is asking where you assigned Subject D4 to."
    "Please tell me the address now so they can stop stalling the chase. Also where are you?"
    show zilang talk
    show collegue wait
    "[[ZILANG] Sorry, I'm on my way. I'll be there in 20."
    show zilang neutral
    show collegue call
    "[[PINT] Alright. Can you give me the address?"
    menu travel0:
        "{i}It's probably not a big deal.{/i}":
            $ n += 1
            show cut call with dissolve
            "[[ZILANG] 642 West Delinoise St. I stickied it in the open catalog."
            hide cut call with dissolve
            "[[PINT] Thank god. Thanks I'll see you later."
            hide collegue
            "{i}Pint hangs up.{/i}"
        "Refuse your coworker.":
            show collegue wait
            show zilang talk
            "[[ZILANG] (Hesitant) I understand it's urgent--"
            "but it's against protocol to send information like this over calls."
            show zilang neutral
            "{i}What a good, responsible employee you are!{/i}"
            "[[PINT] ..."
            show collegue upset
            "[[PINT] Ok."
            hide collegue
            "{i}Pint hangs up.{/i}"
    "I gotta get moving."
# ---------------------------------
label entrance:
    scene bg entrance with fade
    show zilang neutral
    "{i}You arrive at the front entrance.{/i}"
    hide zilang
    show swipe 0
    menu swipe:
        "Swipe your ID":
            show swipe 1
            "{i}You swipe yourself in.{/i}"
            "[[???] Took you long enough."
    hide swipe
    show zilang neutral
    "{i}You look behind you.{/i}"
    show zilang talk
    show niko neutral
    "[[ZILANG] Niko? What are you doing out here? Don't you have to be at that meeting?"
    show zilang neutral
    show niko talk
    "[[NIKO] Left my ID in the RV. Again."
    show niko neutral
    "..."
    "......"
    "........."
    show zilang talk
    "[[ZILANG] You know I can't let you in without your ID."
    show zilang neutral
    show niko talk
    "[[NIKO] Zilang, I just need a temporary badge from the front desk."
    menu entrance0:
        "{i}It's probably not a big deal.{/i}":
            $ n += 1
            show niko neutral
            show cut cctv1 with dissolve
            "{i}You swipe in Niko.{/i}"
            show cut cctv2
            "{i}Niko thanks you with a curt nod and enters.{/i}"
        "{i}Refuse your coworker and friend.{/i}":
            show zilang talk
            show niko neutral
            "I...I'm sorry...."
            show niko talk
            "[[NIKO]{i} Sigh.{/i} Figures."
            show zilang neutral
            hide niko
            "{i}Niko leaves to make a call.{/i}"
            "{i}Isn't it difficult to navigate professionalism and personal relationships?{/i}"
# ---------------------------------
label email:
    scene bg office1 with fade
    show zilang neutral
    "{i}You arrive at your desk.{/i}"
    hide zilang neutral
    show email
    "{i}You go through your inbox and open--{/i}"
label emailcheck:
    if view >= 3:
            jump spill
    menu emailmain:
        "the first email":
            $ view += 1
            show email 1
            "Why are they sending me the spending report?"
            "Hopefully it's not about overspending on snacks again."
            menu email1:
                "Report to IT":
                    "Gallen's profile picture is a bit odd...I should forward this to IT just in case."
                    show email
                    jump emailcheck
                "Close":
                    "(Growl) I'll just ask Niko to help me work on this later."
                    show email
                    jump emailcheck
        "the second email":
            $ view += 1
            show email 2
            "(Chuckle) I should forward this one to Niko."
            menu email2:
                "Report to IT":
                    "But nice try. Off to IT you go!"
                    show email
                    jump emailcheck
                "Close":
                    "I'll show it to him later."
                    show email
                    jump emailcheck
                "Find love now":
                    show email virus with dissolve
                    "{i}Curiosity killed the dog.{/i}"
                    # show email
                    jump hotdog
        "the third email":
            $ view += 1
            show email 3
            "I've never seen this before, but it seems better than the old lottery system."
            menu email3:
                "Report to IT":
                    "\"Mobu\" is a horrible speller. Also, who still uses Yahoo?"
                    show email
                    jump emailcheck
                "Close":
                    "I've got enough on my plate for now."
                    show email
                    jump emailcheck
# ---------------------------------
label spill:
    scene bg warehouse with fade
    show zilang neutral
    "{i}After a long day in the office, you go to the warehouse for a change of pace.{/i}"
    hide zilang neutral
    show spill 1
    "{i}You almost step into a puddle.{/i}"
    show zilang neutral
    "[[ZILANG] What is this?"
    menu spillmenu:
        "Investigate alone":
            "Die."
        "Report this":
            "{i}You call your coworker.{/i}"
            show collegue call
            "[[]]"
        "Leave it to dry":
            "Someone probably spilled their water."
            jump ending
# ---------------------------------
# ENDINGS
# ---------------------------------
label ending:
    scene bg apartment night with fade
    show zilang neutral
    "{i}At last, you arrive at home. You check the results of today's assessment.{/i}"
    if n >= 4:
        jump ending3
    elif n >= 2:
        jump ending2
    else:
        jump ending1
label ending3:
    show ending 3
    "{i}You are a very adventurous individual, and ARF wishes you the best with your adventures elsewhere!{/i}"
    return
label ending2:
    show ending 2
    "{i}You were quite alright. ARF looks forward to your future trainings!{/i}"
    return
label ending1:
    show ending 1
    "{i}Corporate loves you!{/i}"
    # show zilang happy
    # hide ending 1
    return
# ---------------------------------
# BONUSES
# ---------------------------------
label hotdog:
    show email hotdog
    menu hotdogmenu:
        "Hot Dog":
            jump hotdogmenu
        "Hot Dog":
            jump hotdogmenu
        "Hot Dog":
            jump hotdogmenu
        "Send your laptop to IT":
            "{i}Embarassing.{/i}"
            jump spill
label death:
    scene zilang dead
    "{i}You inhaled too much fume from that unidentified puddle.{/i}"
# ---------------------------------