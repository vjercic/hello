import re

def parse_greetings(file_path):
    """
    Parse a text file containing language greetings and optional pronunciations.
    
    Each line is expected to be in the format:
    Language: Greeting (Pronunciation)
    
    Where the pronunciation (using the phonetic alphabet) in parentheses is optional.
    
    Returns a list of dictionaries containing:
    - language: The language name
    - greeting: The greeting in that language
    - pronunciation: The pronunciation (if available, otherwise None)
    """
    results = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    for line in content.strip().split('\n'):
        if not line.strip():  # skip empty lines
            continue
            
        # Pattern to extract language, greeting, and optional pronunciation
        pattern = r'([^:]+):\s+([^(]+?)(?:\s+\(([^)]+)\))?$'
        
        match = re.match(pattern, line.strip())
        if match:
            language = match.group(1).strip()
            greeting = match.group(2).strip()
            pronunciation = match.group(3).strip() if match.group(3) else None
            
            results.append({
                'language': language,
                'greeting': greeting,
                'pronunciation': pronunciation
            })
    
    return results

if __name__ == "__main__":
    file_path = "hello.txt"
    greetings = parse_greetings(file_path)
    
    for greeting in greetings:
        print(f"Language: {greeting['language']}")
        print(f"Greeting: {greeting['greeting']}")
        if greeting['pronunciation']:
            print(f"Pronunciation: {greeting['pronunciation']}")
        print()

