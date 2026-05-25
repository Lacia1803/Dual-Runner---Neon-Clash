import re
path = r'Assets/Scenes/Credits.unity'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Clear ALL text components first
content = re.sub(r'm_Text: (.*)', 'm_Text: ', content)

def update_text_by_id(cid, text):
    global content
    pattern = r'(--- !u!114 &' + str(cid) + r'.*?m_Text: )(.*?)(?=\n)'
    content = re.sub(pattern, r'\1' + text, content, flags=re.DOTALL)

def center_rt_by_id(cid, y_offset=0):
    global content
    m_go = re.search(r'--- !u!114 &' + str(cid) + r'.*?m_GameObject: {fileID: (\d+)}', content, re.DOTALL)
    if m_go:
        goid = m_go.group(1)
        m_rt_id = re.search(r'--- !u!1 &' + goid + r'.*?- 224: {fileID: (\d+)}', content, re.DOTALL)
        if m_rt_id:
            rtid = m_rt_id.group(1)
            rt_pattern = r'(--- !u!224 &' + rtid + r'.*?\n)(.*?)(?=\n---)'
            m_rt = re.search(rt_pattern, content, re.DOTALL)
            if m_rt:
                rt_header, rt_body = m_rt.groups()
                rt_body = re.sub(r'm_AnchorMin: {x: [\d\.]+, y: [\d\.]+}', 'm_AnchorMin: {x: 0.5, y: 0.5}', rt_body)
                rt_body = re.sub(r'm_AnchorMax: {x: [\d\.]+, y: [\d\.]+}', 'm_AnchorMax: {x: 0.5, y: 0.5}', rt_body)
                rt_body = re.sub(r'm_AnchoredPosition: {x: [\-\d\.]+, y: [\-\d\.]+, z: [\-\d\.]+}', f'm_AnchoredPosition: {{x: 0, y: {y_offset}, z: 0}}', rt_body)
                rt_body = re.sub(r'm_SizeDelta: {x: [\d\.]+, y: [\d\.]+}', 'm_SizeDelta: {x: 800, y: 300}', rt_body)
                rt_body = re.sub(r'm_Pivot: {x: [\d\.]+, y: [\d\.]+}', 'm_Pivot: {x: 0.5, y: 0.5}', rt_body)
                content = content.replace(m_rt.group(0), rt_header + rt_body)

# Back to menu (1269224205)
update_text_by_id(1269224205, 'Back to Menu')

# Credits Title (984856136)
update_text_by_id(984856136, 'CREDITS')
center_rt_by_id(984856136, 180)

# Main Credit (1089901939)
# Use double backslash for literal \n in YAML string
styled_text = 'DEVELOPED BY\\n\\nLACIA PHUNG VO QUOC HIEN'
update_text_by_id(1089901939, f'"{styled_text}"')

# Set font size 40 and Alignment 4 (Center)
pattern_font = r'(--- !u!114 &1089901939.*?m_FontSize: )(\d+)'
content = re.sub(pattern_font, r'\1 40', content, flags=re.DOTALL)
pattern_align = r'(--- !u!114 &1089901939.*?m_Alignment: )(\d+)'
content = re.sub(pattern_align, r'\1 4', content, flags=re.DOTALL)

center_rt_by_id(1089901939, 0) # Center of screen

with open(path, 'w', encoding='utf-8', newline='') as f:
    f.write(content)

print("Credits cleaned and centered.")
