from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Schedule,Action
from .forms import ActionForm
# Create your views here.

def index(request):
    #return HttpResponse("Hello, world. You're at the activities index.")
    #latest_question_list = Schedule.objects.order_by('-date_begin')[:5]
    #output = ', '.join([q.description for q in latest_question_list])
    #return HttpResponse(output)
    #def index(request):
    latest_schedule_list = Schedule.objects.order_by('-date_begin')[:5]
    context = {'latest_schedule_list': latest_schedule_list}
    return render(request, 'activities/index.html', context)

def detail(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    return render(request, 'activities/details.html', {'schedule': schedule})

def edit_action(request, action_id):
    action = get_object_or_404(Action, pk=action_id)
    form = ActionForm(instance=action)
    if request.method == 'POST':
        form = ActionForm(request.POST,instance=action)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('activities:detail', args=[
            action.schedule.id])) 
    else:
        form = ActionForm(instance=action)
    context = {'action': action, 'form': form}
    return render(request, 'activities/action.html', context)

