#!/usr/bin/env python3
"""Return a list of schools that have a specific topic."""

def schools_by_topic(mongo_collection, topic):
    """
    Finds all schools that contain a given topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic to search for

    Returns:
        list: matching school documents
    """
    return list(mongo_collection.find({"topics": topic}))
