import random

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))

    for i in range(len(processes)):
        if i == 0:
            processes[i].waiting_time = 0
        else:
            processes[i].waiting_time = max(0, processes[i-1].waiting_time + processes[i-1].burst_time - processes[i].arrival_time)
            processes[i].turnaround_time = processes[i].waiting_time + processes[i].burst_time
            