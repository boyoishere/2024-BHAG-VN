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
    scene bg corpo:
        zoom 4
    show presenter normal
    "[[ARF CEO] Welcome to the ARF Information and Security Awareness Training."
    "This orientation is essential for understanding the critical role of confidentiality--"
    "--and secure practices within our operations."
    
    "Here, we don't just protect people from animals and animals from people,"
    "we protect our knowledge, our methods, and our secrets from those who might exploit them."
    
    "Failure to comply with these standards could jeopardize not only your role--"
    "--but also the lives of our agents, our allies, and the people we serve."
    hide presenter normal
    show zilang normal
    "In this training simulation, you will assume the role of one of our field agents, Zilang,"
    
    "who is tasked with balancing the physical and digital aspects of information security today."
    
    "Through the course of a typical workday, your decisions will shape his effectiveness--"
    "--and assess his readiness to uphold the integrity and confidentiality of ARF."
################################ 1
label intro:
    scene bg breakfast with fade
    "[[ZILANG] (Yawning) So early..."
    show zilang normal at right85
    "What should I eat for breakfast today?"
    menu intro0:
        "2 pieces of animal crackers":
            "Mmm cannibalism!"
        "1 cup of yogurt":
            "So cold..."
    "Well, that's breakfast I guess!"
    "{i}You check the news.{/i}"
    news "[[NEWS ANCHOR] Reports of information breach has happened. Be safe!"
    "Well, time to head off!"
################################ 2
label travel:
    show bg travel with fade:
        zoom 4
    "(Ringtone)"
    "Who is this?"
    coll "[[Collegue] Yo Zilang! I need info on X client. Can you tell me their X number right?"
    menu travel0:
        "Discuss confidential details":
            "Sure, boss. The containment procedures involve exactly…"
            coll "Ok thanks Zilang!"
            "{i}The caller hangs up. You notice NPCs staring at you.{/i}"
        "Wait until office arrival":
            "I'll give you the full rundown when I get to the secure line."
            coll "[[Collegue] Understandable have a nice day."
################################ 3
label entrance:
    show bg entrance with fade:
        zoom 4
    "{i}You arrive at the office.{/i}"
    u "Hey Zilang what's up?"
    "Hi"
    u "Can you let me in?"
    menu entrance0:
        "Sure, happens to the best of us.":
            u "Thanks man you're the best."
        "Sorry, only ID'd personnel are allowed. Better safe than sorry.":
            u "Gee that's kind of an ass move."
    "Well, there's that I guess."
################################ 4
label email:
    show bg office1 with fade
    "You receive an email."
    "[[picture thingy]"
    menu email0:
        "Click link":
            "Uh-oh. That wasn't IT."
        "Ignore email":
            "Annoying spam."
        "Report phishing":
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
            jump confinfo
        "Top secret":
            "CORRECT"
        "Confidential information":
            "WRONG"
            jump confinfo
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