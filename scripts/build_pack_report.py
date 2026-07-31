from __future__ import annotations

import argparse
from pathlib import Path

try:
    from build_embed_blocks import build_pack_report
except ModuleNotFoundError:
    from scripts.build_embed_blocks import build_pack_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build the core starry-diagram pack report without publication adapters."
    )
    parser.add_argument("diagrams_root", type=Path)
    args = parser.parse_args(argv)

    report = build_pack_report(args.diagrams_root)
    return 0 if report["status"] in {"passed", "passed_with_warnings"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
