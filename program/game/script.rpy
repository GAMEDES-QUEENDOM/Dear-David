# Main script for the demo!

define a = Character("Adam")
define d = Character("David")

# NVL characters are used for the phone texting
define a_nvl = Character("Adam", kind=nvl, image="adam", callback=Phone_SendSound)
define e_nvl = Character("Eve", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#Skip the main menu
label main_menu:
    return

label start:
    pause 1.0
    scene apt door
    with fade
    pause 0.5

    scene apt door transp
    show adam
    "So this is my new apartment."
    "It's different from what I'm used to...oh well."
    show adam happy
    "Here's to a new chapter of my life."

    pause 1.0
    scene bedroom
    with fade
    pause 1.0

    scene bedroom transp
    show adam
    with moveinleft

    "This place is old, but nice."
    "Hope I can get some work done here."

    scene bedroom
    pause 1.0

    scene bedroom transp
    show adam at left

    a "...Huh?"
    "That's weird..."
    show adam anxious
    a "Why does it feel so cold all of the sudden?"
    a "The windows are close..."
    a "There shouldn't be any wind coming through it."
    a "..."
    show adam
    a "It's probably my imagination."
    a "Guess the move has taken a toll on me."

    #change scene to bedroom with things
    scene bedroom
    with fade
    pause 1.0
    #unpacking background noises
    "And that's the last of it."
    "I'm finally done unpacking. Finally, I can rest."

    #phone ringtone sound effect
    "Hmm? That was my phone."
    show adam phone at left
    with ease

    #Phone conversation start
    nvl_narrator "You have a new message"
    e_nvl "Hey babe!"
    e_nvl "Did you arrive at your place?"
    a_nvl "Hey."
    a_nvl "Yeah, I just finished unpacking."
    e_nvl "That was quick"
    e_nvl "So how's the apartment?"
    nvl_narrator ""

    menu (nvl=True):
        "Something's weird":
            a_nvl "Well...something weird happened."
            e_nvl "What happened? Is everything okay?"
            a_nvl "I don't know..."
            a_nvl "I felt this sudden chill in the room."
            a_nvl "But when I checked the window, it was closed."
            e_nvl "That's strange...maybe a draft?"
            a_nvl "I don't think that's it."
            a_nvl "But who knows, it must be my imagination."
            pass
        "It's nothing":
            a_nvl "It's alright."
            a_nvl "Just needed a few fixing here and there."
            pass
        #"Test choice 3":
        #    a_nvl "Choice 3"
        #    pass
    
    a_nvl "Anyways, I'm tired from all that unpacking."
    a_nvl "I'm gonna go out and find some place to eat."
    e_nvl "Want to come over at my place?"
    e_nvl "I'll cook something for you! :)"
    a_nvl "Yeah sounds like a plan. I'll head over there now."
    a_nvl "See ya"
    e_nvl "{image=emoji/wave.png}{image=emoji/wave.png}{image=emoji/wave.png}"

    show adam:
        ease 0.5 xalign 0.5 

    a  "To be continued..."

    return
    #$ renpy.quit()

    
#    menu: 
        
 #       "Choice A":
 #           "Dialogue a."
  #          "Dialogue a.."

  #      "Choice B":
   #         "Dialogue b."
   #         "Dialogue b.."

   # scene bedroom
   # "Continue."