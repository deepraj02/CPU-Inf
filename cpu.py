import psutil as psu

print(f"Physical Cores:-{psu.cpu_count(logical=False)}")
print(f"Total Cores:-{psu.cpu_count(logical=True)}")

cpufreq=psu.cpu_freq()
print(f"Max Frequency:-{cpufreq.max:.2f}Mhz")
print(f"Min Frequency:-{cpufreq.min:.2f}Mhz")
print(f"Current Frequency:-{cpufreq.current:.2f}Mhz")

print("CPU Usage per Core:")
for i,perc in enumerate(psu.cpu_percent(percpu=True, interval=1)):
    print(f"Core:{i}:{perc}%")
print(f"Total CPU Usage: {psu.cpu_percent()}%")