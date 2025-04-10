import os
import yaml

def get_md_files(directory):
    """Get all markdown files in a directory and its subdirectories."""
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, file), directory)
                md_files.append(rel_path)
    return sorted(md_files)

def create_navigation_structure():
    docs_dir = 'docs'
    navigation = []
    
    # Get all top-level directories in docs
    top_level_dirs = [d for d in os.listdir(docs_dir) 
                     if os.path.isdir(os.path.join(docs_dir, d)) 
                     and d != 'Houseware API'  # Exclude Houseware API
                     and d != '.git']  # Exclude .git directory
    
    # Sort directories for consistent navigation, but ensure Overview is first
    top_level_dirs.sort()
    if 'Overview' in top_level_dirs:
        top_level_dirs.remove('Overview')
        top_level_dirs.insert(0, 'Overview')
    
    for dir_name in top_level_dirs:
        dir_path = os.path.join(docs_dir, dir_name)
        
        # Create section for each top-level directory
        section = {
            'title': dir_name,
            'children': []
        }
        
        # Get all markdown files in this directory and its subdirectories
        md_files = get_md_files(dir_path)
        
        # Add each markdown file as a child
        for md_file in md_files:
            # Convert file path to URL format
            url = f'/docs/{dir_name}/{md_file}'
            # Get title from the first markdown file in each directory
            title = os.path.splitext(os.path.basename(md_file))[0].replace('-', ' ').title()
            
            section['children'].append({
                'title': title,
                'url': url
            })
        
        navigation.append(section)
    
    return navigation

def main():
    # Generate navigation structure
    navigation = create_navigation_structure()
    
    # Write to _navigation.yml
    with open('_navigation.yml', 'w') as f:
        yaml.dump(navigation, f, default_flow_style=False, sort_keys=False)
    
    print("Navigation structure has been generated in _navigation.yml")

if __name__ == '__main__':
    main() 