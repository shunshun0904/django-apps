#from django.http import HttpResponse
#from test1.forms import KakikomiForm

#def kakikomi(request):
    # f = KakikomiForm()
    # return HttpResponse( f.as_table() )




from django.shortcuts import render_to_response
from test1.forms import KakikomiForm

def kakikomi(request):
     f = KakikomiForm()
     return render_to_response('kakikomiform.html', {'form1': f})
