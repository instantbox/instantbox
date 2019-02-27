import re
import datetime
import time
import subprocess

TIMEFORMAT = '%H:%M:%S'
DAYEFORMAT = '%Y-%m-%d'

def kill_container(containerId):
    try:
        print("[+] kill container is {}".format(containerId))
        # subprocess.check_output("docker rm -f {}".format(containerId), shell=True)
    except:
        return False
    else:
        return True

def check_time(_day, _time, _containerId):

    time_now = datetime.datetime.now().strftime(TIMEFORMAT)
    day_now = datetime.datetime.now().strftime(DAYEFORMAT)

    if day_now.split('-')[2] < _day.split('-')[2]:
        raise RuntimeError
    elif day_now.split('-')[2] == _day.split('-')[2]:

        interval = int(time_now.split(':')[0]) - int(_time.split(':')[0])
        if interval >= 24:
            kill_container(_containerId)
    else:
        interval_day = int(day_now.split('-')[2]) - int(_day.split('-')[2])
        if interval_day == 1:
            interval_time = int(time_now.split(':')[0]) - int(_time.split(':')[0])
            if interval_time > 0:
                kill_container(_containerId)
        else:
            kill_container(_containerId)

def regex_time(status_list):
    for item in status_list:
        if item:
            _day, _time, _containerId = re.findall(
                r"(\d{4}-\d{2}-\d{1,2}) (\d{1,2}:\d{1,2}:\d{1,2}) \+\d{4} \w{3}\s+([\s\S]+)",
                item)[0]
            print("[+] check container({}) create time...".format(_containerId))
            check_time(_day, _time, _containerId)
            time.sleep(1)



def get_status():
    status = subprocess.check_output("docker ps --format \"{{.CreatedAt}}\t{{.ID}}\"", shell=True)
    status_list = (status.decode("utf-8").strip()).split('\n')

    return status_list

if __name__ == '__main__':
    status_list = get_status()
    regex_time(status_list)