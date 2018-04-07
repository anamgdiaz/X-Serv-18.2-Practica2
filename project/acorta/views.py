from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from acorta.models import urls_mod

# Create your views here.

@csrf_exempt

def shortener(request):
	if request.method == "GET":
		url_list = urls_mod.objects.all()
		if urls_mod.objects.all().exists():
			ans = "Url acortadas:<br/>" 
			for i in url_list:
				ans +=  str(i.id) + " su url larga es " + str(i.url_long) + '<br/>'
		else:
			ans = "No hay urls en la base de datos"

		ans += """
				<form action="" method="POST">
				Introduce url para acortar: <input type="text" name="url_long">
				<input type="submit" value="Enviar">
				</form>
				"""
		return HttpResponse(ans)
	elif request.method == "POST":
		url = request.POST['url_long']
		if url.find("http") == -1:	
			print("No empieza por HTTP") 
			body = "http://" + url 
		else:						
			print("Empieza por HTTP")
			body = url
		url_list = urls_mod.objects.all()
		if body in url_list:
			url_short = urls_mod.objects.get(url_long = body)
			url_short = url_short.id
			shortener = True
		else:
			url_new = urls_mod(url_long = body)
			url_new.save()
			url_short = url_new.id
		ans = "Url acortada:" + str(url_short) + " su url larga es " + str(body)
		return HttpResponse(ans)
	else:
		return HttpResponse('Method not allowed',status = 405)

def redirection(request,number):
	try:
		body = urls_mod.objects.get(id=number).url_long
		return HttpResponseRedirect(body)
	except urls_mod.DoesNotExist:
		ans = "La url corta se encuentra indisponible"
		return HttpResponse(ans)




