import vpython as vp
import random
import settings


# Creates background starts
def create_stars_background():
    if settings.universe_age > 0:
        num_stars_background = int(100 * settings.universe_age)
        for i in range(num_stars_background):
            x = random.uniform(-5, 5)
            y = random.uniform(-5, 5)
            z = random.uniform(-5, 5)
            star = vp.sphere(pos=vp.vector(x, y, z),
                    radius=0.01, color=vp.color.white,
                    emissive=True, opacity=0.5)
            settings.stars_background.append(star)


# Creates stars on the filaments
def create_star(position):
    size = random.uniform(0.015, 0.025)
    star = vp.sphere(pos=position, radius=size, color=vp.color.white, emissive=True, opacity=random.uniform(0.5, 0.7))
    settings.stars.append(star)


# Creates galaxies
def create_galaxy(position):
    size = random.uniform(0.05, 0.1)
    galaxy = vp.sphere(pos=position, radius=size, color=settings.current_style['galaxy_color'], emissive=True, opacity=random.uniform(0.7, 0.8))
    settings.galaxies.append(galaxy)


# Creates filaments
def create_filament(position, length, iterations, density, age_factor):
    if iterations > 0:

        adjusted_length = length * (1 + (1 - density) * 2) * (1 + 0.3 * age_factor) # Adjust filament's length based on density and age_factor
        direction = vp.vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1))  # Random direction for the filament
        direction = vp.norm(direction)
        end = position + direction * adjusted_length
        current_position = position  # Track the position as we create each segment of the filament
        current_direction = direction  # Initialize current direction

        for i in range(15): # Number of segments (15)
            segment_length = (vp.mag(end - position) / 10) * 0.8  # Calculate segment length and reduce by 80% (for a finer structure)
            curve = vp.vector(random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6), random.uniform(-0.6, 0.6)) # Add random curve to each segment's direction
            current_direction = vp.norm(current_direction + curve * 0.6)
            segment_end = current_position + current_direction * segment_length  # Calculate the end position of the current segment
            filament_seg = vp.cylinder(pos=current_position,
                            axis=segment_end - current_position,
                            radius=0.01 * (1 + (1 - density)),
                            color=settings.current_style['filament_color'])
            settings.filaments.append(filament_seg)
            current_position = segment_end # Update current position to the end of this segment

            # Randomly place 1 to 3 stars along this segment
            num_stars = random.randint(1, 3)
            for _ in range(num_stars):
                star_position = current_position + current_direction * random.uniform(0, segment_length)
                create_star(star_position)

        # If universe's age is large enough, create galaxies at the start and end points of the filament
        if age_factor >= settings.MIN_UNIVERSE_AGE:
            create_galaxy(position)
            create_galaxy(current_position)
    
        # Recursively create two new filaments from the end of the current filament
        create_filament(current_position, adjusted_length * 0.5, iterations - 1, density, age_factor)
        create_filament(current_position, adjusted_length * 0.5, iterations - 1, density, age_factor)


# Removes all the elements in the scene
def clear_scene():
    for obj in settings.filaments + settings.galaxies + settings.stars + settings.stars_background:
        obj.visible = False
    settings.filaments.clear()
    settings.galaxies.clear()
    settings.stars.clear()
    settings.stars_background.clear()


# Clear the scene and generates filaments based on user-defined parameters (if parameters are sufficient)
def run_vpython():
    clear_scene()

    # Check if the parameters are valid for creating background stars
    if settings.universe_age > 0:
        # Create background stars
        create_stars_background()
        if settings.info_text is not None:
            settings.info_text.visible = False
            settings.info_text = None
        
    else:
        if settings.info_text is None:
            settings.info_text = vp.text(text = 'Adjust the parameters to see the objects', depth = 0,
                                         height = 1.2, color = vp.color.white, align = "center", billboard = True)

    # Check if the parameters are valid for creating filaments
    if settings.num_filaments > 0 and settings.iterations > 0 and settings.universe_age > 0:
        for i in range(settings.num_filaments):

            # Generate a random starting position
            x = random.uniform(-2.5, 2.5) 
            y = random.uniform(-2.5, 2.5)
            z = random.uniform(-2.5, 2.5)
            position = vp.norm(vp.vector(x, y, z))

            # Create a filament starting from this position
            create_filament(position, 1, settings.iterations, settings.density, settings.universe_age)


# Function to update zoom value
def update_zoom(valor):
    zoom = float(valor)
    settings.scene.camera.pos = vp.vector(0, 0, zoom)
    settings.scene.camera.axis = vp.vector(0, 0, -zoom)


# Function to update the label displaying the value of a scale widget
def update_value_label(scale, value_label):
    value_label.config(text=str(round(scale.get(), 1)))


# Function to update the colors of objects based on the current style
def update_object_colors(new_style):
    for filament in settings.filaments:
        filament.color = new_style['filament_color']

    for galaxy in settings.galaxies:
        galaxy.color = new_style['galaxy_color']

    for star in settings.stars:
        star.color = new_style['star_color']


# Function to change the style to 'style_1'
def set_style_1():
    settings.current_style = settings.style_1
    update_object_colors(settings.current_style)

# Function to change the style to 'style_2'
def set_style_2():
    settings.current_style = settings.style_2
    update_object_colors(settings.current_style)

# Function to change the style to 'style_3'
def set_style_3():
    settings.current_style = settings.style_3
    update_object_colors(settings.current_style)
