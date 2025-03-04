import vpython as vp


# Styles
style_1 = {'filament_color': vp.color.white, 'galaxy_color': vp.color.yellow, 'star_color': vp.color.white}
style_2 = {'filament_color': vp.color.blue, 'galaxy_color': vp.color.cyan, 'star_color': vp.color.white}
style_3 = {'filament_color': vp.color.red, 'galaxy_color': vp.color.green, 'star_color': vp.color.white}


# Colors
colors = {'cream': "#faf4ee", 'grey': "#3d3d3d"}


# Initialize and globalise variables
def init():
    global info_text, current_style, num_filaments, iterations, density, universe_age, filaments, galaxies, stars, stars_background
    
    info_text = None
    current_style = style_1

    # Adjustable parameters
    num_filaments = 0
    iterations = 1
    density = 0.1
    universe_age = 0

    # Lists for objects
    filaments = []
    galaxies = []
    stars = []
    stars_background = []


# Set constant for minimum age for galaxies to show
MIN_UNIVERSE_AGE = 0.2


# Vpython canvas
scene = vp.canvas(width=1200, height=650, background=vp.color.black)
scene.lights = []
scene.userzoom = False
scene.title = "<h1 style='font-family: Times New Roman; font-size: 30px;'>Cosmic Web Generator</h1>"
scene.caption = """
<div style="font-family: 'Times New Roman'; font-size: 18px; margin: 0; padding: 0;">
  <b>Controls:</b>
  - Use the <b>right mouse button</b> to rotate the view.
  - Use the <b>controls panel</b> to adjust parameters and styles in real time.
  - Experiment with colors, sizes, and fractal depth!<br>

  <b>Created by:</b>
  Fae Jordaan, Camila Medrano, Anastasiia Korolenko and Raya Mouri.

</div>
"""