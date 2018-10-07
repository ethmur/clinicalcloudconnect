from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, HealthProvider, FilePost

# Create your views here.
def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	files = FilePost.objects.filter(user=user)
	return render(request, 'user_details.html', {'user': user, 'files': files})
	
def user_upload_file(request, pk):
	return render(request, 'user_upload_file.html')
	
def user_post_file(request, pk):
	if request.method != 'POST':
		return HttpResponseForbidden('allowed only via POST')
	if request.FILES.__contains__("file") == False:
		return HttpResponseForbidden('need o upload a file, request.FILES looked like this:' + str(request.FILES))
	file = request.FILES['file']
	user = get_object_or_404(User, pk=pk)
	file_post = FilePost(user = user)
	file_post.file.save(file.name, file, save=True)
	return HttpResponse("Success")
	
def user_view_file(request, pk, findex):
	user = get_object_or_404(User, pk=pk)
	files = FilePost.objects.filter(user=user)
	file = files[findex]
	
def hp_detail(request, pk):
	hp = get_object_or_404(HealthProvider, pk=pk)
	return render(request, 'hp_details.html', {'hp': hp})
