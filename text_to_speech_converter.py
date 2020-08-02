from gtts import gTTS 
from playsound import playsound

def text_to_speech(text_to_convert):

    # Language in which you want to convert 
    language = 'en'
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed 
    myobj = gTTS(text=text_to_convert, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome 
    myobj.save("audio_clip.mp3") 

    #play the saved mp3
    playsound('audio_clip.mp3')



