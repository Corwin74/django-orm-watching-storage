from django.shortcuts import render, get_object_or_404
from datacenter.models import Passcard, format_duration, is_visit_long
from datacenter.models import Visit


def passcard_info_view(request, passcode):

    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard__passcode=passcode):
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
                'is_strange': is_visit_long(visit)
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
