# import random

def song_picker(genre):
    rap_songs = [
    {"name":"The London", "artist":"Young Thug feat. J. Cole Travis Scott", "song":'https://www.youtube.com/watch?v=rxz-PqlVa78'}, {"name":"Sunset", "artist":"J.Cole & Young Nudy", "song":"https://www.youtube.com/watch?v=PztawW00gjM"}, {"name":"Marvelous Day", "artist":"Kap G feat. Lil Uzi Vert & Gunna", "song":"https://www.youtube.com/watch?v=XCVr1aOnpL4"}
    ]
    pop_songs = [
    {"name":"Ransom", "artist":"Lil Tecca", "song":"https://www.youtube.com/watch?v=ycT5jr9W8L0"}, {"name":"Neon Guts", "artist":"Lil Uzi Vert feat. Pharrell", "song":"https://www.youtube.com/watch?v=XBdso9eWf3Q"}, {"name":"Sweet but Psycho", "artist":"Ava Max", "song":"https://www.youtube.com/watch?v=2KBFD0aoZy8"}
    ]
    randb_songs = [     
    {"name":"No Guidance", "artist":"Chris Brown ft. Drake", "song":"https://www.youtube.com/watch?v=6L_k74BOLag"}, {"name":"Let Me Love You", "artist":"Mario", "song":"https://www.youtube.com/watch?v=H64QG4UsrGI"} 
    ]
    trap_songs = [
    {"name":"Welcome ToThe Party", "artist":"Pop Smoke", "song":'https://www.youtube.com/watch?v=b5hwEMxVZME'}    
        ]
    rock_songs = [
    {"name":"Manhattan", "artist":"King of Leon", "song":"https://www.youtube.com/watch?v=a6BOO4G-jV4"}
        ]
    alternative_songs = [
    {"name":"Us and Them", "artist":"Pink Floyd", "song":"https://www.youtube.com/watch?v=nDbeqj-1XOo"}
        ]
    classical_songs = [
    {"name":"Always Too Late", "artist":"Benjamin Monday", "song":"https://www.youtube.com/watch?v=cvO07tkdcpE&list=PLTf9AtDNwOb40PFfI7w9cm-Psg3A-QxL2&index=3&t=0s"},     
        ]
    country_songs = [
    {"name":"Beautiful Crazy", "artist":"Luke Combs", "song":"https://www.youtube.com/watch?v=rItv9i6c7AY"}, {"name":"Take Me Home, Country Roads", "artist":"John Denver", "song":"https://www.youtube.com/watch?v=1vrEljMfXYo"}, 
        ]
    
    workout_songs = [
    {"name":"Humble", "artist":"Kendrick Lamar feat. Skrillex", "song":"https://www.youtube.com/watch?v=Na1DcaBsQG4"}, {"name":"List of Demands", "artist":"Saul Williams", "song":"https://www.youtube.com/watch?v=sXzK0AFpmcI"}, {"name":"The Greatest", "artist":"Sia feat. Kendrick Lamar", "song":"https://www.youtube.com/watch?v=wdOjAS_iJV0"}        ]
    soul_songs = [
    {"name":"Super Freak", "artist":"Ricc James", "song":"https://www.youtube.com/watch?v=QYHxGBH6o4M"}    
        ]
    indie_songs = [
    {"name":"Sail", "artist":"Awolnation", "song":"https://www.youtube.com/watch?v=tgIqecROs5M"} 
        ]
    folkandacoustic_songs = [
    {"name":"Sapphire", "artist":"Diamond Thug", "song":"https://www.youtube.com/watch?v=PULt2INORys"}   
        ]
    jazz_songs = [
    {"name":"Blue In Green", "artist":"Miles Davis", "song":"https://www.youtube.com/watch?v=PoPL7BExSQU"}   
        ]
    christian_songs = [
    {"name":"I Can Only Imagine", "artist":"MercyMe", "song":"https://www.youtube.com/watch?v=B9vx4kP7X-k"},
        ]
    kidsandfamily_songs = [
    {"name":"Havana", "artist":"KIDZ BOP Kids", "song":"https://www.youtube.com/watch?v=8OXf3ufjOsM&list=PLgr4jAFvG97CiDd5ybZsLYNkDrLBOYBhE"},     
        ]

    
    if genre == "Rap":
        # random.shuffle(rap_songs)
        return(rap_songs[0])          
    
    elif genre == "Pop":
        # random.shuffle(pop_songs)
        return(pop_songs[0])     
        
    elif genre == "R&B":
        # random.shuffle(randb_songs)
        return(randb_songs[0])
        
    elif genre == "Trap":
        # random.shuffle(trap_songs)
        return(trap_songs[0])   
        
    elif genre == "Rock":
        # random.shuffle(rock_songs)
        return(rock_songs[0])   
        
    elif genre == "Alternative":
        # random.shuffle(alternative_songs)
        return(alternative_songs[0])  
        
    elif genre == "Classical":
        # random.shuffle(classical_songs)
        return(classical_songs[0])   
        
    elif genre == "Country":
        # random.shuffle(country_songs)
        return(country_songs[0])   
        
    elif genre == "Workout":
        # random.shuffle(workout_songs)
        return(workout_songs[0])   
        
    elif genre == "Soul":
        # random.shuffle(soul_songs)
        return(soul_songs[0])   
        
    elif genre == "Indie":
        # random.shuffle(indie_songs)
        return(indie_songs[0])   
        
    
    
