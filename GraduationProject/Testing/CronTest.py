import schedule
import time



def job():
    print("islam")



schedule.every(0.1).minutes.do(job)


while 1:
    schedule.run_pending()
    time.sleep(0.1)