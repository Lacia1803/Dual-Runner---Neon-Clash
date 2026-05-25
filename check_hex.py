def print_hex(name, path):
    print(f"Hex for {name} ({path}):")
    try:
        with open(path, 'rb') as f:
            data = f.read(200)
            print(data.hex(' '))
    except Exception as e:
        print(e)

print_hex("Loading", r"c:\Users\Lacia\Downloads\Agate-Game-Project-master\Agate-Game-Project-master\Assets\Scenes\Loading.unity")
print_hex("MainMenu", r"c:\Users\Lacia\Downloads\Agate-Game-Project-master\Agate-Game-Project-master\Assets\Scenes\MainMenu.unity")
