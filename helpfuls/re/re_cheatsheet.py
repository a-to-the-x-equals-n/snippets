
# ======================================================
#  - MATCH INLINE AND MULTI-LINE CODE BLOCKS -
# ======================================================

# Matches:
# - Inline code wrapped in single backticks: `example`
# - Multi-line code blocks wrapped in triple backticks:
#   ```
#   example
#   ```
code_block_pattern = r"(```[\s\S]+?```|`[^`\n]+`)"

# ======================================================
#  - MATCH HTML TAGS -
# ======================================================

# Matches:
# - Any HTML tag, including attributes: <tag attr="value">
# - Self-closing tags like <br />
# - Full block elements like <div>content</div>
html_tag_pattern = r"<[^>]+>"

# ======================================================
#  - MATCH MARKDOWN LINKS -
# ======================================================

# Matches:
# - Markdown links: [text](https://example.com)
# - Captures the text inside brackets while ignoring the URL
markdown_link_pattern = r"\[(.*?)\]\((.*?)\)"

# ======================================================
#  - MATCH MARKDOWN HEADERS (# Header) -
# ======================================================

# Matches:
# - Headers from `#` to `######`
# - Ensures only leading `#` are matched
markdown_header_pattern = r"^\#{1,6}\s+"

# ======================================================
#  - MATCH BOLD AND ITALIC TEXT -
# ======================================================

# Matches:
# - **bold** and *italic* formatting in Markdown
# - Removes the `**` or `*` while keeping the text inside
bold_italic_pattern = r"\*\*(.*?)\*\*|\*(.*?)\*"

# ======================================================
#  - MATCH HORIZONTAL RULES (--- or ***) -
# ======================================================

# Matches:
# - Horizontal rules made of three or more dashes (---) or asterisks (***)
horizontal_rule_pattern = r"^-{3,}$|^\*{3,}$"

'''
# ==============================
#        REGEX CHEAT SHEET
# ==============================
# Syntax: `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, `re.split()`
# Flags: re.IGNORECASE (or re.I), re.DOTALL (or re.S), re.MULTILINE (or re.M)

# ------------------------------
#   COMMON REGEX PATTERNS
# ------------------------------
# Match any single character except newline
.                      # "a" matches "a", "abc" matches "a" (first match)

# Match a literal character
a                      # Matches "a" in "apple"

# Match beginning (^) / end ($) of a string
^Hello                 # Matches "Hello world" but not "A Hello world"
world$                 # Matches "Hello world" but not "world Hello"

# Match digits, letters, and whitespace
\d                     # Matches any digit (0-9)
\D                     # Matches any non-digit
\w                     # Matches any word character (a-z, A-Z, 0-9, _)
\W                     # Matches any non-word character
\s                     # Matches any whitespace (spaces, tabs, newlines)
\S                     # Matches any non-whitespace character

# Match specific number of repetitions
a{3}                   # Matches exactly 3 "a" (e.g., "aaa")
a{2,4}                 # Matches between 2 and 4 "a" (e.g., "aa", "aaa", "aaaa")
a+                     # Matches one or more "a" (e.g., "a", "aa", "aaa")
a*                     # Matches zero or more "a" (e.g., "", "a", "aa")
a?                     # Matches zero or one "a" (e.g., "", "a")

# Match sets of characters
[abc]                  # Matches "a", "b", or "c"
[a-z]                  # Matches any lowercase letter
[A-Z]                  # Matches any uppercase letter
[0-9]                  # Matches any digit
[a-zA-Z0-9_]           # Matches any alphanumeric character
[^abc]                 # Matches any character except "a", "b", or "c"

# Match optional groups
(colou?r)              # Matches "color" and "colour" (optional "u")

# Match groups
(\d{4})-(\d{2})-(\d{2})  # Matches date format YYYY-MM-DD and captures groups

# Non-capturing group
(?:abc)                # Matches "abc" but does not capture it

# Named groups
(?P<year>\d{4})        # Matches and names a year group

# Lookahead and Lookbehind
# ------------------------------
# Positive Lookahead (?=...)
\d{3}(?=px)            # Matches 123 in "123px", but not in "123abc"

# Negative Lookahead (?!...)
\d{3}(?!px)            # Matches 123 in "123abc", but not in "123px"

# Positive Lookbehind (?<=...)
(?<=\$)\d+             # Matches digits after "$" in "$100"

# Negative Lookbehind (?<!...)
(?<!\$)\d+             # Matches digits not preceded by "$"

# ------------------------------
#  COMMON USE CASES
# ------------------------------
# Extract email addresses
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Extract phone numbers (123-456-7890)
\d{3}-\d{3}-\d{4}

# Extract URLs
https?://[^\s]+

# Extract words from a string
\w+

# Extract HTML tags
<[^>]+>'''