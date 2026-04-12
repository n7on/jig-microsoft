"""Save an OAuth token response to a file.

Usage:
    save_token.py <response_json> <output_file> [--with-refresh]

Extracts access_token, calculates expires_on, and optionally includes refresh_token.
"""

import json
import sys
import time


def main():
    response = json.loads(sys.argv[1])
    output_file = sys.argv[2]
    with_refresh = "--with-refresh" in sys.argv

    token = {
        "access_token": response["access_token"],
        "expires_on": int(time.time() + response["expires_in"] - 60),
    }

    if with_refresh:
        token["refresh_token"] = response.get("refresh_token", "")

    with open(output_file, "w") as f:
        json.dump(token, f)


if __name__ == "__main__":
    main()
