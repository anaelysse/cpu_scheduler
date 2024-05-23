from processQueue import processQueue
from processCreator import processCreator
import sys
import time

# python3 main.py process.txt 5
if __name__ == "__main__":
    file_name = sys.argv[1]
    time_quantum = int(sys.argv[2])

    our_process_queue = processQueue(time_quantum)
    our_process_creator = processCreator(file_name, our_process_queue)

    our_process_creator.readingFile() # loads in the processes from the file

    while True:
        # if we have processes that should be added to the queue
        # (arrival time == now) we add them to the queue
        our_process_creator.addToQueue()
        # we do the logic of checking people in booths, people on line
        # and move / unmove processes to and from execution
        our_process_queue.moveProcesses()
        # sleep half a second between each loop iteration
        # so our real computer doesnt get spammed with an infinite loop
        time.sleep(0.5)

        # if we DONT have a running current process
        # and we DONT have upcoming processes
        # and we DONT have processes that will be scheduled
        if (our_process_queue.current_process == None) and (len(our_process_queue.process_list) == 0) and (len(our_process_creator.waiting_processes) == 0):
            # our program is done running :) we leave!
            break