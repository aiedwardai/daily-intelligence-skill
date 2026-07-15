# Agent Reach Channel Cookie Setup (Headless Server)

These channels need cookies but **cannot** use `--from-browser` (no browser on server).
Export from your local browser with Cookie-Editor → Header String, paste the string here.

## Twitter/X

```bash
agent-reach configure twitter-cookies '<cookie-header-string>'
```

No special workaround needed — `agent-reach configure` has a `twitter-cookies` subcommand.

**Verify:**
```bash
twitter --help    # should list commands (no error)
```

## Reddit (rdt-cli)

`rdt login` only supports browser extraction. On a server, manually write credential.json:

```python
import json, time, os
cookies = {}
# Parse cookie_header_string into dict
for pair in cookie_header_string.split(";"):
    pair = pair.strip()
    if "=" not in pair: continue
    name, _, value = pair.partition("=")
    cookies[name.strip()] = value.strip()

cred = {
    "cookies": cookies,
    "source": "manual",
    "username": None,        # will be populated on verify
    "modhash": None,
    "saved_at": time.time(),
    "last_verified_at": time.time(),
}
path = os.path.expanduser("~/.config/rdt-cli/credential.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w") as f:
    json.dump(cred, f, indent=2)
os.chmod(path, 0o600)
```

The required cookie is `reddit_session`. If present, `rdt status --json` shows `authenticated: true`.

**Verify:**
```bash
rdt status --json      # authenticated: true + username
rdt search "AI" -n 2   # should return results, not 403
```

## Xueqiu (雪球)

`agent-reach configure` has **no** `xueqiu-cookies` option. Set manually in config:

```python
import yaml, os
config_file = os.path.expanduser("~/.agent-reach/config.yaml")
os.makedirs(os.path.dirname(config_file), exist_ok=True)

data = {}
if os.path.exists(config_file):
    with open(config_file) as f:
        data = yaml.safe_load(f) or {}

data["xueqiu_cookie"] = cookie_header_string
with open(config_file, "w") as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
os.chmod(config_file, 0o600)
```

The module reads `Config().get("xueqiu_cookie")` from this YAML file.

**Verify:**
```python
from agent_reach.channels.xueqiu import XueqiuChannel
ch = XueqiuChannel()
status, msg = ch.check()  # → "ok" if working
posts = ch.get_hot_posts(limit=3)  # → list of dicts
```

## Xiaohongshu (小红书)

`agent-reach configure` has `xhs-cookies` — no workaround needed:

```bash
agent-reach configure xhs-cookies '<cookie-header-string>'
```

## troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `rdt status` → `authenticated: false` | Missing `reddit_session` cookie | Re-export from browser, ensure Cookie-Editor shows that cookie |
| Xueqiu check → `off` | `xueqiu_cookie` key not set in config.yaml | Check the key name exactly matches `xueqiu_cookie` |
| `twitter user @handle --json` returns profile only, no tweets | Used wrong command | Use `twitter user-posts @handle --json` instead |
| tencent-news-cli: `Error: unknown flag: --keyword` | Syntax changed | Use `tencent-news-cli search <keyword>` (positional, no `--keyword` flag) |
| tencent-news-cli: `command not found` | Not in PATH | Create symlink: `ln -sf ~/.tencent-news-cli/bin/tencent-news-cli ~/.local/bin/tencent-news-cli` |