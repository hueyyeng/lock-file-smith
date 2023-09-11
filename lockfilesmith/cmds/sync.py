import subprocess


def clone(repo_url: str, new_name: str = None) -> bool:
    """Clone Git LFS repository

    Parameters
    ----------
    repo_url : str
        The Git LFS repository URL
    new_name : str or None
        The new name of the cloned Git LFS repository. Default None

    Returns
    -------
    bool
        True if successfully cloned

    """
    commands = [
        "git",
        "lfs",
        "clone",
        repo_url,
    ]
    if new_name:
        commands.append(new_name)

    result = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode:
        print(f"Warning! Fail to clone {repo_url}. Error: {result.stderr}")
        return False

    return True


def pull() -> bool:
    """Pull Git LFS repository commits and LFS files

    Returns
    -------
    bool
        True if successfully pulled with or without new commits/LFS files

    """
    # git -c filter.lfs.smudge= -c filter.lfs.required=false pull && git lfs pull
    commands = [
        "git",
        "-c", "filter.lfs.smudge",
        "-c", "filter.lfs.required=false",
        "&&",
        "git",
        "lfs",
        "pull",
    ]
    result = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode:
        print(f"Warning! Fail to pull commits/LFS files. Error: {result.stderr}")
        return False

    return True


def push() -> bool:
    """Push Git LFS repository commits and LFS files

    Returns
    -------
    bool
        True if successfully pushed with or without new commits/LFS files

    """
    commands = [
        "git",
        "push",
    ]
    result = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if result.returncode:
        print(f"Warning! Fail to push commits/LFS files. Error: {result.stderr}")
        return False

    return True