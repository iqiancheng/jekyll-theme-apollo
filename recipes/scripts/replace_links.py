import os
import random

# Configuration
DEAD_LINKS_FILE = "dead_links.txt"
PLACEHOLDER_BASE = "https://loremflickr.com/800/400/random"

def main():
    if not os.path.exists(DEAD_LINKS_FILE):
        print(f"Error: {DEAD_LINKS_FILE} not found. Run check_links.py first.")
        return

    # Group dead links by file to minimize file I/O
    # Format: filepath -> [bad_url1, bad_url2, ...]
    replacements = {}

    with open(DEAD_LINKS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            parts = line.split('|')
            if len(parts) != 2:
                print(f"Skipping invalid line: {line}")
                continue
                
            filepath, bad_url = parts
            
            if filepath not in replacements:
                replacements[filepath] = []
            replacements[filepath].append(bad_url)

    if not replacements:
        print("No dead links to replace.")
        return

    print(f"Found dead links in {len(replacements)} files. Starting replacement...\n")

    for filepath, bad_urls in replacements.items():
        if not os.path.exists(filepath):
            print(f"Warning: File {filepath} not found, skipping.")
            continue
            
        print(f"Processing {filepath}...")
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        count = 0
        for bad_url in bad_urls:
            # Generate a unique placeholder URL to avoid browser caching issues
            # and to make them look different
            rand_id = random.randint(1, 10000)
            new_url = f"{PLACEHOLDER_BASE}?lock={rand_id}"
            
            if bad_url in content:
                content = content.replace(bad_url, new_url)
                print(f"  Replaced: {bad_url} -> {new_url}")
                count += 1
            else:
                print(f"  Warning: URL not found in file content: {bad_url}")
        
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Saved {count} changes.")
        else:
            print("  No changes made.")

    print("\nAll replacements complete.")

if __name__ == "__main__":
    main()
