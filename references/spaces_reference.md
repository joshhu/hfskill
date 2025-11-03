# Hugging Face Spaces Reference

## Overview

Hugging Face Spaces are applications that run on Hugging Face infrastructure. They can be powered by various frameworks including Gradio, Streamlit, Docker, and static HTML.

## Space ID Format

All Spaces are identified by a unique ID in the format: `username/space-name`

Examples:
- `stabilityai/stable-diffusion`
- `openai/whisper`
- `meta-llama/llama-2-chat`

## Space Runtime States

Spaces can be in various runtime states:

- **RUNNING**: Space is active and accessible
- **BUILDING**: Space is being built/deployed
- **STOPPED**: Space has been stopped
- **PAUSED**: Space has been paused to save resources
- **SLEEPING**: Space is in sleep mode due to inactivity
- **RUNTIME_ERROR**: Space encountered an error

## Hardware Options

Spaces can run on different hardware tiers:

- `cpu-basic`: Free tier with basic CPU
- `cpu-upgrade`: Upgraded CPU
- `t4-small`: NVIDIA T4 GPU (small)
- `t4-medium`: NVIDIA T4 GPU (medium)
- `a10g-small`: NVIDIA A10G GPU (small)
- `a10g-large`: NVIDIA A10G GPU (large)
- `a100-large`: NVIDIA A100 GPU (large)

## SDK Types

Spaces can be built with different SDKs:

- **gradio**: Gradio-based applications
- **streamlit**: Streamlit applications
- **docker**: Custom Docker containers
- **static**: Static HTML/JS applications

## Common Operations

### List Spaces
Search and filter spaces by author, search terms, or other criteria.

### Get Space Information
Retrieve detailed metadata about a specific space including:
- Runtime state
- Hardware configuration
- SDK version
- Last modified date
- Visibility (public/private)
- Number of likes

### Restart Space
Restart a space to apply changes or recover from errors. Requires authentication and ownership/write access.

### Pause Space
Pause a space to save compute resources when not in use. Can be resumed later. Requires authentication and ownership.

### Get Runtime Information
Get real-time runtime information including:
- Current stage/state
- Allocated hardware
- Requested hardware changes
- Sleep time configuration

## Authentication

Most read operations (listing, getting info) work without authentication for public spaces.
Write operations (restart, pause, hardware changes) require:

1. A valid Hugging Face access token
2. Ownership or write access to the space

### Token Permissions

Access tokens can have different scopes:
- **read**: Read access to private content
- **write**: Write access (required for space management)

## Rate Limits

Hugging Face API has rate limits:
- Authenticated requests: Higher rate limits
- Unauthenticated requests: Lower rate limits
- Specific limits depend on your account tier

## Common Errors

- **401 Unauthorized**: Invalid or missing token
- **403 Forbidden**: Insufficient permissions (need write access)
- **404 Not Found**: Space does not exist or is private
- **429 Too Many Requests**: Rate limit exceeded
- **503 Service Unavailable**: Space is temporarily unavailable

## Best Practices

1. **Use Environment Variables**: Store tokens in `HF_TOKEN` or `HUGGINGFACE_TOKEN`
2. **Handle Errors Gracefully**: Check for HTTP errors and runtime states
3. **Respect Rate Limits**: Add delays between bulk operations
4. **Check Runtime State**: Verify space state before performing operations
5. **Use Specific Space IDs**: Always use full `username/space-name` format
