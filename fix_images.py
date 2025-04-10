import os
import re
import json

def convert_image_block(content):
    # Convert [block:image] format to standard markdown
    def replace_block(match):
        block_content = match.group(1)
        try:
            # Parse the JSON content
            data = json.loads(block_content)
            if isinstance(data, dict) and 'images' in data:
                image_data = data['images'][0]
                if isinstance(image_data, dict) and 'image' in image_data:
                    image_url = image_data['image'][0]
                    alt_text = image_data['image'][2] if len(image_data['image']) > 2 else ''
                    caption = image_data.get('caption', '')
                    
                    # Create standard markdown image
                    result = f'![{alt_text}]({image_url})'
                    if caption:
                        result += f'\n\n*{caption}*'
                    return result
        except:
            pass
        return match.group(0)

    # Replace all [block:image] blocks
    pattern = r'\[block:image\](.*?)\[/block\]'
    content = re.sub(pattern, replace_block, content, flags=re.DOTALL)
    return content

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert image blocks
    new_content = convert_image_block(content)
    
    # Write back if changes were made
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

def main():
    # Process all markdown files in docs directory
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == '__main__':
    main() 