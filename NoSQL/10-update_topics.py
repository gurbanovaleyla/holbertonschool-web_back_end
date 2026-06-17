#!/usr/bin/env python3
"""Update the topics of a school document based on its name."""

def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to match
        topics (list): list of topics to set

    Returns:
        Nothing
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
