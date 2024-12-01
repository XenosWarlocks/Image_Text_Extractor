import logging

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    return logging.getLogger()

class ProgressTracker:
    def __init__(self, total):
        self.total = total

    def update(self, progress):
        print(f"Progress: {progress}/{self.total}")