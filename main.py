# Hackathon

# Constants
MAX_LEISURE_TIME = 30
ANNOYED_VALUE = 2
ANGRY_VALUE = 3

# Data set 4 -> a student who slacked off
data = {
    "canvas" : 60,
    "khan academy" : 40,
    "youtube" : 500,
    "netflix" : 300,
    "edx" : 0,
    "twitter" : 80,
    "instagram" : 70
}

# Allowed websites 4
allowedWebsites = {
    "canvas" : 0,
    "khan academy" : 0,
    "edx" : 0
}

# Too much time spent on these websites
tooMuchTime = []

# Analysis
print("Quack. Welcome to Quack Track")
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
      ,~~.
     (  9 )-_,
(\___ )=='-'
 \ .   ) )
  \ `-' /
   `~j-'   
     "=:
    """)
    print("You made me stand up 🧍😠️")
    
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
    print("STOP DUCKIN' AROUND 😡😡😡🦆🦆🦆")

elif len(tooMuchTime) == 0:
    print("""
                  _      _      _
               __(.)< __(.)> __(.)=
               \___)  \___)  \___)    
    """)
    print("Hmm, looks like there was no information...🤔")
    
else:
    print(""" __
             <(o )___
              ( ._> /
               `---'   
    """)
    print("Good job, keep it up 😛!")