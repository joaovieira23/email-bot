import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
  engine.say(text)
  engine.runAndWait()

def get_info():
  try:
    with sr.Microphone() as source:
      print('Ouvindo...')
      voice = listener.listen(source)
      info = listener.recognize_google(voice)
      print(info)
      return info.lower()
  except:
    pass

def send_email(receiver, subject, message):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login('joaoandrad398@gmail.com', 'senhafalsa')
  email = EmailMessage()
  email['From'] = 'joaoandrad398@gmail.com'
  email['To'] = receiver
  email['Subject'] = subject
  email.set_content(message)
  server.send_message(email)

email_list = {
  'black': 'joaovictorvieira.23@hotmail.com',
  'test': 'teste@gmail.com',
  'programming': 'support@programming.com',
  'lisa': 'lisa22@gmail.com',
  'pink': 'pink123@teste.com.br'
}

def get_email_info():
  talk('Para quem você deseja enviar o e-mail?')
  name = get_info()
  receiver = email_list[name]
  print(receiver)
  talk('Qual é o assunto do seu e-mail?')
  subject = get_info()
  talk('Diga-me o próximo em seu e-mail')
  message = get_info()

  send_email(receiver, subject, message)
  talk('Ei preguiçoso. Seu email foi enviado')
  talk('Quer enviar mais email?')

get_email_info()