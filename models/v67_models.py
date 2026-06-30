"""Python bindings for the V67 protocol schema."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel, Field


class Priority(str, Enum):
    low = "low"
    normal = "normal"
    high = "high"
    critical = "critical"


class Encoding(str, Enum):
    utf8 = "utf8"
    base64 = "base64"
    binary = "binary"


class Sender(BaseModel):
    """Identifies the origin of a V67 message."""

    node_id: str
    service: str
    region: Optional[str] = None


class Recipient(BaseModel):
    """Target destination for a V67 message."""

    node_id: str
    channel: str


class V67Header(BaseModel):
    """Routing and metadata envelope for every V67 message."""

    version: str
    message_id: str
    timestamp: datetime
    priority: Priority
    sender: Sender
    recipient: Recipient
    ttl: Optional[int] = None
    correlation_id: Optional[str] = None


class V67Message(BaseModel):
    """The body/content carried by a V67 envelope."""

    type: str
    encoding: Encoding
    body: dict[str, Any]
    tags: Optional[list[str]] = None


class V67Envelope(BaseModel):
    """A complete V67 protocol unit: header (routing/metadata) + message (content)."""

    header: V67Header
    message: V67Message