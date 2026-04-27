"""
scanner.py - Scans Claude Code JSONL transcript files and stores data in SQLite.
"""

import json
import os
import glob
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

PROJECTS_DIR = Path.home() / ".claude" / "projects"
XCODE_PROJECTS_DIR = Path.home() / "Library" / "Developer" / "Xcode" / "CodingAssistant" / "ClaudeAgentConfig" / "projects"
DB_PATH = Path.home() / ".claude" / "usage.db"
DEFAULT_PROJECTS_DIRS = [PROJECTS_DIR, XCODE_PROJECTS_DIR]

# Higher number = higher priority when choosing a session's primary model
MODEL_PRIORITY = {"opus": 3, "sonnet": 2, "haiku": 1}


def _model_priority(model):
    """Return a priority score for a model name (higher = more capable)."""
    pass


def get_db(db_path=DB_PATH):
    # Ensure the parent directory exists — on a fresh install or CI runner
    # ~/.claude may not yet exist, and sqlite3.connect needs the parent dir.
    pass


def init_db(conn):
    pass


def project_name_from_cwd(cwd):
    """Derive a friendly project name from cwd path."""
    pass


def parse_jsonl_file(filepath):
    """Parse a JSONL file and return (session_metas, turns, line_count).

    Deduplicates streaming events by message.id — Claude Code logs multiple
    JSONL records per API response, all sharing the same message.id. Only the
    last record per message_id is kept (it has the final usage tallies).
    """
    pass


def aggregate_sessions(session_metas, turns):
    """Aggregate turn data back into session-level stats."""
    pass


def upsert_sessions(conn, sessions):
    pass


def insert_turns(conn, turns):
    pass


def scan(projects_dir=None, projects_dirs=None, db_path=DB_PATH, verbose=True):
    pass


if __name__ == "__main__":
    import sys
    projects_dir = None
    for i, arg in enumerate(sys.argv[1:]):
        if arg == "--projects-dir" and i + 1 < len(sys.argv[1:]):
            projects_dir = Path(sys.argv[i + 2])
            break
    scan(projects_dir=projects_dir)
