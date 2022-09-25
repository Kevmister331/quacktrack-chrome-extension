# Hackathon

# Constants
MAX_LEISURE_TIME = 30
ANNOYED_VALUE = 2
ANGRY_VALUE = 3

# Data set
data = {

}

# Allowed websites
allowedWebsites = {
    "canvas" : 0,
    "khan academy" : 0,
    "edx" : 0
}

# Too much time spent on these websites
tooMuchTime = []

# Analysis
print("Quack. Welcome to QuackTrack!")
print("Here are your results for this study session: ")


# Analyze results
for key, value in data.items():
    print(key, ":", value, "minutes")
    
for key, value in data.items():
    if value > MAX_LEISURE_TIME and key not in allowedWebsites:
        tooMuchTime.append(key)

# Response
if len(tooMuchTime) >= ANNOYED_VALUE:
    tooMuchTime.insert(-1, "and")
    print("Nice going, but you spent too much time on", ' '.join(tooMuchTime), "!")
    print("""
                  .-""-.
                 /      \
                /     (0 \______
                |         "_____)
                \        ,-----'
                 \_    _/
                  /    \
                 /      \
                /        \
               /          \
              /        :   |
             /     ;   :   |
    \\\     /  _.-'    :   |
     \\\\  / _'        :   |
      \\\\/ ;         :   /
       \\  ;         :   /
        \   `._`-'_.'  _/
         \     ''' _.-'
          \      / /
           \    / /
            \  /)(_______
             )(_________<
            (__________<
    
    """)
    print("You made me stand up")
    
elif len(tooMuchTime) >= ANGRY_VALUE:
    print("""
    
               ,-.
           ,--' ~.).
         ,'         `.
        ; (((__   __)))
        ;  ( (#) ( (#)
        |   \_/___\_/|
       ,"  ,-'    `__".
      (   ( ._   ____`.)--._        _
       `._ `-.`-' \(`-'  _  `-. _,-' `-/`.
        ,')   `.`._))  ,' `.   `.  ,','  ;
      .'  .     `--'  /     ).   `.      ;
     ;     `-        /     '  )         ;
     \                       ')       ,'
      \                     ,'       ;
       \               `~~~'       ,'
        `.                      _,'
          `.                ,--'
            `-._________,--'
                    """)
    print("STOP DUCKIN' AROUND")

elif len(tooMuchTime) == 0:
    print("""
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------    
    """)
    print("Hmm, looks like there was no information...")
    
else:
    print("""
    
            ,----,
       ___.`      `,
       `===  D     :
         `'.      .'
            )    (                   ,
           /      \_________________/|
          /                          |
         |                           ;
         |               _____       /
         |      \       ______7    ,'
         |       \    ______7     /
          \       `-,____7      ,'   
    ^~^~^~^`\                  /~^~^~^~^
      ~^~^~^ `----------------' ~^~^~^
     ~^~^~^~^~^^~^~^~^~^~^~^~^~^~^~^~

    """)
    print("Good job, keep it up!")