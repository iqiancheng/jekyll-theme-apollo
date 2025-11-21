import os
import re
import urllib.request
import urllib.error
import ssl

# Configuration
POSTS_DIR = "_posts"
OUTPUT_FILE = "dead_links.txt"

# Ignore SSL certificate errors (for testing purposes)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_links_from_file(filepath):
    """Extracts all http/https links from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Regex to match URLs in markdown: [text](url) or ![alt](url) or just (url)
    # We capture the content inside parentheses that starts with http
    links = re.findall(r'\((http[s]?://[^)]+)\)', content)
    return set(links)

def check_link(url):
    """Checks if a URL is accessible. Returns status code or error message."""
    try:
        # User-Agent is often required to avoid 403 Forbidden from some sites
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
            return response.getcode()
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)

def main():
    dead_links = []
    
    if not os.path.exists(POSTS_DIR):
        print(f"Error: Directory '{POSTS_DIR}' not found.")
        return

    print(f"Scanning files in {POSTS_DIR}...")
    
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(POSTS_DIR, filename)
            links = get_links_from_file(filepath)
            
            if not links:
                continue
                
            print(f"Checking {filename} ({len(links)} links)...")
            
            for link in links:
                status = check_link(link)
                
                # Consider 4xx and 5xx as dead links, or connection errors (strings)
                if isinstance(status, int) and status >= 400:
                    print(f"  [DEAD] {status}: {link}")
                    dead_links.append(f"{filepath}|{link}")
                elif isinstance(status, str): # Exception message
                    print(f"  [ERR ] {status}: {link}")
                    dead_links.append(f"{filepath}|{link}")
                else:
                    # Link is OK
                    pass

    # Write results to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for line in dead_links:
            f.write(line + "\n")
    
    print(f"\nScan complete. Found {len(dead_links)} dead links.")
    if dead_links:
        print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
