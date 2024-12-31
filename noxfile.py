import os
import platform
import subprocess

import nox

args = dict(python=["3.7", "3.8", "3.9", "3.10", "3.11"], reuse_venv=True)

@nox.session(venv_backend="venv", **args)
def test(session):
    session.install("--upgrade", "pip")
    session.install("pytest")
    session.run("pytest")
