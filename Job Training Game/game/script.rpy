#################################
# Author: Boyo
# A parody job training game, mostly for the purpose of learning RenPy
# This is Boyo's BHAG 2024
#################################
# Characters
define e = Character("Zilang")
define news = Character("Reporter")
define coll = Character("Collegue")
define u = Character("Unknown")

# Utility
define right85 = Position(xalign=0.85)
################################# 0
label start:
    scene bg corpo
    show presenter normal
    show logo
    "[[ARF CEO] Welcome to the ARF Information and Security Awareness Training."
    # jump intro #!!!!!!!!!!!
    "This orientation is essential for understanding the critical role of confidentiality--"
    "--and secure practices within our operations."
    
    "Here, we don't just protect people from animals and animals from people,"
    "we protect our knowledge, our methods, and our secrets from those who might exploit them."
    
    "Failure to comply with these standards could jeopardize not only your role--"
    "--but also the lives of our agents, our allies, and the people we serve."
    hide presenter normal
    show zilang avatar at center
    "In this training simulation, you will assume the role of one of our field agents, Zilang,"
    
    "who is tasked with balancing the physical and digital aspects of information security today."
    
    "Through the course of a typical workday, your decisions will shape his effectiveness--"
    "--and assess his readiness to uphold the integrity and confidentiality of ARF."
################################ 1
label intro:
    scene bg apartment with fade
    "[[ZILANG] (Yawning) Good morning world..."
    show zilang neutral
    # jump email #!!!!!!!!!!!
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
################################ 2
label travel:
    show bg travel with fade
    "(Ringtone) {i}You receive a call from your coworker, Pint.{/i}"
    show collegue call
    "[[PINT] Zilang, where are you? The client is waiting."
    "[[ZILANG] Sorry, I'm on my way. I'll be there in 20."
    "[[PINT] Ok... Do you still rememeber her case number?"
    hide collegue call
    hide zilang neutral
    menu travel0:
        "Tell him":
            show cut call with dissolve
            "[[ZILANG] You can find it in the open catalog. It was H23-something..."
            hide cut call with dissolve
            show collegue call
            show zilang neutral
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
################################ 3
label entrance:
    show bg entrance with fade
    "{i}You arrive at the office.{/i}"
    show niko talk
    "[[NIKO] Took you long enough."
    show zilang talk
    show niko neutral
    "[[ZILANG] What are you doing out here? Don't you have to be at that meeting?"
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
            "{i}You swipe in Niko.{/i}"
            "{i}Niko thanks you with a curt nod and enters.{/i}"
            hide niko
            show cut cctv
        "{i}Would management see this?{/i}":
            "I...I'm sorry...."
            "[[NIKO]{i} Sigh.{/i} Figures."
            hide niko
            "{i}Niko leaves to make a call.{/i}"
    "{i}I hope that wasn't a big deal....{/i}"
################################ 4
label email:
    hide cut cctv
    show bg office1 with fade
    "{i}You arrive at your desk.{/i}"
    "{i}You check your email. You click on-{/i}"
    menu email0:
        "The first email":
            show email 1
            "Not the snack bills again..."
            hide email 1
        "The second email.":
            show email 2
            "Annoying spam."
        "The third email.":
            "IT" "CONGRATS FOR NOT FALLING FOR THIS I GUESS LOL"
################################ 5
label confinfo:
    show bg office2 with fade:
        zoom 0.9
    "Now it's time to identify different levels of confidentiality."
    "What kinda info is this scenario?"
    menu confinfo0:
        "Company secret":
            "WRONG"
            jump confinfo0
        "Top secret":
            "CORRECT"
        "Confidential information":
            "WRONG"
            jump confinfo0
    "Good job."
################################ 6
# label exist:
#     show bg entrance with fade:
#         zoom 4
#     "You arrive at the office."
#     u "Hey Zilang what's up?"
#     "Hi"
#     u "Can you let me in?"
#     menu exit:
#         "Sure, happens to the best of us.":
#             u "Thanks man you're the best."
#         "Sorry, only ID'd personnel are allowed. Better safe than sorry.":
#             u "Gee that's kind of an ass move."
#     "Well, there's that I guess."
################################ 7
label ending:
    show bg home with fade:
        zoom 1
    "Zilang's choices lead to a breach, resulting in \"Critical Incident Report.\""