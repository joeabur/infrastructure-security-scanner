import shutil
import subprocess
from typing import List, Optional


def run_command(command: List[str], timeout: float = 5.0) -> Optional[str]:
    if not command or shutil.which(command[0]) is None:
        return None
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        return result.stdout.strip() or result.stderr.strip()
    except (OSError, subprocess.SubprocessError):
        return None
