import json
import tempfile
from markdownify import markdownify as mdify
from markitdown import MarkItDown

def extract_html_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # Extract HTML based on how the rest api works
    return data["body"]["storage"]["value"]

def main():
    json_filename = input("Enter JSON filename: ")
    html_content = extract_html_from_json(json_filename)
    print("Extracted HTML content.")

    # markdownify conversion
    md1 = mdify(html_content)

    # MarkItDown conversion via tempfile
    md_converter = MarkItDown()
    with tempfile.NamedTemporaryFile("w+", suffix=".html", delete=False, encoding='utf-8') as f:
        f.write(html_content)
        f.flush()
        result = md_converter.convert(f.name)
    md2 = result.markdown

    # Save outputs
    with open("output_markdownify.md", "w", encoding="utf-8") as f:
        f.write(md1)
    print("Markdownify output saved to output_markdownify.md")

    with open("output_markitdown.md", "w", encoding="utf-8") as f:
        f.write(md2)
    print("MarkItDown output saved to output_markitdown.md")

if __name__ == "__main__":
    main()
