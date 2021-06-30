import urllib, json
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType

from mixer.backend.django import mixer

user=get_user_model()
class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--mixit')

    def handle(self, *args, **options):
        image_list_response = urllib.request.urlopen("https://picsum.photos/v2/list?limit=100")
        data = json.loads(image_list_response.read())
        image_list=[]
        for obj in data: image_list.append(obj['download_url'])
        names=["James", "William", "Evelyn", "Harper", "Mason", "Ella", "Jackson", "Avery", "Scarlett", "Jack", "Eleanor", "Madison", "Ellie", "Wyatt", "Hazel"]
        members=mixer.cycle(15).blend(user,username=(obj for obj in names ),password=mixer.RANDOM)
    
        embeds = mixer.cycle(20).blend('visitorsite.embed',
            slug=mixer.sequence(lambda c: "embd_%s" % c*5),
            width="800",
            link=(obj for obj in ("https://youtu.be/jYgiV4Iz7I0", "", "https://vimeo.com/560708511","https://bixlyinc.medium.com/managed-hosting-what-you-need-to-know-8f8a60b3982","https://www.youtube.com/watch?v=FjHGZj2IjBk", "https://www.youtube.com/watch?v=hj83cwfOF3Y","https://vimeo.com/185335467", "https://vimeo.com/25968068", "https://vimeo.com/137341902", "https://soundcloud.com/interscope/maroon-5-animals", "https://youtu.be/jYgiV4Iz7I0", "", "https://vimeo.com/560708511","https://bixlyinc.medium.com/managed-hosting-what-you-need-to-know-8f8a60b3982","https://www.youtube.com/watch?v=FjHGZj2IjBk", "https://www.youtube.com/watch?v=hj83cwfOF3Y","https://vimeo.com/185335467", "https://vimeo.com/25968068", "https://vimeo.com/137341902", "https://soundcloud.com/interscope/maroon-5-animals" )),
            embed_code=(obj for obj in ("", '<iframe width="70%" height="300" style="margin: 0 auto" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1066575343&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/niallbyrne" title="Niall Byrne" target="_blank" style="color: #cccccc; text-decoration: none;">Niall Byrne</a> · <a href="https://soundcloud.com/niallbyrne/amble" title="Amble" target="_blank" style="color: #cccccc; text-decoration: none;">Amble</a></div>', '', '',  '',  '',  '',  '',  '',  '',"", '<iframe width="70%" height="300" style="margin: 0 auto" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1066575343&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/niallbyrne" title="Niall Byrne" target="_blank" style="color: #cccccc; text-decoration: none;">Niall Byrne</a> · <a href="https://soundcloud.com/niallbyrne/amble" title="Amble" target="_blank" style="color: #cccccc; text-decoration: none;">Amble</a></div>', '', '',  '',  '',  '',  '',  '',  '' )),
            description=mixer.RANDOM,
        )
        embed_post = mixer.cycle(20).blend('visitorsite.post',
                cat=1,
                status=2,
                external_image=(obj for obj in image_list),
                creator=user.objects.first(),
                embed_file=(obj for obj in embeds),
                body=mixer.RANDOM,
                # body=(obj for obj in ("Vivamus luctus imperdiet imperdiet. Nullam quis tincidunt sem. Nam mi leo, sollicitudin ut dui quis, mattis consectetur lacus.", "Pellentesque sit amet venenatis est. Cras metus ligula, ornare ut posuere et, convallis id arcu. Cras congue fermentum eros eget finibus", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc aliquam lectus id metus convallis, id consectetur magna posuere. Donec et lectus tincidunt, porttitor augue non, maximus libero", "Phasellus sed odio felis. In scelerisque lacus at efficitur pharetra.")),
            )
            
        text_post = mixer.cycle(100).blend('visitorsite.post',
                cat=0,
                status=2,
                creator=user.objects.first(),
                body=mixer.RANDOM,
            )
        image_post = mixer.cycle(50).blend('visitorsite.post',
                cat=2,
                status=2,
                external_image=(obj for obj in image_list),
                creator=user.objects.first(),
                body=mixer.RANDOM,
            )
        for e,item in enumerate(range(1,15),0):
            comments = mixer.cycle(20).blend('django_comments.comment',
                    user=members[e],
                    user_name=members[e],
                    content_type=ContentType.objects.get(id=5),
                    object_pk=(obj.pk for obj in embed_post ),
                    site=Site.objects.first(),
                    comment=mixer.RANDOM,
                )
        self.stdout.write(self.style.SUCCESS('Successfully created all fixtures'))

