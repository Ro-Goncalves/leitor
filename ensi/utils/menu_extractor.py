def extract_menu_content(text, menu_title):
    """
    Extracts content associated with a specific menu title from text.
    
    Args:
        text (str): The full text to search in
        menu_title (str): The menu title to look for (e.g., '## Kaihua Ni')
        
    Returns:
        str: The content associated with the menu title, or None if not found
    """
    # Split the text into lines
    lines = text.split('\n')
    
    # Find the index of the menu title
    menu_index = -1
    for i, line in enumerate(lines):
        if line.strip() == menu_title:
            menu_index = i
            break
    
    # If menu title not found, return None
    if menu_index == -1:
        return None
    
    # Get the content (next line after the menu title)
    # Keep concatenating lines until we hit another header or empty line
    content = []
    i = menu_index + 1
    
    while i < len(lines):
        
        if lines[i].startswith('##'):
            break
        
        if lines[i].strip() != '':
            content.append(lines[i].strip())
            
        i += 1
    
    return ' '.join(content) if content else None