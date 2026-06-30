---
name: v67sub-negotiate
description: Generates two JSONs — a V67Sub handshake frame and a V67 envelope carrying it — by chaining v67sub-handshake-gen then v67-message-gen.
---

# V67Sub Negotiate (Chained Skill)

This skill chains two existing skills in sequence using the Skill tool and outputs both results.

## Input Parameters

### For v67sub-handshake-gen (subprotocol):

| Parameter | Required | Description |
|-----------|----------|-------------|
| `intent` | yes | One of: `offer`, `accept`, `reject` |
| `capabilities` | yes | List of capabilities, each with a `name` (string) and `revision` (integer) |
| `token` | no | Auth/session token (default: null) |

### For v67-message-gen (main protocol envelope):

| Parameter | Required | Description |
|-----------|----------|-------------|
| `priority` | yes | One of: `low`, `normal`, `high`, `critical` |
| `sender_node_id` | yes | Unique ID of the sending node |
| `sender_service` | yes | Service name of the sender |
| `recipient_node_id` | yes | Unique ID of the recipient node |
| `recipient_channel` | yes | Channel on the recipient node |

The `type`, `encoding`, and `body` for the envelope message are auto-filled from the handshake output.

## Instructions

1. **Invoke** the Skill tool with `skill: "v67sub-handshake-gen"` passing the user's handshake parameters (intent, capabilities, token) as args. Capture the JSON output as `handshake_result`.

2. **Output** the subprotocol JSON labeled `## Subprotocol (V67Sub Handshake)` followed by the `handshake_result` JSON.

3. **Invoke** the Skill tool with `skill: "v67-message-gen"` passing args that include:
   - The user's envelope header parameters (priority, sender, recipient)
   - `type` = `handshake`
   - `encoding` = `utf8`
   - `body` = the `handshake_result` JSON object from step 1

4. **Output** the main protocol JSON labeled `## Main Protocol (V67 Envelope)` followed by the envelope JSON from step 3.

## Output Format

```
## Subprotocol (V67Sub Handshake)
<handshake JSON>

## Main Protocol (V67 Envelope)
<envelope JSON containing the handshake as message.body>
```

## Constraints

- You MUST use the Skill tool to invoke each sub-skill — do not inline their logic or fetch their files manually.
- Each sub-skill will fetch its own schema from GitHub. Do not duplicate that work.
- Output both JSONs — the standalone subprotocol frame AND the full envelope wrapping it.
