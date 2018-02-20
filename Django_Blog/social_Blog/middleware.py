from django.conf import settings
from django.http import HttpResponse
from django.core.urlresolvers import reverse

class AdminMiddleware():
    def process_request(self,request):
        if not request.user.is_authenticated():
            if True:
                return HttpResponse("aaaaaaa")
            else:
                return HttpResponse("khaled")


