#!/usr/bin/env python3
"""Internal SDK usage example."""

import os

from nadeshiko_internal import Nadeshiko
from nadeshiko_internal.api.auth import login
from nadeshiko_internal.models import Error

client = Nadeshiko(
    base_url=os.getenv("NADESHIKO_BASE_URL", "https://api.nadeshiko.co"),
    token=os.getenv("NADESHIKO_API_KEY", "your-api-key"),
)

result = login.sync(
    client=client,
    body={"email": "internal@example.com", "password": "secret"},
)

if isinstance(result, Error):
    print(result.code, result.detail)
else:
    print("Login succeeded")
