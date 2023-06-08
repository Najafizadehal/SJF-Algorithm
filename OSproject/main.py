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

    print("PID\tavviral time\tburst time\twaiting time\tturnaround time")

    for i in range (len(processes)):
        print(f"{processes[i].pid}\t{processes[i].avviral_time}\t\t{processes[i].burst_time}\t\t{processes[i].waiting_time}\t\t{processes[i].turnaround_time}")

    avg_waiting_time, avg_turnaround_time = calculate_metrics(processes)
    print(f":میانگین زمان انتظار{avg_waiting_time}")
    print(f":میانگین زمان برگشت{avg_turnaround_time}")

def generate_random_processes(num_processes):
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = random.randint(0, 10)
        burst_time = random.randint (1, 20)
        processes.append(Process(pid, arrival_time, burst_time))

        return processes

