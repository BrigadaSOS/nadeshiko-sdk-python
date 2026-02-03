#!/usr/bin/env python3
"""
Nadeshiko SDK Example

Shows all API methods using the namespace approach.
"""

import os
from nadeshiko import Nadeshiko, Environment
from nadeshiko.api.search import search, search_multiple, fetch_media_info
from nadeshiko.models import Error

# Configure once
client = Nadeshiko(
    api_key=os.getenv('NADESHIKO_API_KEY', 'your-api-key'),
    base_url=Environment.PRODUCTION,  # or Environment.LOCAL
)


def search_example():
    """Example 1: Search for sentences"""
    result = search.sync(
        client=client,
        body={
            'query': '彼女',
            'limit': 5,
        },
    )

    if isinstance(result, Error):
        print('Error:', result.code, result.detail)
        return

    print(f'Found {len(result.sentences)} sentences\n')

    for sentence in result.sentences:
        print(f'JP: {sentence.segment_info.content_jp}')
        print(f'EN: {sentence.segment_info.content_en}')
        print(f'From: {sentence.basic_info.name_anime_en}\n')


def search_multiple_example():
    """Example 2: Search multiple words"""
    result = search_multiple.sync(
        client=client,
        body={
            'words': ['彼女', '私'],
        },
    )

    if isinstance(result, Error):
        print('Error:', result)
        return

    for match in result.results:
        print(f'{match.word}: {match.total_matches} matches')


def fetch_media_info_example():
    """Example 3: Fetch media info"""
    result = fetch_media_info.sync(
        client=client,
        query={
            'query': 'steins gate',
            'type': 'anime',
        },
    )

    if isinstance(result, Error):
        print('Error:', result)
        return

    for media in result.results:
        print(f'- {media.english_name}')
