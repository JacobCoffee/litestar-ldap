"""Configuration dataclasses for LDAP configurations.

.. todo:: Make it work
"""
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class LDAPSettings:
    """Security settings dataclass for LDAP configurations."""
    SERVICE_ACCOUNT: str | None
    SERVICE_PASSWORD: str | None
    DOMAIN: str = "mydomain"
    LDAP_SERVER: str = "ldap://mydomain.example.com"
    ROOT_DN: str = "DC=example,DC=com"
    ROOT_USERS_DN: list[str] = field(default_factory=lambda: [
        "CN=Users,dc=example,dc=com",
        "OU=Corporate,OU=User Accounts,DC=example,DC=com",
    ])
    ROOT_GROUPS_DN: str = "OU=Groups,DC=example,DC=com"
