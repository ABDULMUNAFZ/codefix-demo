"""Decide which installed plugins are compatible with the running host version."""

from __future__ import annotations

from dataclasses import dataclass

from app.versions import satisfies


@dataclass(frozen=True)
class Plugin:
    name: str
    version: str
    requires_host: str


@dataclass(frozen=True)
class CompatReport:
    loadable: list[str]
    rejected: dict[str, str]


def check_plugins(host_version: str, plugins: list[Plugin]) -> CompatReport:
    loadable: list[str] = []
    rejected: dict[str, str] = {}
    for plugin in plugins:
        if satisfies(host_version, plugin.requires_host):
            loadable.append(plugin.name)
        else:
            rejected[plugin.name] = f"requires host {plugin.requires_host}, running {host_version}"
    return CompatReport(loadable=loadable, rejected=rejected)
