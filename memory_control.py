import psutil, requests, logging, time

"""
Можно также вынести константные значения в отдельный .env файл, но решил
не делать этого на данном этапе для удобства восприятия программы
"""

MEMORY_THRESHOLD = 90 # memory percentage to make an alarm
TIME_OFFSET_BETWEEN_TICKS = 3 # time offset between memory checkings in seconds

def send_alarm():
    url = "http://localhost:5000/alarm" # for test
    body = {"message": "Memory usage is too high! Threshold has been exceeded."}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=body, headers=headers)

        if response.status_code == 200:
            logging.info("Sent an alarm successfully")
        else:
            logging.error("Something wrong happened while sending an alarm")
    except requests.exceptions.ConnectionError:
        print("Unsuccessful connection to the server")


def main():
    while True:
        memory_usage = psutil.virtual_memory().percent

        if memory_usage > MEMORY_THRESHOLD:
            send_alarm()
            break

        time.sleep(TIME_OFFSET_BETWEEN_TICKS)


if __name__=="__main__":
    main()
