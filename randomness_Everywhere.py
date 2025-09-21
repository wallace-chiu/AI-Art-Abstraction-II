import random
from PIL import Image, ImageDraw, ImageFont

for iterator in range (10):
    # Set a random canvas size (width x height)
    canvas_size = (random.randint(1000, 4000), random.randint(600, 2000))

    # Create the image
    img = Image.new('RGB', canvas_size, color='white')
    d = ImageDraw.Draw(img)

    # Define some fonts for the text
    font_sizes = [10, 20, 30, 40]
    fonts = ['Arial.ttf', 'Times New Roman.ttf']
    colors = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) for _ in range(5)]

    # Function to draw a random shape
    def draw_shape(d, x, y):
        shape_type = random.choice(['circle', 'square', 'triangle'])
        size = (random.randint(10, 200), random.randint(10, 200))
        
        if shape_type == 'circle':
            d.ellipse((x-size[0]//2, y-size[1]//2,
                       x+size[0]//2, y+size[1]//2),
                      fill=random.choice(colors))
        elif shape_type == 'square':
            d.rectangle((x-size[0]//2, y-size[1]//2,
                         x+size[0]//2, y+size[1]//2),
                        fill=random.choice(colors))
        else:  # triangle
            points = [(x+size[0]//4, y), (x+size[0]*3//4, y), (x+random.randint(0,size[0]//2), y-size[1]//2)]
            d.polygon(points, fill=random.choice(colors))

    # Function to draw random text
    def draw_text(d, x, y):
        font_size = random.choice(font_sizes)
        font = ImageFont.truetype(random.choice(fonts), font_size)
        
        words = ["RANDOM", "ART", "CHAOS", "FUN", "SURREALISM"]
        for _ in range(random.randint(5, 15)):
            word = random.choice(words)
            d.text((x, y), word, fill=random.choice(colors), font=font)
            x += random.randint(-20, 50)

    # Draw shapes and text randomly
    for i in range(random.randint(100, 1000)):
        x = random.randint(0, canvas_size[0])
        y = random.randint(0, canvas_size[1])
        
        if random.random() < 0.7:
            draw_shape(d, x, y)
        else:
            draw_text(d, x, y)

    # Save the image
    img.save('RANDOMNESS_EVERYWHERE_' + str(iterator) + '.png')
