import subprocess


def lock_file(name: str) -> bool:
    """Lock File

    Parameters
    ----------
    name : str
        The filename or path to filename

    Returns
    -------
    bool
        True if successfully lock file

    """
    commands = [
        "git",
        "lfs",
        "lock",
        name,
    ]
    result = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode:
        print(f"Warning! Error locking file {name}", result.stderr)
        return False

    return True


def unlock_file(lock_id: int) -> bool:
    """Unlock File

    Parameters
    ----------
    lock_id : int
        The locked object ID

    Returns
    -------
    bool
        True if successfully unlock file

    """
    commands = [
        "git",
        "lfs",
        "unlock",
        "-i",
        str(lock_id),
    ]
    result = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode:
        print(f"Warning! Error unlocking file ID {lock_id}", result.stderr)
        return False

    return True

