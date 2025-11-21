#!/bin/bash
# Image Conversion Script for Jekyll
# Converts images to WebP and AVIF formats for better web performance
# Usage: ./convert-images.sh <input_directory>

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if vips is installed
if ! command -v vips &> /dev/null; then
    echo -e "${RED}Error: vips is not installed${NC}"
    echo "Install it with: brew install libvips"
    exit 1
fi

# Get input directory
INPUT_DIR="${1:-assets/images}"

if [ ! -d "$INPUT_DIR" ]; then
    echo -e "${RED}Error: Directory $INPUT_DIR does not exist${NC}"
    exit 1
fi

echo -e "${GREEN}Converting images in: $INPUT_DIR${NC}"
echo ""

# Find all jpg, jpeg, and png files
find "$INPUT_DIR" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) | while read -r file; do
    # Get filename without extension
    filename="${file%.*}"
    extension="${file##*.}"
    
    echo -e "${YELLOW}Processing: $file${NC}"
    
    # Convert to WebP
    if [ ! -f "${filename}.webp" ]; then
        vips copy "$file" "${filename}.webp[Q=80]"
        echo -e "  ${GREEN}✓${NC} Created ${filename}.webp"
    else
        echo -e "  ${YELLOW}⊘${NC} ${filename}.webp already exists"
    fi
    
    # Convert to AVIF
    if [ ! -f "${filename}.avif" ]; then
        vips copy "$file" "${filename}.avif[Q=75]"
        echo -e "  ${GREEN}✓${NC} Created ${filename}.avif"
    else
        echo -e "  ${YELLOW}⊘${NC} ${filename}.avif already exists"
    fi
    
    echo ""
done

echo -e "${GREEN}Conversion complete!${NC}"
echo ""
echo "Usage in HTML:"
echo '<picture>'
echo '  <source srcset="image.avif" type="image/avif">'
echo '  <source srcset="image.webp" type="image/webp">'
echo '  <img src="image.jpg" alt="Description" loading="lazy">'
echo '</picture>'
