#!/usr/bin/env python3
"""Insert a new document in a MongoDB collection using kwargs."""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: document fields to insert

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
