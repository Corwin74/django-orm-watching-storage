from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def active_passcards_view(request):
    # Программируем здесь

    in_da_storage = Visit.objects.filter(leaved_at=None)
    print(in_da_storage.count())
    for visit in in_da_storage:
        enter_at = localtime(visit.entered_at)
        print(visit.passcard)
        print(f'Вошел в хранилище: {enter_at}')
        print(f'Провел в хранилище: {(localtime() - enter_at) // 1000000 * 1000000}')
    active_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
