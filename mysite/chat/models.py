from django.db import models


def new_file_name(instance, filename):
    return '/'.join(['chatJSON', 'chat-v' + str(instance.version) + '.json'])


class ChatJSON(models.Model):
    script = models.FileField(upload_to=new_file_name)
    version = models.DecimalField(max_digits=6, decimal_places=2, unique=True)

    def __str__(self):
        return 'Chat v-%s' % str(self.version)
