# Module for windows process related functions
import psutil


def get_pid(process_name: str) -> int:
    """
    Get the PID by name
    """
    if process_name:
        for proc in psutil.process_iter():
            if process_name == proc.name():
                return proc.pid


def get_location(process_name: str = None, pid: int = None) -> str:
    """
    Get the location of a process
    Use either process_name or pid
    """
    if process_name:
        pid = get_pid(process_name)
    return psutil.Process(pid).exe() if psutil.Process(pid).exe() != psutil.Process().exe() else None


def kill(process_name: str = None, pid: int = None) -> None:
    """
    Stop a process by name or PID
    """
    if process_name:
        pid = get_pid(process_name)
    psutil.Process(pid).kill()
