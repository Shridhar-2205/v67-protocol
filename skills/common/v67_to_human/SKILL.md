---
name: v67-to-human
description: Converts a V67 JSON envelope into a simple human-readable string.
---

# V67 to Human

## Context / Trigger Requirements

Use this skill when you receive a valid V67 JSON envelope and need to produce a simple, human-readable plain-text representation on stdout.

## Schema Reference

Fetch the raw content from these URLs before processing:

- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/schema/v67_schema.json — see `$defs.V67Envelope`, `$defs.V67Header`, `$defs.V67Message`, `$defs.Sender`, `$defs.Recipient`
- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/models/v67_models.py — see classes `V67Envelope`, `V67Header`, `V67Message`, `Sender`, `Recipient`

You can `curl` or `fetch` the data from those URLs. Do not rely on cached or memorized schema content.

## Input Parameters

The only input is a valid V67 JSON envelope. Derive field structure from the fetched schema.

## Instructions

1. **Fetch** the schema and model files from the URLs above.
2. **Parse** the input as a valid V67 JSON envelope per `$defs.V67Envelope`.
3. **Extract** the sender service, priority, message type, and body content.
4. **Format** as plain text: `[V67/<priority>/<type>] <sender_service>@<sender_node_id>: <body summary>`
5. **Output** ONLY the plain-text string. No JSON, no markdown fences, no explanation.

## Constraints

- All structural rules MUST come from the fetched schema/model files, not hardcoded assumptions.
- You MUST fetch the remote files every time — do not assume schema content from memory.
- Output plain text only — no JSON wrapping, no markdown.
- If the body cannot be summarized as a single line, produce a concise multi-line representation.
