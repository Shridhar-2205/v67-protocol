---
name: v67-header-gen
description: Generates a valid V67 header JSON from priority and sender.
---

# V67 Header Generator

## Context / Trigger Requirements

Use this skill when you need to produce a standalone V67 header as valid JSON on stdout.

## Schema Reference

Fetch the raw content from these URLs before generating output:

- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/schema/v67_schema.json — see `$defs.V67Header`, `$defs.Sender`, `$defs.Recipient`, `$defs.Priority`
- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/models/v67_models.py — see class `V67Header`, `Sender`, `Recipient`, `Priority`

You can `curl` or `fetch` the data from those URLs. Do not rely on cached or memorized schema content.

## Input Parameters

The user must provide:

- `priority` — one of the `Priority` enum values from the schema (e.g. `low`, `normal`, `high`, `critical`)
- `sender_node_id` — unique ID of the sending node
- `sender_service` — service name of the sender
- `recipient_node_id` — unique ID of the recipient node
- `recipient_channel` — channel on the recipient node

Auto-generate `message_id` as a UUID (v4). Derive all other fields and their types from the fetched schema (`$defs.V67Header`).

## Instructions

1. **Fetch** the schema and model files from the URLs above.
2. **Parse** the fetched content to extract field requirements, types, and enum values.
3. **Generate** a `V67Header` conforming to the schema.
4. **Output** ONLY valid JSON. No explanation, no markdown fences.

## Constraints

- All validation rules MUST come from the fetched schema/model files, not hardcoded assumptions.
- You MUST fetch the remote files every time — do not assume schema content from memory.
- Output valid JSON only.
