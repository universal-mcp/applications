# Project Documentation

This project uses Python managed by `uv` for dependency management and includes guidelines for building API integration applications.

## Documentation Structure

The documentation has been organized into focused files:

- **[SETUP.md](./SETUP.md)** - Python + uv environment setup, dependency management, and common commands
- **[APPLICATION.md](./APPLICATION.md)** - Guidelines for creating API integration applications, tool naming conventions, and best practices
- **[TESTING.md](./TESTING.md)** - Comprehensive testing guide for API integrations, test patterns, and troubleshooting

## Quick Start

1. **Setup Environment** - See [SETUP.md](./SETUP.md) for:
   - Installing and configuring `uv`
   - Managing dependencies with `pyproject.toml` and `uv.lock`
   - Common commands reference

2. **Build Applications** - See [APPLICATION.md](./APPLICATION.md) for:
   - Creating new API integration applications
   - Tool function naming and documentation standards
   - Best practices checklist
   - Complete minimal application example

3. **Test Applications** - See [TESTING.md](./TESTING.md) for:
   - Testing philosophy and workflow
   - Test script structure and templates
   - Common issues and solutions
   - Best practices summary

## Repository Structure

```
src/universal_mcp/applications/<app_name>/
├── __init__.py
├── app.py                      # Application implementation
└── test_<app_name>_tools.py   # Tests (co-located with app)
```

## Core Principles

- **Use `uv` for all Python operations** - Never use `pip install` directly
- **All tool methods must be async** - Except `list_tools()` which is synchronous
- **Authentication via integration** - Inject credentials using `AgentrIntegration`
- **Test co-location** - Keep test files in the same directory as the application code
- **Comprehensive documentation** - Every tool needs complete docstring with Args, Returns, Raises, Tags

## Need Help?

Refer to the specific documentation files:
- Environment issues? → [SETUP.md](./SETUP.md)
- Building a new app? → [APPLICATION.md](./APPLICATION.md)
- Testing problems? → [TESTING.md](./TESTING.md)
