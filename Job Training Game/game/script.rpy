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
#################################
label start:
    scene bg corpo:
        zoom 4
    "Welcome to the ARF Information and Security Awareness Training."
    "This orientation is essential for understanding the critical role of confidentiality and secure practices within our operations."
    "Here, we don’t just protect people from animals and animals from people; we protect our knowledge, our methods, and our secrets from those who might exploit them."
    "Failure to comply with these standards could jeopardize not only your role but also the lives of our agents, our allies, and the people we serve."
    show zilang normal at right85
    "In this training simulation, you will assume the role of one of our esteemed field agents, Zilang, who is tasked with balancing the physical and digital aspects of animal containment and information security."
    "Through the course of a typical workday, your decisions will shape his effectiveness and assess his readiness to uphold the integrity and confidentiality of ARF."
################################
label intro0:
    scene bg breakfast with fade
    e "Yawnnn good morning"
    show zilang normal at right85
    e "Help me pick my breakfast"
    menu c_intro:
        "2 pieces of animal crackers":
            e "Mmm cannibalism!"
        "1 cup of yogurt":
            e "So cold..."
    e "Well, that's breakfast I guess!"
    "News start playing on his phone."
    news "Ding ding ding, reports of information breach has happened. Be safe!"
    e "Well, time to head off!"
################################
label travel0:
    show bg travel with fade:
        zoom 4
    "Ring ring ring. A phone call occurs."
    e "Who is this?"
    coll "Yo Zilang! I need info on X client. Can you tell me their X number right?"
    menu c_travel:
        "Discuss confidential details":
            e "Sure, boss. The containment procedures involve exactly…"
            coll "Ok thanks Zilang!"
            "The caller hangs up. You notice NPCs staring at you."
        "Wait until office arrival":
            e "I'll give you the full rundown when I get to the secure line."
            coll "Understandable have a nice day."
################################
label entrance0:
    show bg entrance with fade:
        zoom 4
    "You arrive at the office."
    u "Hey Zilang what's up?"
    e "Hi"
    u "Can you let me in?"
    menu c_entrance:
        "Sure, happens to the best of us.":
            u "Thanks man you're the best."
        "Sorry, only ID'd personnel are allowed. Better safe than sorry.":
            u "Gee that's kind of an ass move."
    e "Well, there's that I guess."
################################
label email0:
    show bg office1 with fade
    "You receive an email."
    "[[picture thingy]"
    menu c_email:
        "Click link":
            e "Uh-oh. That wasn't IT."
        "Ignore email":
            e "Annoying spam."
        "Report phishing":
            "IT" "CONGRATS FOR NOT FALLING FOR THIS I GUESS LOL"
################################
label confinfo0:
    show bg office2 with fade:
        zoom 0.9
    "Now it's time to identify different levels of confidentiality."
    "What kinda info is this scenario?"
    menu c_confinfo:
        "Company secret":
            "WRONG"
            jump c_confinfo
        "Top secret":
            "CORRECT"
        "Confidential information":
            "WRONG"
            jump c_confinfo
    "Good job."
################################
label ending:
    show bg home with fade:
        zoom 1
    "Zilang's choices lead to a breach, resulting in \"Critical Incident Report.\""