import markdown
from weasyprint import HTML
from pathlib import Path

ROOT = Path(__file__).parent.parent
input_file = ROOT / "Readme.md"
output_file = ROOT / "build" / "caict-meeting-proposal.pdf"
output_file.parent.mkdir(parents=True, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @page {{ margin: 42px 54px; }}
  body {{
    font-family: 'Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'Source Han Sans CN',
                 'Droid Sans Fallback', sans-serif;
    line-height: 1.72;
    color: #1a1a1a;
    font-size: 13.5px;
  }}
  h1 {{
    color: #1a1a2e;
    border-bottom: 2px solid #d0d0d0;
    padding-bottom: 7px;
    margin-top: 0;
    margin-bottom: 12px;
    font-size: 19px;
  }}
  h2 {{
    color: #16213e;
    border-bottom: 1px solid #e0e0e0;
    padding-bottom: 4px;
    margin-top: 22px;
    margin-bottom: 7px;
    font-size: 15.5px;
  }}
  h3 {{ color: #0f3460; margin-top: 14px; margin-bottom: 5px; font-size: 14px; }}
  code {{
    background: #f4f4f4;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 0.88em;
    font-family: monospace;
  }}
  pre {{
    background: #f4f4f4;
    padding: 10px 14px;
    border-radius: 5px;
    font-size: 0.88em;
  }}
  li {{ margin-bottom: 4px; }}
  ul, ol {{ margin: 5px 0; padding-left: 22px; }}
  strong {{ color: #222; }}
  p {{ margin: 6px 0; }}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

HTML(string=html).write_pdf(str(output_file))
print(f"Done: {output_file}")
