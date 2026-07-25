"""Optional integration boundary.

The default application never calls an external LLM. A future organisation-approved
adapter can implement this interface after consent, privacy and security review.
"""
from dataclasses import dataclass
import os


@dataclass
class LLMConfig:
    provider: str = os.getenv("LLM_PROVIDER", "")
    api_key: str = os.getenv("LLM_API_KEY", "")


def is_configured(config: LLMConfig | None = None) -> bool:
    current = config or LLMConfig()
    return bool(current.provider and current.api_key)


def generate(*args, **kwargs):
    raise RuntimeError(
        "External generation is disabled in the default no-API build. "
        "Use the generated prompt with an institutionally approved AI tool."
    )
