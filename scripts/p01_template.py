# -*- coding: utf-8 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Project: OC Watersheds
# Part 1: Raw Data Processing ----
# Author: Dr. Kostas Alexandridis, GISP
# Version: 2026.1, Date: March 2026
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("\nOC Watersheds: Part 1 - Raw Data Processing\n")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1. Import necessary libraries ----
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n1. Import necessary libraries")

import os
import datetime
import pytz
import pandas as pd
from dotenv import load_dotenv
from scripts.ocwbd import OCWBD

# Load environment variables from .env file
load_dotenv()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2. Create project metadata and directories ----
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\n2. Create project metadata and directories")

# Initialize the OCWBD class
wbd = OCWBD(part = 1, version = 2026.1)

# Create project variables
part = wbd.part
version = wbd.version

# Create project metadata
prj_meta = wbd.prj_meta

# Create project directories
prj_dirs = wbd.prj_dirs

# Create logger
logger = wbd.logger

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# End of Script ----
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\nLast Execution:", datetime.datetime.now().strftime("%Y-%m-%d"))
print("End of Script")
