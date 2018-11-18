# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class menu(models.Model):
	titulo = models.CharField(max_length=10)
	url = models.TextField()
	#time = models.DateTimeField()
