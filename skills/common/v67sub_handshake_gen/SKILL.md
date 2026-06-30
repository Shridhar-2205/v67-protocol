---
name: v67sub-handshake-gen
description: Generates a V67Sub capability negotiation handshake frame as valid JSON.
---

# V67Sub Handshake Generator

## Context / Trigger Requirements

Use this skill when you need to produce a V67Sub handshake frame (capability negotiation) as valid JSON on stdout.

## Schema Reference

Fetch the raw content from these URLs before generating output:

- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/subprotocol/schema/v67sub_schema.json — see `$defs.V67SubHandshake`, `$defs.V67SubCapability`, `$defs.Intent`
- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/subprotocol/models/v67sub_models.py — see classes `V67SubHandshake`, `V67SubCapability`, `Intent`

You can `curl` or `fetch` the data from those URLs. Do not rely on cached or memorized schema content.

## Input Parameters

The user must provide:

- `intent` — one of the `Intent` enum values from the schema (`offer`, `accept`, `reject`)
- `capabilities` — list of capability names and revisions to negotiate

Optionally:

- `token` — authentication or session token for the handshake

## Instructions

1. **Fetch** the schema and model files from the URLs above.
2. **Parse** the fetched content to extract field requirements, types, and enum values.
3. **Generate** a `V67SubHandshake` conforming to the schema.
4. **Output** ONLY valid JSON. No explanation, no markdown fences.

## Constraints

- All validation rules MUST come from the fetched schema/model files, not hardcoded assumptions.
- You MUST fetch the remote files every time — do not assume schema content from memory.
- Output valid JSON only.
