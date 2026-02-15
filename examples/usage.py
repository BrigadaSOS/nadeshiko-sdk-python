#!/usr/bin/env python3
"""Public SDK usage example."""

import os

from nadeshiko import Nadeshiko
from nadeshiko.api.search import search
from nadeshiko.models import Error

client = Nadeshiko(
    base_url=os.getenv("NADESHIKO_BASE_URL", "https://api.nadeshiko.co"),
    token=os.getenv("NADESHIKO_API_KEY", "your-api-key"),
)

result = search.sync(
    client=client,
    body={"query": "彼女", "limit": 5},
)

if isinstance(result, Error):
    print(result.code, result.detail)
else:
    print(f"Found {len(result.sentences)} sentences")
