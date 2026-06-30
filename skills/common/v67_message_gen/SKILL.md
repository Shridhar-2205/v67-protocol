---
name: v67-message-gen
description: Generates a complete V67 envelope (header + message) as valid JSON.
---

# V67 Message Generator

## Context / Trigger Requirements

Use this skill when you need to produce a complete V67 envelope (header + message) as valid JSON on stdout.

## Schema Reference

Fetch the raw content from these URLs before generating output:

- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/schema/v67_schema.json — see `$defs.V67Envelope`, `$defs.V67Header`, `$defs.V67Message`, `$defs.Priority`, `$defs.Encoding`
- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/models/v67_models.py — see classes `V67Envelope`, `V67Header`, `V67Message`, `Priority`, `Encoding`

You can `curl` or `fetch` the data from those URLs. Do not rely on cached or memorized schema content.

## Input Parameters

The user must provide:

- `priority` — one of the `Priority` enum values from the schema (e.g. `low`, `normal`, `high`, `critical`)
- `sender_node_id` — unique ID of the sending node
- `sender_service` — service name of the sender
- `recipient_node_id` — unique ID of the recipient node
- `recipient_channel` — channel on the recipient node
- `type` — string describing the message type
- `encoding` — one of the `Encoding` enum values from the schema (e.g. `utf8`, `base64`, `binary`)
- `body` — object containing the message content

Auto-generate `message_id` as a UUID (v4). Derive all other fields and their types from the fetched schema (`$defs.V67Envelope`).

## Instructions

1. **Fetch** the schema and model files from the URLs above.
2. **Parse** the fetched content to extract field requirements, types, and enum values.
3. **Generate** a `V67Envelope` conforming to the schema.
4. **Output** ONLY valid JSON. No explanation, no markdown fences.

## Constraints

- All validation rules MUST come from the fetched schema/model files, not hardcoded assumptions.
- You MUST fetch the remote files every time — do not assume schema content from memory.
- `message.body` MUST be an object — never a string or number.
- Output valid JSON only.
