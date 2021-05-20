from django.shortcuts import render
from django.http import HttpResponse
from .resources import UserDataResource
from tablib import Dataset
from .models import UserData


def export(request):
    UserData_resource = UserDataResource()
    dataset = UserData_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        UserData_resource = UserDataResource()
        dataset = Dataset()
        new_UserData = request.FILES['myfile1']

        imported_data = dataset.load(new_UserData.read(), format='xlsx')
        # print(imported_data)
        for data in imported_data:
            print(data[1])
            value = UserData(
                data[0],
                data[1],
                data[2],
                data[3]
            )
            value.save()

            # result = UserData_resource.import_data(dataset, dry_run=True)  # Test the data import

        # if not result.has_errors():
        #    UserData_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'cook/input.html')