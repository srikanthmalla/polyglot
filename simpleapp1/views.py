from django.shortcuts import render#render on request
from django.http import HttpResponseRedirect # http redirect
from django.contrib import auth#login authentication model
from django.core.context_processors import csrf #cross site ref forgery
from django.contrib.auth.forms import UserCreationForm
from os import path
from django.http import HttpResponseForbidden,HttpResponse
from django.core.urlresolvers import reverse

#for voice to text thing
from scipy.io.wavfile import read
import speech_recognition as sr
import datetime


def subs(request):
	WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "test.wav")
	# (fs,w_file)=read("test.wav")#this is to do operations on that wav file
	# use "test.wav" as the audio source
	offset=28
	duration=5
	r = sr.Recognizer()
	with sr.WavFile(WAV_FILE) as source:
	    audio = r.record(source,duration,offset) # read the entire WAV file

	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    print("Google Speech Recognition thinks you said " + r.recognize_google(audio,language="en-US"))
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return render(request,"subs.html",{'subtitles':r.recognize_google(audio,language="en-US")})
def home(request):
	return render(request,"login.html",{'subtitles': datetime.datetime.now()})
def login(request):
	return render(request,'test.html')
def auth_view(request):
	username= request.POST.get("username","")
	password= request.POST.get("password","")
	user =auth.authenticate(username=username,password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')
def logout(request):
	auth.logout(request)
	return render(request,'logout.html')
def loggedin(request):
	return render(request,'loggedin.html',{'full_name':request.user.username})
def invalid_login(request):
	return render(request,'invalid_login.html')
def register_user(request):
	if request.method =='POST':
		form =UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	args={}
	args.update(csrf(request))
	args['form']=UserCreationForm
	return render(request,'register.html',args)
def register_success(request):
	return render(request,'register_success.html')

def upload_pic(request):
	for count,x in enumerate(request.FILES.getlist("files")):
		def process(f):
			with open('/home/malla/Documents/webclass/media/file_'+str(count), 'wb+') as destination:
				for chunk in f.chunks():
					destination.write(chunk)
		process(x)
	return HttpResponse("File(s) uploaded!")

def upload(request):
	return render(request,'upload.html',{})