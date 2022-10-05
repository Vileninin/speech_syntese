import gtts
from gtts import gTTS

tts = gTTS("Добро пожаловать в путешествие. Хочешь услышать который час, нажми 1. Если ты мандривник, нажми два.", lang="ru")
tts.save("welcome.mp3")