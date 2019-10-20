# Truncate-Logs-RPi
Python script that will empty files matching a user-defined file path and extension. Can be used with a cron job to regularly truncate logs or other file types.  

## Getting started

Set file path: `path = "/home/pi/"`

Set file extension `ext = glob.glob('*.log')`

Run the script `python truncate_logs.py`
