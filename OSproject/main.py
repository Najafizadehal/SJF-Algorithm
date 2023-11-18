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

    print("PID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(f"{processes[i].pid}\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{processes[i].waiting_time}\t\t{processes[i].turnaround_time}")
    avg_waiting_time, avg_turnaround_time = calculate_metrics(processes)
    print(f"avg_waiting_time: {avg_waiting_time}")
    print(f"avg_turnaround_time: {avg_turnaround_time}")

    cpu_utilization = calculate_cpu_utilization(processes)
    throughput = calculate_throughput(processes)
    avg_response_time = calculate_avg_response_time(processes)

    print(f"cpu_utilization: {cpu_utilization:.2f}%")
    print(f"throughput: {throughput:.2f}")
    print(f"avg_response_time: {avg_response_time:.2f}")

def generate_random_processes(num_processes):
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 20)
        processes.append(Process(pid, arrival_time, burst_time))
    return processes

def get_user_processes():
    num_processes = int(input("number of process: "))
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = int(input(f"Enter arrival_time : {pid}"))
        burst_time = int(input(f"Enter burst_time : {pid} "))
        processes.append(Process(pid, arrival_time, burst_time))
    return processes

def calculate_metrics(processes):
    total_waiting_time = sum([process.waiting_time for process in processes])
    total_turnaround_time = sum([process.turnaround_time for process in processes])
    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    return avg_waiting_time, avg_turnaround_time

def calculate_cpu_utilization(processes):
    total_burst_time = sum([process.burst_time for process in processes])
    total_time = max([process.arrival_time + process.burst_time for process in processes])
    cpu_utilization = (total_burst_time / total_time) * 100
    return cpu_utilization

def calculate_throughput(processes):
    total_time = max([process.arrival_time + process.burst_time for process in processes])
    throughput = len(processes) / total_time
    return throughput

def calculate_avg_response_time(processes):
    total_response_time = sum([process.waiting_time for process in processes])
    avg_response_time = total_response_time / len(processes)
    return avg_response_time

def main():
    print("Select the input method of the tables:")
    print("1. Random process table")
    print("2. Manual entry of processes")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        num_processes = int(input("Enter the number of processes: "))
        processes = generate_random_processes(num_processes)
        print("Table of random processes:")
        print("PID\tArrival Time\tBurst Time")
        for process in processes:
            print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}")
    elif choice == 2:
        processes = get_user_processes()
    else:
        print("Invalid selection. Exit.")
        return

    sjf(processes)

if __name__ == "__main__":
    main()
