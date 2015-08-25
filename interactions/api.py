import logging
import json

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from interactions.models import Interaction


logger = logging.getLogger(__name__)


@login_required
@require_http_methods(['POST'])
def interaction(request):
    i = Interaction(lti_params=request.LTI, payload=json.loads(request.body))
    i.save()

    return JsonResponse({'success': True})
