from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .inference.model import recognize
from .inference.model import classifier
import pyttsx3 

# Create your views here.

file_path = "D:/Stud/AI/programs and projects/Numera - MNIST classifier/saved_image/Hello.jpeg"
def index(request):
    return render(request, TemplateView.as_view(template_name = 'index.html'))

def numera(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',160)
    engine.say(audio)
    engine.runAndWait()

def recog(request):

    result = recognize(file_path)
    print(result)
    numera("The number   you have written is:"+str(result))
    mydict = {"recognized":"Possibilites: "+str(result)}
    return render(request, 'index.html',mydict)


