"""Build a resource access array for Microsoft Graph app registration.

Usage:
    build_resource_access.py <graph_sp_json> <perm1:type> <perm2:type> ...

    Types: Role (application), Scope (delegated)

Example:
    build_resource_access.py "$graph_sp" \
        "InformationProtectionPolicy.Read.All:Role" \
        "InformationProtectionPolicy.Read:Scope"

Outputs the full requiredResourceAccess JSON array.
"""

import json
import sys


def main():
    graph_sp = json.loads(sys.argv[1])
    perm_specs = sys.argv[2:]

    scopes = {p["value"]: p["id"] for p in graph_sp.get("oauth2PermissionScopes", [])}
    roles = {p["value"]: p["id"] for p in graph_sp.get("appRoles", [])}

    resource_access = []
    for spec in perm_specs:
        name, perm_type = spec.rsplit(":", 1)
        if perm_type == "Role":
            perm_id = roles.get(name)
        else:
            perm_id = scopes.get(name)

        if not perm_id:
            print(f"Permission '{name}' not found", file=sys.stderr)
            sys.exit(1)

        resource_access.append({"id": perm_id, "type": perm_type})

    result = [{
        "resourceAppId": "00000003-0000-0000-c000-000000000000",
        "resourceAccess": resource_access,
    }]

    json.dump(result, sys.stdout, ensure_ascii=False)


if __name__ == "__main__":
    main()
