from PIL import Image
import math

def process_img(input_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Distance to white
            dist = math.sqrt((255 - item[0])**2 + (255 - item[1])**2 + (255 - item[2])**2)
            
            if dist < 20:
                # Very close to white -> transparent
                newData.append((255, 255, 255, 0))
            elif dist < 80:
                # Anti-aliasing edge -> semi transparent
                alpha = int(((dist - 20) / 60) * 255)
                # We blend the original color but make it partially transparent
                newData.append((item[0], item[1], item[2], alpha))
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save(input_path, "PNG")
        print(f"Successfully processed {input_path}")
    except Exception as e:
        print(f"Failed {input_path}: {e}")

if __name__ == "__main__":
    process_img("public/images/logo.png")
    process_img("public/images/new logo.png")
