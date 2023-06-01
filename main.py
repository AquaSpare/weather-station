from apscheduler.schedulers.background import BackgroundScheduler


def print_hi():
    print("Hi")


def main():
    scheduler = BackgroundScheduler()
    scheduler.start()

    scheduler.add_job(print_hi, "interval", minutes=1)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        scheduler.shutdown(wait=True)


if __name__ == "__main__":
    main()
