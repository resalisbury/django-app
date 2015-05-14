import json

from django.db import models
from django.core.files import File


def get_new_file_name(instance, filename):
    return '/'.join(['chatJSON', 'chat-v' + str(instance.version) + '.json'])


class ChatJSON(models.Model):
    script = models.FileField(upload_to=get_new_file_name)
    version = models.DecimalField(max_digits=6, decimal_places=2, unique=True)

    def __str__(self):
        return 'Chat v-%s' % str(self.version)

    def script_as_json(self):
        with open(self.script.path) as data_file:
            data = json.load(data_file)
        return data
