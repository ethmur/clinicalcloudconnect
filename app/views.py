from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, HealthProvider, FilePost, ProvidesFor

# Create your views here.
def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	files = FilePost.objects.filter(user=user)
	hps = HealthProvider.objects.filter(pk__in=ProvidesFor.objects.filter(user=user).values("hp"))
	return render(request, 'user_details.html', {'user': user, 'files': files, 'hps': hps})
	
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
	
def user_add_hp(request, pk):
	hps = HealthProvider.objects.all()
	return render(request, 'user_add_hp.html', {'hps': hps})
	
def user_post_add_hp(request, pk):
	user = get_object_or_404(User, pk=pk)
	hp_pk = request.POST.get('hp')
	hp = get_object_or_404(HealthProvider, pk=hp_pk)
	pf = ProvidesFor.objects.create(user=user, hp=hp)
	pf.save()
	return HttpResponse("Success")
	
def hp_detail(request, pk):
	hp = get_object_or_404(HealthProvider, pk=pk)
	users = User.objects.filter(pk__in=ProvidesFor.objects.filter(hp=hp).values("user"))
	return render(request, 'hp_details.html', {'hp': hp, 'users': users})
	
def hp_user_detail(request, pk, upk):
	hp = get_object_or_404(HealthProvider, pk=pk)
	user = get_object_or_404(User, pk=upk)
	files = FilePost.objects.filter(user=user)
	hps = HealthProvider.objects.filter(pk__in=ProvidesFor.objects.filter(user=user).values("hp"))
	if not hp in hps:
		return HttpResponse("Permission Error")
	return render(request, 'hp_user_details.html', {'user': user, 'files': files, 'hps': hps})
	
def hp_user_upload_file(request, pk, upk):
	hp = get_object_or_404(HealthProvider, pk=pk)
	user = get_object_or_404(User, pk=upk)
	hps = HealthProvider.objects.filter(pk__in=ProvidesFor.objects.filter(user=user).values("hp"))
	if not hp in hps:
		return HttpResponse("Permission Error")
	return render(request, 'hp_user_upload_file.html')
	
def hp_user_post_file(request, pk, upk):
	if request.method != 'POST':
		return HttpResponseForbidden('allowed only via POST')
	if request.FILES.__contains__("file") == False:
		return HttpResponseForbidden('need o upload a file, request.FILES looked like this:' + str(request.FILES))
	file = request.FILES['file']
	hp = get_object_or_404(HealthProvider, pk=pk)
	user = get_object_or_404(User, pk=upk)
	hps = HealthProvider.objects.filter(pk__in=ProvidesFor.objects.filter(user=user).values("hp"))
	if not hp in hps:
		return HttpResponse("Permission Error")
	file_post = FilePost(user = user)
	file_post.file.save(file.name, file, save=True)
	return HttpResponse("Success")
