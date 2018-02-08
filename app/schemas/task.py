task_schema = {
    "type": "object",
    "properties": {
        "task_id": {"type": "number"},
        "user_id": {"type": "number"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "done": {"done": "boolean"}
    },
    "required": ["name", "description", "user_id"],
    "additionalProperties": False,
}