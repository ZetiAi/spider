# Spider

An async command-line web crawler (aiohttp) that saves every HTML page under a start URL, respecting robots.txt.

## Deployment map

**Status:** local-only tool, never deployed.

```text
poetry run python command_line.py --url <start> → aiohttp crawler → ./html_files
```

| Layer | Platform | Notes |
|---|---|---|
| Runtime | local Python 3.12 (Poetry) | aiohttp, beautifulsoup4, lxml; pytest |
| External calls | only the crawled site | No AI APIs |
| CI/CD | none | Dependabot only |

_Mapped 2026-10-04 from the default branch's config. Update this section when a platform changes._
