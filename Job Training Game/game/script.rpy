#################################
# Author: Boyo
# A parody job training game, mostly for the purpose of learning RenPy
# This is Boyo's BHAG 2024
#################################

define e = Character("Zilang")
define news = Character("Reporter")
define coll = Character("Collegue")

define right85 = Position(xalign=0.85)

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
label zilangintro:
    scene bg breakfast with fade
    e "Yawnnn good morning"
    show zilang normal at right85
    e "Help me pick my breakfast"
menu breakfast:
    "2 pieces of animal crackers":
        e "Mmm cannibalism!"
    "1 cup of yogurt":
        e "So cold..."
label breakfast_common:
    e "Well, that's breakfast I guess!"
    "News start playing on his phone."
    news "Ding ding ding, reports of information breach has happened. Be safe!"
    e "Well, time to head off!"
################################
label travel:
    show bg travel with fade:
        zoom 4
    "Ring ring ring. A phone call occurs."
    e "Who is this?"
    coll "Yo Zilang! I need info on X client. Can you tell me their X number right?"
menu call:
    "Discuss confidential details":
        e "Sure, boss. The containment procedures involve exactly…"
        coll "Ok thanks Zilang!"
        "The caller hangs up. You notice NPCs staring at you."
    "Wait until office arrival":
        e "I'll give you the full rundown when I get to the secure line."
        coll "Understandable have a nice day."
################################