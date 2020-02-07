#!/usr/bin/env python

# Get the 20CRv3 data for 1930 and 1931.

import datetime
import IRData.twcr as twcr

for year in (1930,1931):
    for var in ('PRMSL','TMP2m','PRATE','observations'):
        twcr.fetch(var,datetime.datetime(year,1,1),version='3')
