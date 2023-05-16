#!/usr/bin/env python3

import os

print("Running system update...")
os.system("sudo apt update && sudo apt upgrade -y")

print("Cleaning the package cache...")
os.system("sudo apt clean")

print("Removing old packages...")
os.system("sudo apt autoremove --purge -y")

print("Script execution completed.")
