import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from file_analyzer import analyze_file
from logger import log_event

WATCH_FOLDER = "uploads"

class UploadHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:

            filepath = event.src_path
            filename = filepath.split("/")[-1]

            print("New file uploaded:", filename)

            log_event(f"New file uploaded: {filename}")

            analyze_file(filepath)


if __name__ == "__main__":

    print("Secure File Transfer Monitoring System Started")

    event_handler = UploadHandler()

    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
