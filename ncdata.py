#!/usr/bin/env python
import cdsapi
c = cdsapi.Client()
c.retrieve("reanalysis-era5-pressure-levels",
{
"variable": "temperature",
"pressure_level": "1000",
"product_type": "reanalysis",
"year": "2020",
"month": "10",
"day": "01",
"time": "12:00",
"format": "netcdf"
}, 
"/home/bing/Downloads/download.nc")
