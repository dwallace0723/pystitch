# pystitch
[![PyPI version](https://badge.fury.io/py/pystitchconnect.svg)](https://badge.fury.io/py/pystitchconnect)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/dwallace0723/pystitch.svg?branch=master)](https://travis-ci.com/dwallace0723/pystitch)
[![Python Versions](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://pypi.python.org/pypi/ansicolortags/)

a Python SDK for the [Stitch Connect API](https://www.stitchdata.com/docs/stitch-connect/api).

## Installation

```bash
pip install pystitchconnect
```

## Example Usage

```python
import os
from pystitch import PyStitch

STITCH_API_TOKEN = os.environ["STITCH_API_TOKEN"]

# Instantiate a PyStitch client using your API token.
client = PyStitch(token=STITCH_API_TOKEN)

# List all available Source objects.
sources = client.list_sources()

# Trigger a replication job for a specific Source.
response = client.start_replication_job(source_id=12345)
assert(response.ok)
```
