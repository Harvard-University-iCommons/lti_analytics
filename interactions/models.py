import logging

from django.db import models
from django.utils import timezone

from django_pgjson.fields import JsonBField


logger = logging.getLogger(__name__)


class Interaction(models.Model):
    lti_params = JsonBField()
    payload = JsonBField()
    date_created = models.DateTimeField(default=timezone.now)
