# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Zilang")
define right85 = Position(xalign=0.85)

# The game starts here.

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

    jump zilangintro

label zilangintro:
    scene bg breakfast with fade

    e "Hi there I don't know what I'm doing here."
    show zilang normal at right85
    e "I guess I'll think of something to do"
    e "Nevermind bye."

    return
