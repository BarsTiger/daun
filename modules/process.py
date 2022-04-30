# Module for windows process related functions
import psutil


def get_pid(process_name: str) -> int:
    """
    Get the PID by name
    """
    if process_name:
        for proc in psutil.process_iter():
            if process_name == proc.name():
                return proc.pid if proc.pid != psutil.Process().pid else None


def get_name(pid: int) -> str:
    """
    Get the name of a process by PID
    """
    try:
        return psutil.Process(pid).name()
    except psutil.NoSuchProcess:
        return "Not found"


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
    if pid is not None:
        psutil.Process(pid).kill()
    else:
        raise Exception("Process not found")
