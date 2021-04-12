#!/usr/bin/env python3
"""setup.py script for alice discord bot"""
from setuptools import find_packages, setup

setup(
    name="alice",
    version="0.0",  # This only affects the egg-info file with our build methodology
    packages=find_packages(include=["alice*"]),
    description="Alice discord bot",
    scripts=["alicebot.sh"],
    install_requires=["discord.py>=1.7.1"]
)
