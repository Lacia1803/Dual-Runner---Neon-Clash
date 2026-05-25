from pathlib import Path

def fix_unity_scene_v3(path):
    print(f"Fixing {path}")
    # Read as bytes to handle everything correctly
    data = Path(path).read_bytes()
    
    # Remove BOM if present
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]
    
    # Convert to string for easier processing
    # Using utf-8 and replacing errors just in case
    content = data.decode('utf-8', errors='ignore')
    
    # Standardize line endings to LF first
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            new_lines.append(line.rstrip())
    
    # Join with LF (as seen in Loading.unity)
    final_content = '\n'.join(new_lines) + '\n'
    
    # Write back as UTF-8 WITHOUT BOM
    Path(path).write_bytes(final_content.encode('utf-8'))
    print(f"Done {path}")

scenes = [
    r"c:\Users\Lacia\Downloads\Agate-Game-Project-master\Agate-Game-Project-master\Assets\Scenes\MainMenu.unity",
    r"c:\Users\Lacia\Downloads\Agate-Game-Project-master\Agate-Game-Project-master\Assets\Scenes\Credits.unity"
]

for s in scenes:
    if Path(s).exists():
        fix_unity_scene_v3(s)
