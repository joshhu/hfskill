#!/usr/bin/env python3
"""
Hugging Face Space Operations Script

This script provides comprehensive operations for managing Hugging Face Spaces.
It supports listing, retrieving information, starting, stopping, and interacting with Spaces.

Requirements:
    pip install huggingface_hub requests

Environment Variables:
    HF_TOKEN or HUGGINGFACE_TOKEN: Your Hugging Face access token
"""

import os
import sys
import json
import argparse
from typing import Optional, Dict, Any, List

try:
    from huggingface_hub import HfApi, SpaceInfo
    from huggingface_hub.utils import HfHubHTTPError
except ImportError:
    print("Error: huggingface_hub is not installed.", file=sys.stderr)
    print("Please install it with: pip install huggingface_hub", file=sys.stderr)
    sys.exit(1)


def get_token() -> Optional[str]:
    """Get Hugging Face token from environment variables."""
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_TOKEN")
    if not token:
        print("Warning: No HF_TOKEN or HUGGINGFACE_TOKEN found in environment.", file=sys.stderr)
        print("Some operations may require authentication.", file=sys.stderr)
    return token


def list_spaces(author: Optional[str] = None, search: Optional[str] = None, limit: int = 20, token: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List Hugging Face Spaces.

    Args:
        author: Filter by author username
        search: Search term for space names/descriptions
        limit: Maximum number of spaces to return
        token: HF access token (optional for public spaces)

    Returns:
        List of space information dictionaries
    """
    api = HfApi(token=token)

    try:
        spaces = api.list_spaces(
            author=author,
            search=search,
            limit=limit,
            full=True
        )

        results = []
        for space in spaces:
            space_dict = {
                "id": space.id,
                "author": space.author,
                "sha": space.sha,
                "last_modified": str(space.lastModified) if hasattr(space, 'lastModified') else None,
                "private": space.private if hasattr(space, 'private') else False,
                "likes": space.likes if hasattr(space, 'likes') else 0,
                "sdk": space.sdk if hasattr(space, 'sdk') else None,
            }
            results.append(space_dict)

        return results

    except Exception as e:
        print(f"Error listing spaces: {e}", file=sys.stderr)
        return []


def get_space_info(space_id: str, token: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Get detailed information about a specific Space.

    Args:
        space_id: Space ID in format "username/space-name"
        token: HF access token

    Returns:
        Dictionary with space information or None if error
    """
    api = HfApi(token=token)

    try:
        space = api.space_info(repo_id=space_id)

        info = {
            "id": space.id,
            "author": space.author,
            "sha": space.sha,
            "last_modified": str(space.lastModified) if hasattr(space, 'lastModified') else None,
            "private": space.private if hasattr(space, 'private') else False,
            "likes": space.likes if hasattr(space, 'likes') else 0,
            "sdk": space.sdk if hasattr(space, 'sdk') else None,
            "sdk_version": space.sdk_version if hasattr(space, 'sdk_version') else None,
            "runtime": space.runtime.stage if hasattr(space, 'runtime') and hasattr(space.runtime, 'stage') else None,
            "hardware": space.runtime.hardware if hasattr(space, 'runtime') and hasattr(space.runtime, 'hardware') else None,
        }

        return info

    except HfHubHTTPError as e:
        print(f"Error getting space info: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def restart_space(space_id: str, token: Optional[str] = None) -> bool:
    """
    Restart a Space.

    Args:
        space_id: Space ID in format "username/space-name"
        token: HF access token (required)

    Returns:
        True if successful, False otherwise
    """
    if not token:
        print("Error: Token is required to restart a space.", file=sys.stderr)
        return False

    api = HfApi(token=token)

    try:
        api.restart_space(repo_id=space_id)
        print(f"Successfully restarted space: {space_id}")
        return True

    except HfHubHTTPError as e:
        print(f"Error restarting space: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return False


def pause_space(space_id: str, token: Optional[str] = None) -> bool:
    """
    Pause a Space.

    Args:
        space_id: Space ID in format "username/space-name"
        token: HF access token (required)

    Returns:
        True if successful, False otherwise
    """
    if not token:
        print("Error: Token is required to pause a space.", file=sys.stderr)
        return False

    api = HfApi(token=token)

    try:
        api.pause_space(repo_id=space_id)
        print(f"Successfully paused space: {space_id}")
        return True

    except HfHubHTTPError as e:
        print(f"Error pausing space: {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return False


def get_space_runtime(space_id: str, token: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """
    Get runtime information for a Space.

    Args:
        space_id: Space ID in format "username/space-name"
        token: HF access token

    Returns:
        Dictionary with runtime information or None if error
    """
    api = HfApi(token=token)

    try:
        runtime = api.get_space_runtime(repo_id=space_id)

        runtime_info = {
            "stage": runtime.stage,
            "hardware": runtime.hardware if hasattr(runtime, 'hardware') else None,
            "requested_hardware": runtime.requested_hardware if hasattr(runtime, 'requested_hardware') else None,
            "sleep_time": runtime.sleep_time if hasattr(runtime, 'sleep_time') else None,
            "raw_data": str(runtime)
        }

        return runtime_info

    except HfHubHTTPError as e:
        print(f"Error getting space runtime: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def list_user_spaces(username: str, token: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List all spaces for a specific user.

    Args:
        username: Hugging Face username
        token: HF access token

    Returns:
        List of space information dictionaries
    """
    return list_spaces(author=username, limit=100, token=token)


def main():
    parser = argparse.ArgumentParser(description="Hugging Face Space Operations")
    parser.add_argument("--token", help="Hugging Face access token (or set HF_TOKEN env var)")

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # List spaces
    list_parser = subparsers.add_parser("list", help="List spaces")
    list_parser.add_argument("--author", help="Filter by author username")
    list_parser.add_argument("--search", help="Search term")
    list_parser.add_argument("--limit", type=int, default=20, help="Maximum number of results")

    # Get space info
    info_parser = subparsers.add_parser("info", help="Get space information")
    info_parser.add_argument("space_id", help="Space ID (username/space-name)")

    # Restart space
    restart_parser = subparsers.add_parser("restart", help="Restart a space")
    restart_parser.add_argument("space_id", help="Space ID (username/space-name)")

    # Pause space
    pause_parser = subparsers.add_parser("pause", help="Pause a space")
    pause_parser.add_argument("space_id", help="Space ID (username/space-name)")

    # Get runtime
    runtime_parser = subparsers.add_parser("runtime", help="Get space runtime information")
    runtime_parser.add_argument("space_id", help="Space ID (username/space-name)")

    # List user spaces
    user_parser = subparsers.add_parser("user", help="List spaces for a user")
    user_parser.add_argument("username", help="Hugging Face username")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Get token
    token = args.token or get_token()

    # Execute command
    if args.command == "list":
        results = list_spaces(author=args.author, search=args.search, limit=args.limit, token=token)
        print(json.dumps(results, indent=2, ensure_ascii=False))

    elif args.command == "info":
        info = get_space_info(args.space_id, token=token)
        if info:
            print(json.dumps(info, indent=2, ensure_ascii=False))
        else:
            sys.exit(1)

    elif args.command == "restart":
        success = restart_space(args.space_id, token=token)
        sys.exit(0 if success else 1)

    elif args.command == "pause":
        success = pause_space(args.space_id, token=token)
        sys.exit(0 if success else 1)

    elif args.command == "runtime":
        runtime = get_space_runtime(args.space_id, token=token)
        if runtime:
            print(json.dumps(runtime, indent=2, ensure_ascii=False))
        else:
            sys.exit(1)

    elif args.command == "user":
        results = list_user_spaces(args.username, token=token)
        print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
