import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

try:
  with sr.Microphone() as source:
    print('Ouvindo...')
    voice = listener.listen(source)
    info = listener.recognize_google(voice)
    print(info)
except:
  pass

def send_email():
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login('joaoandrad398@gmail.com', 'senhafalsa')
  server.sendmail('joaoandrad398@gmail.com', 'joaovictorvieira.23@hotmail.com', 'Hi Dude make sure you join party on christmas night')