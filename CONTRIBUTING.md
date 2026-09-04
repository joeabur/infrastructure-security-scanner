# Contributing

Use Python 3.9 or newer. Keep modules read-only, independently testable, and returning `Finding` objects. Use `run_command` for optional tools and never pass untrusted input through a shell.

Before submitting changes:

```bash
python3 -m pytest
```

Add or update a focused fixture when changing detection behavior. Keep findings actionable and include evidence, recommendation, and confidence.