# import random
def all_songs(genre):
    rap_songs = [
    {"name":"The London", "artist":"Young Thug feat. J. Cole Travis Scott", "song":'https://www.youtube.com/watch?v=rxz-PqlVa78', "pic":"static/assets/resultimages/The_London.png"}, {"name":"Sunset", "artist":"J.Cole & Young Nudy", "song":"https://www.youtube.com/watch?v=PztawW00gjM", "pic":"static/assets/resultimages/sunset.jpg"}, {"name":"Marvelous Day", "artist":"Kap G feat. Lil Uzi Vert & Gunna", "song":"https://www.youtube.com/watch?v=XCVr1aOnpL4","pic":"static/assets/resultimages/marvelousDay.jpg"}
    ]
    pop_songs = [
    {"name":"Ransom", "artist":"Lil Tecca", "song":"https://www.youtube.com/watch?v=ycT5jr9W8L0","pic":"static/assets/resultimages/Ransom.jpg"}, {"name":"Neon Guts", "artist":"Lil Uzi Vert feat. Pharrell", "song":"https://www.youtube.com/watch?v=XBdso9eWf3Q","pic":"static/assets/resultimages/neonguts.jpg"}, {"name":"Sweet but Psycho", "artist":"Ava Max", "song":"https://www.youtube.com/watch?v=2KBFD0aoZy8","pic":"static/assets/resultimages/sweet.png"}
    ]
    randb_songs = [     
    {"name":"No Guidance", "artist":"Chris Brown ft. Drake", "song":"https://www.youtube.com/watch?v=6L_k74BOLag","pic":"static/assets/resultimages/no.png"}, {"name":"Let Me Love You", "artist":"Mario", "song":"https://www.youtube.com/watch?v=H64QG4UsrGI","pic":"static/assets/resultimages/let.jpg"} 
    ]
    trap_songs = [
    {"name":"Welcome ToThe Party", "artist":"Pop Smoke", "song":'https://www.youtube.com/watch?v=b5hwEMxVZME',"pic":"static/assets/resultimages/welcome.jpg"}  
        ]
    rock_songs = [
    {"name":"Manhattan", "artist":"King of Leon", "song":"https://www.youtube.com/watch?v=a6BOO4G-jV4"}
        ]
    alternative_songs = [
    {"name":"Us and Them", "artist":"Pink Floyd", "song":"https://www.youtube.com/watch?v=nDbeqj-1XOo"}
        ]
    classical_songs = [
    {"name":"Always Too Late", "artist":"Benjamin Monday", "song":"https://www.youtube.com/watch?v=cvO07tkdcpE&list=PLTf9AtDNwOb40PFfI7w9cm-Psg3A-QxL2&index=3&t=0s"},     
        ]
    country_songs = [
    {"name":"Beautiful Crazy", "artist":"Luke Combs", "song":"https://www.youtube.com/watch?v=rItv9i6c7AY"}, {"name":"Take Me Home, Country Roads", "artist":"John Denver", "song":"https://www.youtube.com/watch?v=1vrEljMfXYo"}, 
        ]
    
    workout_songs = [
    {"name":"Humble", "artist":"Kendrick Lamar feat. Skrillex", "song":"https://www.youtube.com/watch?v=Na1DcaBsQG4"}, {"name":"List of Demands", "artist":"Saul Williams", "song":"https://www.youtube.com/watch?v=sXzK0AFpmcI"}, {"name":"The Greatest", "artist":"Sia feat. Kendrick Lamar", "song":"https://www.youtube.com/watch?v=wdOjAS_iJV0"}        ]
    soul_songs = [
    {"name":"Super Freak", "artist":"Ricc James", "song":"https://www.youtube.com/watch?v=QYHxGBH6o4M"}    
        ]
    indie_songs = [
    {"name":"Sail", "artist":"Awolnation", "song":"https://www.youtube.com/watch?v=tgIqecROs5M"} 
        ]
    folkandacoustic_songs = [
    {"name":"Sapphire", "artist":"Diamond Thug", "song":"https://www.youtube.com/watch?v=PULt2INORys"}   
        ]
    jazz_songs = [
    {"name":"Blue In Green", "artist":"Miles Davis", "song":"https://www.youtube.com/watch?v=PoPL7BExSQU"}   
        ]
    christian_songs = [
    {"name":"I Can Only Imagine", "artist":"MercyMe", "song":"https://www.youtube.com/watch?v=B9vx4kP7X-k"},
        ]
    kidsandfamily_songs = [
    {"name":"Havana", "artist":"KIDZ BOP Kids", "song":"https://www.youtube.com/watch?v=8OXf3ufjOsM&list=PLgr4jAFvG97CiDd5ybZsLYNkDrLBOYBhE"},     
        ]

    
    if genre == "Rap":
        # random.shuffle(rap_songs)
        return(rap_songs)          
    
    elif genre == "Pop":
        # random.shuffle(pop_songs)
        return(pop_songs)     
        
    elif genre == "R&B":
        # random.shuffle(randb_songs)
        return(randb_songs)
        
    elif genre == "Trap":
        # random.shuffle(trap_songs)
        return(trap_songs)   
        
    elif genre == "Rock":
        # random.shuffle(rock_songs)
        return(rock_songs)   
        
    elif genre == "Alternative":
        # random.shuffle(alternative_songs)
        return(alternative_songs)  
        
    elif genre == "Classical":
        # random.shuffle(classical_songs)
        return(classical_songs)   
        
    elif genre == "Country":
        # random.shuffle(country_songs)
        return(country_songs)   
        
    elif genre == "Workout":
        # random.shuffle(workout_songs)
        return(workout_songs)   
        
    elif genre == "Soul":
        # random.shuffle(soul_songs)
        return(soul_songs)   
        
    elif genre == "Indie":
        # random.shuffle(indie_songs)
        return(indie_songs)   
        
    