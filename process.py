class process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.burst_time = burst_time
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.end_time = -1
        self.response_time = -1
        self.num_turns = 0
        self.remaining_time = burst_time