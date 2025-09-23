#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="ros2-unbag",
    version="0.1.0",
    description="A ROS 2 tool for exporting bags to human readable files. Supports pluggable export routines to handle any message type.",
    author="Lukas Ostendorf",
    author_email="lukas.ostendorf@ika.rwth-aachen.de",
    url="https://github.com/ika-rwth-aachen/ros2_unbag",
    packages=find_packages(),
    package_data={
        "ros2_unbag.ui": ["assets/loading.gif", "assets/title.png"]
    },
    install_requires=[
        "numpy==1.26.4",
        "opencv-python-headless==4.11.0.86",
        "pypcd4==1.3.0",
        "PySide6==6.9.1",
        "pyyaml==6.0.2",
        "tqdm==4.67.1"
    ],
    entry_points={
        "ros2cli.command": [
            "unbag = ros2_unbag.export:ExportCommand"
        ],
        "ros2cli.extension_point": [
            "ros2_unbag = ros2cli.command:CommandExtension"
        ]
    },
    python_requires=">=3.8",
)
