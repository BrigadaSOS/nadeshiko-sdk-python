#!/usr/bin/env python3
"""Internal SDK usage example."""

from __future__ import annotations

import os

from nadeshiko_internal import Nadeshiko

client = Nadeshiko(api_key=os.environ["NADESHIKO_API_KEY"])

announcement = client.get_announcement()
print(announcement.title if announcement is not None else "No announcement")
