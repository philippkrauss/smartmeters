#!/usr/bin/python3
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import sys


if (len(sys.argv) != 2):
    print('specify value')
    exit(1)

value = sys.argv[1]


token = "<snip>"
org = "<snip>"
url = "<snip>"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

bucket="SmartMeters"

write_api = client.write_api(write_options=SYNCHRONOUS)

point = (
Point("heizung")
.tag("art", "waerme")
.field("zaehlerstand", int(value.replace("\x02", ""))) # not sure why, but the string starts with 0x02, which stands for START_OF_TEXT...
)
write_api.write(bucket=bucket, org=org, record=point)
