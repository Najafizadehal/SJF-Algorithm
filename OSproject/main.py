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
    print(f"میانگین زمان انتظار: {avg_waiting_time}")
    print(f"میانگین زمان برگشت: {avg_turnaround_time}")

    cpu_utilization = calculate_cpu_utilization(processes)
    throughput = calculate_throughput(processes)
    avg_response_time = calculate_avg_response_time(processes)

    print(f"بهره‌وری CPU: {cpu_utilization:.2f}%")
    print(f"توان عملیاتی: {throughput:.2f} فرآیند/ثانیه")
    print(f"میانگین زمان پاسخ: {avg_response_time:.2f} ثانیه")

def generate_random_processes(num_processes):
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 20)
        processes.append(Process(pid, arrival_time, burst_time))
    return processes

def get_user_processes():
    num_processes = int(input("تعداد فرآیندها را وارد کنید: "))
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = int(input(f"زمان ورود فرآیند {pid} را وارد کنید: "))
        burst_time = int(input(f"زمان اجرای فرآیند {pid} را وارد کنید: "))
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
    print("روش ورودی جدول فرآیندها را انتخاب کنید:")
    print("1. جدول فرآینده تصادفی")
    print("2. ورودی دستی فرآیندها")
    choice = int(input("انتخاب خود را وارد کنید (1 یا 2): "))

    if choice == 1:
        num_processes = int(input("تعداد فرآیندها را وارد کنید: "))
        processes = generate_random_processes(num_processes)
        print("جدول فرآیندهای تصادفی:")
        print("PID\tArrival Time\tBurst Time")
        for process in processes:
            print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}")
    elif choice == 2:
        processes = get_user_processes()
    else:
        print("انتخاب نامعتبر. خروج.")
        return

    sjf(processes)

if __name__ == "__main__":
    main()
