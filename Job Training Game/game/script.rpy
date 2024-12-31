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
    jump entrance
    "This orientation is essential for understanding the critical role of confidentiality--"
    "--and secure practices within our operations."
    "Here, we don't just protect people from animals and animals from people,"
    "we protect our knowledge, our methods, and our secrets from those who might exploit them."
    "Noncompliance could endanger your position, our agents, and the lives we strive to protect."
    hide presenter normal
    show zilang avatar
    "In this training, you will assume the role of Agent Zilang,"
    "who is tasked with balancing the physical and digital aspects of information security today."
    "Through the course of a typical workday, your decisions will shape not only his success--"
    "--but your own readiness to uphold integrity and confidentiality at ARF. Good luck."
# ---------------------------------
label intro:
    scene bg apartment with fade
    "[[ZILANG] (Yawning) Good morning world..."
    show zilang neutral
    "What should I eat for breakfast today?"
    hide zilang neutral
    show breakfast all
    menu intro0:
        "A bowl of Boy-O Crisp breakfast cereal":
            hide breakfast all
            show breakfast cereal
            "Boy-O Crisp breakfast cereal sure is the best."
            "You can get 4 large size boxes for only $4 right now at Walmart."
            hide breakfast cereal
        "A cup of Moogurt yogurt":
            hide breakfast all
            show breakfast yogurt
            "I never liked this brand, but it's I suppose it's healthy..."
            hide breakfast yogurt
    show zilang neutral
    "{i}While devouring your cold, bite-sized breakfast, you turn on the TV.{/i}"
    hide zilang neutral
    show cut news
    "[[NEWS ANCHOR] Across multiple firms across Washington has reported incidents of security breach last night."
    "FBI posted an emergent announcement to navigate work sites with extra caution--"
    hide cut news
    show zilang neutral
    "Shoot, it's almost 7:00. I better head off now."
# ---------------------------------
label travel:
    scene bg travel with fade
    show zilang neutral
    "(Ringtone) {i}You receive a call from your coworker, Pint.{/i}"
    show collegue call
    "[[PINT] Zilang, where are you? The client is waiting."
    "[[ZILANG] Sorry, I'm on my way. I'll be there in 20."
    "[[PINT] Ok... Do you still rememeber her case number?"
    menu travel0:
        "Tell him":
            $ n += 1
            show cut call with dissolve
            "[[ZILANG] You can find it in the open catalog. It was H23-something..."
            hide cut call with dissolve
            "[[PINT] Okay thanks, I'll see you later."
            hide collegue
            "{i}Pint hangs up.{/i}"
            "I gotta get moving."
        "\"Yes, but I can't tell you until I get to the office.\"":
            show collegue call
            show zilang neutral
            "[[PINT] Why are you being an ass when you're already late?"
            hide collegue
            "{i}Pint hangs up.{/i}"
            "Man, maybe I shouldn't have said that."
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
    show zilang talk
    "[[ZILANG] You know I can't let you in without your ID."
    show zilang neutral
    show niko talk
    "[[NIKO] Zilang, I just need a temporary badge from the front desk."
    menu entrance0:
        "{i}It's probably not a big deal.{/i}":
            $ n += 1
            show niko neutral
            show cut cctv with dissolve
            "{i}You swipe in Niko.{/i}"
            hide cut cctv with dissolve
            "{i}Niko thanks you with a curt nod and enters.{/i}"
            hide niko
        "{i}It's probably a big deal{/i}":
            show zilang talk
            show niko neutral
            "I...I'm sorry...."
            show niko talk
            "[[NIKO]{i} Sigh.{/i} Figures."
            show zilang neutral
            hide niko
            "{i}Niko leaves to make a call.{/i}"
    "{i}I hope that wasn't a big deal....{/i}"
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
            "Why are they sending me the spending report? Hopefully it's not about overspending on snacks again."
            menu email1:
                "Report to IT":
                    "Gallen's profile picture is a bit odd...I'll forward this to IT just in case."
                    show email
                    jump emailcheck
                "Close and go back":
                    "(Growl) I'll just ask Niko to help me work on this later."
                    show email
                    jump emailcheck
        "the second email":
            $ view += 1
            show email 2
            "(Chuckle) I should send this one to Niko."
            menu email2:
                "Report to IT":
                    "But nice try. Off to IT you go!"
                    show email
                    jump emailcheck
                "Find love now":
                    "{i}Curiosity killed the dog.{/i}"
                    show email
                    jump emailcheck
        "the third email":
            $ view += 1
            "Admin work truly is the most annoying!"
            menu email3:
                "Report to IT":
                    "I'm not opening anything sensitive without a green light from IT."
                    jump emailcheck
                "Close and go back":
                    "But I guess I can work on this...tomorrow..."
                    jump emailcheck
# ---------------------------------
label spill:
    scene bg warehouse with fade
    show zilang neutral
    "{i}You enter the warehouse.{/i}"
# ---------------------------------
# ENDINGS
# ---------------------------------
label ending:
    scene bg apartment night with fade
    show zilang neutral
    "{i}After a long day of work, you arrive home.{/i}"
    if n >= 4:
        jump badending
    elif n >= 1:
        jump neutralending
    else:
        jump goodending
label badending:
    "{i}Due to your horrible practices, you have been fired.{/i}"
    return
label neutralending:
    "{i}You are ok...{/i}"
    return
label goodending:
    show zilang happy
    "{i}Good job, you are a good employee!{/i}"
    return
