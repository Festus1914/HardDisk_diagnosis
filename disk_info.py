import psutil

def get_disk_info():
    disk_partitions = psutil.disk_partitions()
    disk_usage = {partition.device: psutil.disk_usage(partition.mountpoint) for partition in disk_partitions}
    disk_io_counters = psutil.disk_io_counters(perdisk=True)

    return {
        'partitions': disk_partitions,
        'usage': disk_usage,
        'io_counters': disk_io_counters
    }

if __name__ == "__main__":
    disk_info = get_disk_info()
    print(disk_info)
