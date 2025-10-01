from PIL import Image, ImageDraw, ImageFont
import os
import random

def create_racing_image(filename, text, width=800, height=600, color=(26, 26, 26)):
    """Create a racing placeholder image with text"""
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)
    
    # Draw some racing stripes
    stripe_color = (78, 255, 0)  # Green color
    stripe_width = width // 10
    for i in range(0, width, stripe_width * 2):
        draw.rectangle([i, 0, i + stripe_width, height], fill=stripe_color)
        
    # Try to get a font
    font_size = width // 20
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
        
    # Add text
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (font_size * len(text) // 2, font_size)
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Add a text background for better visibility
    text_bg = (0, 0, 0)
    draw.rectangle([
        position[0] - 10, 
        position[1] - 10, 
        position[0] + text_width + 10, 
        position[1] + text_height + 10
    ], fill=text_bg)
    
    draw.text(position, text, fill=(255, 255, 255), font=font)
    
    # Save the image
    img.save(filename)
    print(f"Created {filename}")
    
def create_helmet_image(filename, width=600, height=600):
    """Create a helmet placeholder image"""
    img = Image.new('RGB', (width, height), (26, 26, 26))
    draw = ImageDraw.Draw(img)
    
    # Draw a basic helmet shape
    helmet_color = (200, 200, 200)
    
    # Draw the main helmet shell
    draw.ellipse([width//4, height//4, 3*width//4, 3*height//4], fill=helmet_color)
    
    # Draw the visor area
    visor_color = (0, 0, 0)
    draw.rectangle([width//3, height//3, 2*width//3, height//2], fill=visor_color)
    
    # Add some green racing stripes
    stripe_color = (78, 255, 0)
    draw.rectangle([width//4, 2*height//5, 3*width//4, 2*height//5 + height//20], fill=stripe_color)
    
    # Save the image
    img.save(filename)
    print(f"Created {filename}")
    
def create_driver_image(filename, width=600, height=800):
    """Create a driver placeholder image"""
    img = Image.new('RGB', (width, height), (26, 26, 26))
    draw = ImageDraw.Draw(img)
    
    # Draw a basic driver silhouette
    # Head
    head_color = (200, 200, 200)
    draw.ellipse([width//3, height//8, 2*width//3, height//3], fill=head_color)
    
    # Body
    body_color = (78, 255, 0)  # Green racing suit
    draw.rectangle([width//3, height//3, 2*width//3, 3*height//4], fill=body_color)
    
    # Add racing team logo
    logo_color = (255, 255, 255)
    draw.rectangle([width//2 - width//10, height//2 - height//10, width//2 + width//10, height//2 + height//10], fill=logo_color)
    
    # Add text "MRAD RACING"
    text = "MRAD RACING"
    try:
        font = ImageFont.truetype("arial.ttf", width//20)
    except:
        font = ImageFont.load_default()
        
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (width//20 * len(text) // 2, width//20)
    draw.text(
        ((width - text_width) // 2, 3*height//4),
        text,
        fill=(255, 255, 255),
        font=font
    )
    
    # Save the image
    img.save(filename)
    print(f"Created {filename}")
    
def create_background_image(filename, width=1200, height=800):
    """Create a racing background image"""
    img = Image.new('RGB', (width, height), (10, 10, 10))
    draw = ImageDraw.Draw(img)
    
    # Draw a racetrack
    track_color = (50, 50, 50)
    draw.ellipse([width//10, height//4, 9*width//10, 3*height//4], outline=track_color, width=height//10)
    
    # Add some random racing elements
    for i in range(20):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(5, 20)
        draw.rectangle([x, y, x+size, y+size], fill=(78, 255, 0))
    
    # Save the image
    img.save(filename)
    print(f"Created {filename}")

def main():
    # Make sure the images directory exists
    images_dir = os.path.join(os.path.dirname(__file__), "images")
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    
    # Create racing images
    for i in range(1, 7):
        filename = os.path.join(images_dir, f"racing{i}.jpg")
        create_racing_image(filename, f"Racing Photo {i}")
    
    # Create helmet images
    for i in range(1, 3):
        filename = os.path.join(images_dir, f"helmet{i}.jpg")
        create_helmet_image(filename)
    
    # Create driver image
    driver_filename = os.path.join(images_dir, "driver1.jpg")
    create_driver_image(driver_filename)
    
    # Create background images
    for i in range(1, 3):
        filename = os.path.join(images_dir, f"background{i}.jpg")
        create_background_image(filename)
        
    # Create logo placeholder if they don't exist
    logo_files = ["m-logo.png", "mrad-wordmark.png"]
    for logo_file in logo_files:
        logo_path = os.path.join(images_dir, logo_file)
        if not os.path.exists(logo_path) or os.path.getsize(logo_path) == 0:
            img = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            if logo_file == "m-logo.png":
                # Create a simple M logo
                draw.polygon([(40, 160), (70, 40), (100, 100), (130, 40), (160, 160), (130, 160), (100, 80), (70, 160)], fill=(78, 255, 0))
            else:
                # Create a text logo
                try:
                    font = ImageFont.truetype("arial.ttf", 60)
                except:
                    font = ImageFont.load_default()
                draw.text((10, 70), "MRAD", fill=(78, 255, 0), font=font)
                
            img.save(logo_path)
            print(f"Created {logo_path}")

if __name__ == "__main__":
    main()