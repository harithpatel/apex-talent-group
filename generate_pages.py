"""Generate programmatic SEO pages for file converter tool."""
import os, json, random

formats = ["PDF","Word","Excel","PowerPoint","JPG","PNG","CSV","JSON","HTML","Markdown","TXT","EPUB","MP3","MP4","WAV","GIF","SVG","WEBP","HEIC","TIFF","RTF","ODT","DOCX","XLSX"]
pairs = [{"src":s,"dst":d,"slug":f"convert-{s.lower()}-to-{d.lower()}"} for s in formats for d in formats if s!=d]

template = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Convert {src} to {dst} Free Online — AI-Powered | Apex Tools</title>
<meta name="description" content="Convert {src} to {dst} instantly for free. AI-enhanced conversion. No signup required.">
<link rel="canonical" href="https://harithpatel.github.io/apex-talent-group/{slug}">
<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:system-ui;background:#050508;color:#e0e0e8;line-height:1.7;padding:32px 24px}}.w{{max-width:700px;margin:0 auto}}h1{{font-size:1.8em;margin-bottom:16px}}h2{{color:#6366f1;margin:24px 0 8px}}p{{color:#aaa;margin:8px 0}}.btn{{display:inline-block;padding:16px 32px;background:linear-gradient(135deg,#6366f1,#8b5cf6);color:#fff;border-radius:12px;text-decoration:none;font-weight:700;margin:20px 0}}.card{{background:#0c0c14;border:1px solid #1e1e2e;border-radius:12px;padding:24px;margin:16px 0}}a{{color:#6366f1}}ul{{padding-left:20px;color:#aaa}}li{{margin:4px 0}}</style></head><body><div class="w">
<h1>Convert {src} to {dst} Free Online</h1>
<p>AI-powered {src} to {dst} conversion. Free, fast, secure.</p>
<div class="card" style="text-align:center"><p style="font-size:1.2em;font-weight:700;color:#6366f1">⚡ {src} → {dst} Converter</p><p>3 free/day. Unlimited $9/month.</p><a href="https://triyambakam-apex-corp.hf.space" class="btn">Convert Now →</a></div>
<h2>How to Convert {src} to {dst}</h2><ol style="padding-left:20px;color:#aaa"><li>Click convert above</li><li>Upload your {src} file</li><li>AI converts to {dst}</li><li>Download instantly</li></ol>
<h2>Features</h2><ul><li>AI-enhanced quality</li><li>Preserves formatting</li><li>No signup for free tier</li><li>Works on any device</li></ul>
<h2>More Converters</h2><p>{links}</p>
<div style="text-align:center;margin:32px 0"><a href="https://triyambakam-apex-corp.hf.space" class="btn">Start Converting Free →</a></div>
</div></body></html>"""

existing = [f[:-5] for f in os.listdir(".") if f.startswith("convert-") and f.endswith(".html")]
print(f"Existing pages: {len(existing)}")

count = 0
for p in pairs:
    if p["slug"] in existing:
        continue
    if count >= 30:  # 30 pages per run
        break
    links = " · ".join(f'<a href="{r["slug"]}.html">{r["src"]}→{r["dst"]}</a>' for r in random.sample(pairs, 8))
    html = template.format(src=p["src"], dst=p["dst"], slug=p["slug"], links=links)
    with open(f'{p["slug"]}.html', "w") as f:
        f.write(html)
    count += 1

print(f"Generated {count} new pages (total will be {len(existing)+count})")
