from process import process
import time

class processCreator:
    def __init__(self, file_path, queue):
        self.file_path = file_path
        self.queue = queue
        self.waiting_processes = []
        self.program_start_time = time.time()

    def readingFile(self):
        file = open(self.file_path, "r")
        lines = file.readlines()
        for each_line in lines[1:]:
            # "1          | 0            | 5             "
            each_line = each_line.replace(" ", "")
            # "1|0|5"
            process_data = each_line.split("|")
            # ["1","0","5"]
            new_process = process(int(process_data[0]), int(process_data[1]), int(process_data[2]))
            print("made process with ID: %s" % new_process.process_id)
            self.waiting_processes.append(new_process)
        
    def addToQueue(self):
        current_time_offset = time.time() - self.program_start_time
        for process in self.waiting_processes:
            if process.arrival_time <= current_time_offset:
                print("current time: %i | adding process with ID: %i, arrival time of: %i to queue" % (current_time_offset, process.process_id, process.arrival_time))
                self.queue.addProcess(process)
                self.waiting_processes.remove(process)