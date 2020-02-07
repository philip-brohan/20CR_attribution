#!/usr/bin/env python

# Get the 4.6.1 data for 1930 and 1931.

import datetime
import IRData.twcr as twcr

for year in (1930,1931):
    for month in range(1,13):
        for var in ('prmsl','air.2m','prate','observations'):
            try:
                twcr.fetch(var,
                           datetime.datetime(year,month,1),
                           version='4.6.1')
