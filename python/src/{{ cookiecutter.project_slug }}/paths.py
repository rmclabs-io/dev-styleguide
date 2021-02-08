# -*- coding: utf-8 -*-
""""""

import os
from pathlib import Path

CACHE = Path(
    os.environ.get("XDG_CACHE_HOME", Path.home()/".cache")
) / "{{ cookiecutter.project_slug }}"

CONFIG = Path(
    os.environ.get("XDG_CONFIG_HOME", Path.home()/".config")
) / "{{ cookiecutter.project_slug }}"
