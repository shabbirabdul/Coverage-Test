import os

from models import *
from forms import *

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.contrib.gis.geos import Point
from django.contrib import messages

import mailchimp
from recaptcha.client import captcha

def subscribe(request):

    if request.method == 'POST':
        form = AddSubscriberForm(request.POST)
        response = captcha.submit(
                                  request.POST.get('recaptcha_challenge_field'),                                    
                                  request.POST.get('recaptcha_response_field'),
                                  os.environ['RECAPTCHA_PRIVATE_KEY'],                                    
                                  request.META['REMOTE_ADDR'],)        
        if not response.is_valid:
            #messages.info(request, 'ReCaptcha was incorrect.')
            return HttpResponse('ReCaptcha was incorrect.')
                       
        if form.is_valid():
            new_sub = subscriber()
            cd = form.cleaned_data
            coordinates = cd['coord'].split(',')
             
            new_sub.email = cd['email']
            new_sub.fname = cd['fname']
            new_sub.lname = cd['lname']
            new_sub.sector = cd['sector']
            new_sub.geom = Point(float(coordinates[0]), float(coordinates[1]))
            try:
                mc = mailchimp.Mailchimp(os.environ['MAILCHIMP_API_KEY'])
                if mc.lists.member_info(os.environ['LIST_ID'], [{'email':request.POST['email']}])['success_count'] == 0:
                    mc.lists.subscribe(os.environ['LIST_ID'], {'email':request.POST['email']},
                                                              {'fname':request.POST['fname'],
                                                               'lname':request.POST['lname'],
                                                               'sector':request.POST['sector'],
                                                               #'range':request.POST['range'],
                                                               'test':'No',
                                                               'sendalert':'No'},
                                       double_optin=False)                    
                    new_sub.save()
                    return HttpResponseRedirect('success/')
                else:
                    #messages.error(request, "That email address is already subscribed.")
                    #return render_to_response('subscribe/subscribe.html', {}, context_instance=RequestContext(request))
                    return HttpResponse('That email address is already subscribed.')
            except  mailchimp.Error, e:
                return HttpResponse('An error occurred: %s - %s' % (e.__class__, e))            
        else:
            #messages.info(request, 'Form is incomplete.')
            return HttpResponseRedirect('/lights/subscribe')
    
    else:
        form = AddSubscriberForm()

    args = {}
    args.update(csrf(request))
    args['form'] = AddSubscriberForm()

    return render_to_response('subscribe/subscribe.html', args)

def success(request):
    return render_to_response('subscribe/success.html')

def alert(request):
    return render_to_response('subscribe/alert.html')

#===============================================================================
# def subscribe(request, list_id):
#     try:
#         m = get_mailchimp_api()
#         m.lists.subscribe(list_id, {'email':request.POST['email']})
#         messages.success(request,  "The email has been successfully subscribed")
#     except mailchimp.ListAlreadySubscribedError:
#         messages.error(request,  "That email is already subscribed to the list")
#         return redirect('/lists/'+list_id)
#     except mailchimp.Error, e:
#         messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
#         return redirect('/lists/'+list_id)
#     return redirect(reverse('lists.views.view', args=(list_id,)))
#===============================================================================
