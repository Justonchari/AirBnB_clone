#!/usr/bin/python3
"""The __init__ magic method used in the models directory."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
