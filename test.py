

from gtts.tts import gTTS



if __name__ == "__main__":
    tts = gTTS('test a b c d e f g',lang='en')
    tts.save('tts.mp3')
    print('Finished!')