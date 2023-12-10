from django.db import models


class Template(models.Model):
    html_block = models.TextField()
    ex_id = models.TextField(max_length=3)

    def __str__(self):
        return f'template_id: {self.ex_id}'
