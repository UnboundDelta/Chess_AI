# So the rate will gonna be 125..
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

'''
    Later used
'''
numbers_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'to':'2', 'for':'4'}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'for', 'to']
# if not voices:
#     print("No voices found")
# else:
#     ans = 125
#     voice_id = 0
#     engine.setProperty('voice', voices[voice_id].id)
#     engine.setProperty('rate', ans)
#     engine.say("Hey there..This is a testing voice")
#     engine.runAndWait()
#     voice_id = 1
#     engine.setProperty('voice', voices[voice_id].id)
#     engine.setProperty('rate', ans)
#     engine.say("Hey there..This is a testing voice")
#     engine.runAndWait()
import speech_recognition as sr
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone(sample_rate=44100) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.pause_threshold = 1
        audio = r.listen(source)

# try:
    print("Recognizing...")   
    query = r.recognize_google(audio, language='en-in')
    query = query.lower()
    print(query)
    querylist = query.split()
    print(querylist)
    
    ans = ''
    for i in querylist:
        if i in letters:
            ans += i
        elif i in numbers_list:
            ans += numbers_dict[i]
        
    print("User said:", ans)
    # except Exception as e:
    #     # print(e)    
    #     print("Say that again please...")  
    #     return "None"

takeCommand()


        