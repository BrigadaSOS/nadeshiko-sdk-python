#!/usr/bin/env python3
"""Public SDK usage example."""

from __future__ import annotations

import os

from nadeshiko import Nadeshiko
from nadeshiko.models import SearchQuery

client = Nadeshiko(api_key=os.environ["NADESHIKO_API_KEY"])

data = client.search(query=SearchQuery(search="彼女"))
print(f"Found {len(data.segments)} segments")
