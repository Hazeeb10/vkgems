from PIL import Image

def make_solid_color(img_path, target_color=(255, 102, 0)):
    try:
        img = Image.open(img_path).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # item[3] is the alpha channel.
            # If it's completely transparent, leave it alone.
            # If it has any opacity, we change its RGB to the target color
            # but keep the original opacity (alpha) for smooth edges.
            if item[3] > 0:
                newData.append((target_color[0], target_color[1], target_color[2], item[3]))
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save(img_path, "PNG")
        print(f"Successfully converted {img_path} to flat orange.")
    except Exception as e:
        print(f"Failed {img_path}: {e}")

if __name__ == "__main__":
    # We apply this to the current transparent logos
    make_solid_color("public/images/logo.png")
    make_solid_color("public/images/new logo.png")
