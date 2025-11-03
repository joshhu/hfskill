# HFSkill - Hugging Face Spaces Management Toolkit

A comprehensive command-line toolkit for managing and interacting with Hugging Face Spaces. This skill provides easy-to-use operations for listing, monitoring, and controlling Hugging Face Spaces through Python scripts.

## Features

- **List Spaces**: Search and filter Spaces by author or keyword
- **Space Information**: Get detailed metadata about any Space
- **Runtime Management**: Restart or pause Spaces
- **Status Monitoring**: Check Space runtime state and hardware configuration
- **User Spaces**: List all Spaces owned by a specific user

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/hfskill.git
cd hfskill
```

2. Install dependencies:
```bash
pip install huggingface_hub
```

## Authentication

Most operations require a Hugging Face access token. Configure authentication using one of these methods:

### Option 1: Environment Variable (Recommended)
```bash
export HF_TOKEN="hf_your_token_here"
```

### Option 2: Command-line Parameter
```bash
python3 scripts/space_operations.py --token "hf_your_token_here" <command>
```

**Token Requirements:**
- Read operations: Token optional for public Spaces
- Write operations (restart/pause): Token required with write permissions

## Usage

### List Spaces
```bash
# List recent Spaces
python3 scripts/space_operations.py list --limit 10

# List Spaces by author
python3 scripts/space_operations.py list --author stabilityai

# Search Spaces
python3 scripts/space_operations.py list --search "chatbot"
```

### Get Space Information
```bash
python3 scripts/space_operations.py info stabilityai/stable-diffusion
```

### Restart a Space
```bash
python3 scripts/space_operations.py restart myusername/my-space
```

### Pause a Space
```bash
python3 scripts/space_operations.py pause myusername/my-space
```

### Get Space Runtime Status
```bash
python3 scripts/space_operations.py runtime stabilityai/stable-diffusion
```

### List User's Spaces
```bash
python3 scripts/space_operations.py user stabilityai
```

## Space ID Format

All Spaces are identified using the format: `username/space-name`

Examples:
- `stabilityai/stable-diffusion`
- `openai/whisper`
- `meta-llama/llama-2-chat`

## Common Workflows

### Monitor and Restart a Space
```bash
# Check Space status
python3 scripts/space_operations.py runtime myusername/my-space

# Restart if needed
python3 scripts/space_operations.py restart myusername/my-space
```

### Search and Explore Spaces
```bash
# Search for chatbot Spaces
python3 scripts/space_operations.py list --search "chatbot" --limit 20

# Get detailed info
python3 scripts/space_operations.py info username/interesting-space
```

## Project Structure

```
hfskill/
├── SKILL.md                    # Detailed skill documentation
├── README.md                   # This file
├── scripts/
│   └── space_operations.py     # Main executable script
└── references/
    └── spaces_reference.md     # API reference documentation
```

## Error Handling

Common errors and solutions:

- **"No HF_TOKEN found"**: Set the environment variable or pass `--token`
- **401 Unauthorized**: Invalid or expired token
- **403 Forbidden**: Insufficient permissions or not the Space owner
- **404 Not Found**: Space doesn't exist or is private
- **429 Too Many Requests**: Rate limit exceeded, wait before retrying

## Documentation

For detailed information about Space states, hardware options, and API specifics, refer to:
- `SKILL.md` - Complete skill documentation
- `references/spaces_reference.md` - API reference

## Requirements

- Python 3.6+
- `huggingface_hub` package

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
