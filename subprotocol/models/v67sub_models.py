"""Python bindings for the V67Sub capability negotiation subprotocol."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Intent(str, Enum):
    offer = "offer"
    accept = "accept"
    reject = "reject"


class V67SubCapability(BaseModel):
    """A single capability being negotiated."""

    name: str
    revision: int


class V67SubHandshake(BaseModel):
    """A V67Sub negotiation frame."""

    intent: Intent
    capabilities: list[V67SubCapability]
    token: Optional[str] = None
