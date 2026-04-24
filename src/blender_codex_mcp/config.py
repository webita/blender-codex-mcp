"""Runtime configuration for Blender Codex MCP."""

from __future__ import annotations

import os
from dataclasses import dataclass


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass
class TelemetryConfig:
    """Telemetry defaults are conservative for local agent use."""

    enabled: bool = _env_bool("BLENDER_MCP_TELEMETRY_ENABLED", False)
    max_prompt_length: int = int(os.environ.get("BLENDER_MCP_MAX_PROMPT_LENGTH", "1000"))
    supabase_url: str = os.environ.get("BLENDER_MCP_SUPABASE_URL", "")
    supabase_anon_key: str = os.environ.get("BLENDER_MCP_SUPABASE_ANON_KEY", "")


telemetry_config = TelemetryConfig()
