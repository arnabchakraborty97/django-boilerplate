from django.conf import settings

def settings_values(request):
	settings_dict = {
		'APP_ENV': settings.APP_ENV,
		'site_host': settings.SITE_HOST
	}
	
	return settings_dict;