# V67 Common Skills

Reusable skills for working with V67 protocol messages and the V67Sub subprotocol.

## Skills

| Skill | Description |
|-------|-------------|
| `v67_header_gen` | Generates a standalone V67 header as valid JSON for a given priority and sender |
| `v67_message_gen` | Generates a complete V67 envelope (header + message) as valid JSON |
| `v67_to_human` | Converts a V67 JSON envelope into a human-readable plain-text string |
| `v67_transform` | Converts plain-text human input into a valid V67 envelope |
| `v67_validate` | Validates a V67 JSON envelope against the schema and reports PASS/FAIL with details |
| `v67sub_handshake_gen` | Generates a V67Sub capability negotiation handshake frame as valid JSON |
| `v67sub_validate` | Validates a V67Sub handshake JSON against the subprotocol schema |
