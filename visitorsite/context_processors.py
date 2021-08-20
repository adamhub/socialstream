from .models import Settings


def base(request):
    try:
        obj=Settings.objects.filter(status=0).first()
        my_dict = {
            'logo_url': obj.image.url,
        }
    except:
        my_dict = {
            'logo_url': None,
        }
    return my_dict

