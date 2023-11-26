import os.path
import datetime
from app import generate_id


def delete():
    idLAstet = str(int(generate_id()) - 1)
    for i in range(1, int(idLAstet) + 1):
        filename = f'storage//{i}.txt'
        ctime = os.path.getctime(filename)
        ctime_datetime = datetime.datetime.fromtimestamp(ctime)
        datetime_now = datetime.datetime.now()

        if datetime_now >= ctime_datetime + datetime.timedelta(hours=1):
            os.remove(filename)


delete()
