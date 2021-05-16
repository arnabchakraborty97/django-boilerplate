from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def handle_404(request, exception):
	return render(request, 'dashboard/404.html', status=404)

def handle_500(request):
	return render(request, 'dashboard/500.html', status=500)