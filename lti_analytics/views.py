from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse
from django.shortcuts import render

from ims_lti_py.tool_config import ToolConfig


def lti_auth_error(request):
    raise PermissionDenied


@require_http_methods(['GET'])
def tool_config(request):
    url = "%s://%s%s" % (request.scheme, request.get_host(), reverse('lti_launch', exclude_resource_link_id=True))
    lti_tool_config = ToolConfig(
        title='LTI Analytics Example',
        launch_url=url,
        secure_launch_url=url,
        description="Example LTI tool for recording LTI tool interactions."
    )

    # this is how to tell Canvas that this tool provides a course navigation link:
    course_nav_params = {
        'enabled': 'true',
        'text': 'LTI Analytics Example',
        'default': 'disabled',
        'visibility': 'members',
    }
    lti_tool_config.set_ext_param('canvas.instructure.com', 'course_navigation', course_nav_params)
    lti_tool_config.set_ext_param('canvas.instructure.com', 'privacy_level', 'public')

    return HttpResponse(lti_tool_config.to_xml(), content_type='text/xml')


@login_required
@require_http_methods(['POST'])
@csrf_exempt
def lti_launch(request):
    return render(request, 'lti_analytics/example.html', {})
