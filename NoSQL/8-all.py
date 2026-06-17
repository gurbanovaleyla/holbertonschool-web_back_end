#!/usr/bin/env python3
"""List all documents in a MongoDB collection."""

def list_all(mongo_collection):
    """
    Returns all documents in a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        list: all documents, or empty list if none exist
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
