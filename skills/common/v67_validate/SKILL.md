---
name: v67-validate
description: Validates a V67 JSON envelope against the schema. Reports PASS or FAIL.
---

# V67 Validator

## Context / Trigger Requirements

Use this skill when you receive a V67 JSON envelope and need to verify it conforms to the schema. Input is the JSON to validate. Output is a validation report on stdout.

## Schema Reference

Fetch the raw content from these URLs before validating:

- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/schema/v67_schema.json — walk `$defs.V67Envelope` → `$defs.V67Header` → `$defs.V67Message` and all referenced types.
- https://raw.githubusercontent.com/Shridhar-2205/v67-protocol/main/models/v67_models.py — mirrors the schema as Pydantic classes.

You can `curl` or `fetch` the data from those URLs. Do not rely on cached or memorized schema content.

## Input Parameters

The only input is the V67 JSON envelope to validate. Derive all validation rules from the fetched schema.

## Instructions

1. **Fetch** the schema and model files from the URLs above.
2. **Parse** the input as JSON — reject if invalid.
3. **Validate** the input against the fetched schema, checking every required field, enum constraint, and type rule.
4. **Report** ALL errors found, not just the first.
5. **Output** the validation report as JSON only. No prose, no markdown fences.

## Constraints

- ALL validation rules MUST be derived from the fetched schema/model files, not hardcoded assumptions.
- You MUST fetch the remote files every time — do not assume schema content from memory.
- Report ALL errors found, not just the first.
- Do not modify the input — this is read-only validation.
- Output valid JSON only.
