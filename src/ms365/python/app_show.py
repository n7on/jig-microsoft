"""Show app registration with resolved permission names.

Usage:
    app_show.py <app_json> <graph_sp_json>

Outputs TSV with headers: name,client_id,permissions
"""

import json
import sys


def main():
    app = json.loads(sys.argv[1])
    sp = json.loads(sys.argv[2])

    perm_map = {
        p["id"]: p["value"]
        for p in sp.get("oauth2PermissionScopes", []) + sp.get("appRoles", [])
    }

    perms = ",".join(
        perm_map.get(ra["id"], ra["id"])
        for rra in app.get("requiredResourceAccess", [])
        for ra in rra.get("resourceAccess", [])
    )

    print("name,client_id,permissions")
    print(f"{app['displayName']}\t{app['appId']}\t{perms}")


if __name__ == "__main__":
    main()
