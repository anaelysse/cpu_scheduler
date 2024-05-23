import time

class processQueue:
    def __init__(self, time_quantum):
        self.process_list = []
        self.program_start_time = time.time()
        self.last_turn_start = time.time()
        self.time_quantum = time_quantum
        self.current_process = None

    def addProcess(self, process_in):
        self.process_list.append(process_in)

    def moveProcesses(self):
        current_time_offset = time.time() - self.program_start_time

        # if no one is in booth, AND we have people waiting
        # let the first person in
        if self.current_process == None and len(self.process_list) > 0:
            self.current_process = self.process_list.pop(0)
            # update it so that our turn starts now
            self.last_turn_start = time.time()
            print("current time: %i | STARTED process with ID: %i" % (current_time_offset, self.current_process.process_id))
            self.current_process.num_turns += 1
            if self.current_process.response_time == -1:
                self.current_process.response_time = current_time_offset
                #its like getting a stamp at chuck e cheese :D
            return
        
        time_since_last_turn = time.time() - self.last_turn_start
        # if someone is in booth, AND, we have people waiting
        if self.current_process != None and len(self.process_list) > 0:

            # check if the person's TURN (time quantum) is up
            if time_since_last_turn >= self.time_quantum:
                # if their turn IS UP (>= time quantum), kick them out
                # and update the remaining time
                self.current_process.remaining_time -= time_since_last_turn
                if self.current_process.remaining_time > 0:
                    self.process_list.append(self.current_process)
                else:
                    # we execute this if there isn't remaining time
                    # process is over and we log time
                    self.current_process.end_time = current_time_offset
                    print("current time: %i | FINISHED process with ID: %i\nresponse time: %i, finished at: %i, turnaround time: %i" % (current_time_offset, self.current_process.process_id, self.current_process.response_time, self.current_process.end_time, self.current_process.end_time - self.current_process.response_time))

                # we've kicked the last person out, now we have to wait a bit
                time.sleep(1) # this is our "context switch" time
                # now we've waited 1 second to prepare our booth
                # the next person can go inside

                # we update the time offset because we've waited from context switch
                current_time_offset = time.time() - self.program_start_time

                self.current_process = self.process_list.pop(0)
                # update it so that our turn starts now
                self.last_turn_start = time.time()
                
                print("current time: %i | STARTED process with ID: %i" % (current_time_offset, self.current_process.process_id))
                self.current_process.num_turns += 1
                # we still need this, because if its the NEXT person's first turn
                # we should track it (give them a stamp)
                if self.current_process.response_time == -1:
                    self.current_process.response_time = current_time_offset
                    #its like getting a stamp at chuck e cheese :D
            return
        
        # if someone is in booth but no one is waiting they stay in until
        # they need to leave BUT not forever
        if self.current_process != None and len(self.process_list) == 0:
            time_since_last_turn = time.time() - self.last_turn_start
            if time_since_last_turn >= self.current_process.remaining_time:
                self.current_process.remaining_time = 0
                self.current_process.end_time = current_time_offset
                print("current time: %i | FINISHED process with ID: %i\nresponse time: %i, finished at: %i, turnaround time: %i" % (current_time_offset, self.current_process.process_id, self.current_process.response_time, self.current_process.end_time, self.current_process.end_time - self.current_process.response_time))
                self.current_process = None
            return