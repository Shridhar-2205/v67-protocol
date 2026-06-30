---
name: v67-transform
description: Converts plain-text input into a valid V67 envelope JSON.
---

# V67 Transform

## Context / Trigger Requirements

Use this skill when the input is a human-readable message that needs to be converted into a valid V67 envelope. Input pattern: `<sender_service>: <message>`.

If no sender service is provided (no colon separator), default sender service to `"user-cli"`.

## Schema Reference

Fetch the raw content from these URLs before generating output:

- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/schema/v67_schema.json — see `$defs.V67Envelope`, `$defs.V67Header`, `$defs.V67Message`, `$defs.Sender`, `$defs.Recipient`
- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/models/v67_models.py — see classes `V67Envelope`, `V67Header`, `V67Message`, `Sender`, `Recipient`

You can `curl` or `fetch` the data from those URLs. Do not rely on cached or memorized schema content.

## Input Parameters

Derive all structural fields from the fetched schema. The only user input is the plain-text message.

## Instructions

1. **Fetch** the schema and model files from the URLs above.
2. **Parse** input to extract `sender_service` and `message`. No colon → sender service is `"user-cli"`.
3. Derive sender `node_id`: lowercase, replace spaces with dashes, append `-node`.
4. **Generate** a `V67Envelope` conforming to the fetched schema with defaults:
   - `header.priority` = `"normal"`
   - `header.recipient` = `{"node_id": "gateway-001", "channel": "inbound"}`
   - `message.type` = `"text"`
   - `message.encoding` = `"utf8"`
   - `message.body` = `{"content": "<message>"}`
5. **Output** ONLY valid JSON. No explanation, no markdown fences.

## Constraints

- All structural rules MUST come from the fetched schema/model files, not hardcoded assumptions.
- You MUST fetch the remote files every time — do not assume schema content from memory.
- `message.body` must be an object.
- Output valid JSON only.
