from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.models import Visit
from datacenter.models import format_duration, is_visit_long


def storage_information_view(request):

    in_storage = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in in_storage:
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(visit.get_duration()),
                'is_strange': is_visit_long(visit)
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
