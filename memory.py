"""
Memory Management
Handles state, context, and historical data for agents.
"""

from typing import Any, Dict, List
from datetime import datetime
import json


class Memory:
    """
    Memory system for agents to store and retrieve information.
    """

    def __init__(self):
        self.entries: List[Dict[str, Any]] = []
        self.context: Dict[str, Any] = {}

    def add_entry(self, source: str, content: str, entry_type: str = "log") -> None:
        """
        Add an entry to memory.

        Args:
            source: Agent or system that created the entry
            content: The content to store
            entry_type: Type of entry (log, result, error, etc.)
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "content": content,
            "type": entry_type,
        }
        self.entries.append(entry)

    def get_entries(self, source: str = None, entry_type: str = None) -> List[Dict[str, Any]]:
        """
        Retrieve entries from memory.

        Args:
            source: Filter by source (optional)
            entry_type: Filter by type (optional)

        Returns:
            List of matching entries
        """
        results = self.entries
        if source:
            results = [e for e in results if e["source"] == source]
        if entry_type:
            results = [e for e in results if e["type"] == entry_type]
        return results

    def set_context(self, key: str, value: Any) -> None:
        """Store context information."""
        self.context[key] = value

    def get_context(self, key: str = None) -> Any:
        """Retrieve context information."""
        if key:
            return self.context.get(key)
        return self.context

    def clear(self) -> None:
        """Clear all memory entries and context."""
        self.entries.clear()
        self.context.clear()

    def export(self, filepath: str) -> None:
        """Export memory to a JSON file."""
        data = {
            "entries": self.entries,
            "context": self.context,
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def __str__(self) -> str:
        """String representation of memory contents."""
        return f"Memory with {len(self.entries)} entries"
