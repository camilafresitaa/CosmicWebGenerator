import tkinter as tk
import functions
import settings
import vpython as vp


# Function to update the cosmic web parameters when user changes parameters
def update_cosmic_web(new_num_filaments, new_iterations, new_density, new_universe_age):

    # Update global variables with new values
    settings.num_filaments = new_num_filaments
    settings.iterations = new_iterations
    settings.density = new_density
    settings.universe_age = new_universe_age

    # Schedules 'run_vpython' to execute immediately in the event loop
    window.after(0, functions.run_vpython)


# Graphical User Interface (GUI) with Tkinter
def create_gui():
    global window 

    # Create the main window
    window = tk.Tk()
    window.title("Cosmic Web Controls")
    window.geometry("600x750")
    window.config(bg = "black")
    window.resizable(True, True)

    # Create a main frame (light cream background)
    main_frame = tk.Frame(window, padx=50, pady=30, bg=settings.colors['cream'])
    main_frame.pack(fill='both', expand=True, padx=5, pady=5)

    # Title Label (Cosmic Web Controls)
    title_label = tk.Label(main_frame, text='Cosmic Web Controls', font=('Times New Roman', 50, 'bold'), 
                           bg=settings.colors['cream'], fg='black', anchor='center')
    # title_label.pack(pady=(0, 15))
    title_label.pack(pady=(0, 5))

    # Description Label
    description_label = tk.Label(main_frame, text="Adjust parameters to simulate the cosmic web and choose\nthe visual style of filaments and galaxies.", 
                                 font=("Times New Roman", 17),bg= settings.colors['cream'], fg='black', anchor='center')
    description_label.pack(pady=(0, 15))

    # Universe Age control
    frame_universe_age = tk.Frame(main_frame, bg=settings.colors['cream'], padx=5, pady=3)
    frame_universe_age.pack(fill="x", pady=(0, 15))

    label_universe_age = tk.Label(frame_universe_age, text="Universe Age", font=('Times New Roman', 20, 'bold'), bg=settings.colors['cream'], fg= 'black')
    label_universe_age.grid(row=0, column=0, padx=3, pady=3, sticky='w')

    scale_universe_age = tk.Scale(frame_universe_age, from_=0, to=1, orient='horizontal', bg=settings.colors['cream'], 
                                  sliderlength=20, length=100, width = 10, showvalue= 0,resolution= 0.1, 
                                  command=lambda x: [update_cosmic_web(settings.num_filaments, settings.iterations, settings.density, float(x)),
                                                     functions.update_value_label(scale_universe_age, value_label_universe_age)])
    scale_universe_age.grid(row=0, column=1, padx=7, pady=(7,0), sticky='ew')

    value_label_universe_age = tk.Label(frame_universe_age, text='0.0', font=('Times New Roman', 10), bg= settings.colors['cream'], fg='black', width=3)
    value_label_universe_age.grid(row=0, column=2, padx=(5, 0), sticky="w")

    desc_label_universe_age = tk.Label(frame_universe_age, text="Affects the expansion of filaments and the formation of galaxies.", 
                                       font=("Times New Roman", 15, "italic"), bg=settings.colors['cream'],fg='black')
    desc_label_universe_age.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=3)

    frame_universe_age.grid_columnconfigure(0, weight=0, minsize=200)  
    frame_universe_age.grid_columnconfigure(1, weight=1, minsize=200) 
    frame_universe_age.grid_columnconfigure(2, weight=0)

    frame_universe_age.grid_rowconfigure(0, weight=0)  
    frame_universe_age.grid_rowconfigure(1, weight=1)

    # Density control
    frame_density = tk.Frame(main_frame, bg= settings.colors['cream'], padx=5, pady=3)
    frame_density.pack(fill="x", pady=(0, 15))

    label_density = tk.Label(frame_density, text="Density", font=("Times New Roman", 20, "bold"), bg=settings.colors['cream'], fg="black")
    label_density.grid(row=0, column=0, padx=3, pady=3, sticky="w")

    scale_density = tk.Scale(frame_density, from_=0.1, to=1, orient=tk.HORIZONTAL, bg=settings.colors['cream'], sliderlength=20, length=100, width=10, showvalue=0,
                            resolution=0.1, command=lambda x: [update_cosmic_web(settings.num_filaments, settings.iterations,  float(x), settings.universe_age), 
                                                               functions.update_value_label(scale_density, value_label_density)])
    scale_density.grid(row=0, column=1, padx=7, pady=(7,0), sticky="ew")

    value_label_density = tk.Label(frame_density, text="0.1", font=("Times New Roman", 10), bg=settings.colors['cream'], fg="black", width=3)
    value_label_density.grid(row=0, column=2, padx=(5, 0), sticky="w")

    desc_label_density = tk.Label(frame_density, text="Defines how compact the filaments are within the cosmic web.", font=("Times New Roman", 15, "italic"), bg=settings.colors['cream'], fg="black")
    desc_label_density.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=3)

    frame_density.grid_columnconfigure(0, weight=0, minsize=200)  
    frame_density.grid_columnconfigure(1, weight=1, minsize=200) 
    frame_density.grid_columnconfigure(2, weight=0)

    frame_density.grid_rowconfigure(0, weight=0)  
    frame_density.grid_rowconfigure(1, weight=1)

    # Number of Filaments control
    frame_filaments = tk.Frame(main_frame, bg=settings.colors['cream'], padx=5, pady=3)
    frame_filaments.pack(fill="x", pady=(0, 15))    

    label_filaments = tk.Label(frame_filaments, text="Number of Filaments", font=("Times New Roman", 20, "bold"), bg=settings.colors['cream'], fg="black")
    label_filaments.grid(row=0, column=0, padx=3, pady=3, sticky="w") 

    scale_filaments = tk.Scale(frame_filaments, from_=0, to=30, orient=tk.HORIZONTAL, bg=settings.colors['cream'], sliderlength=20, length=100, width=10, showvalue=0,
                            resolution=1, command=lambda x: [update_cosmic_web(int(x), settings.iterations, settings.density, settings.universe_age), 
                                                             functions.update_value_label(scale_filaments, value_label_filaments)])
    scale_filaments.grid(row=0, column=1, padx=7, pady=(7,0), sticky="ew")
    
    value_label_filaments = tk.Label(frame_filaments, text="0", font=("Times New Roman", 10), bg=settings.colors['cream'], fg="black", width=3)
    value_label_filaments.grid(row=0, column=2, padx=(5, 0), sticky="w")

    desc_label_filaments = tk.Label(frame_filaments, text="Determines the number of filament structures in the cosmic web.", font=("Times New Roman", 15, "italic"), 
                                    bg=settings.colors['cream'], fg="black")
    desc_label_filaments.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=3)
       
    frame_filaments.grid_columnconfigure(0, weight=0, minsize=200)  
    frame_filaments.grid_columnconfigure(1, weight=1, minsize=200) 
    frame_filaments.grid_columnconfigure(2, weight=0)
        
    frame_filaments.grid_rowconfigure(0, weight=0)  
    frame_filaments.grid_rowconfigure(1, weight=1)

    # Iterations control
    frame_iterations = tk.Frame(main_frame, bg=settings.colors['cream'], padx=5, pady=3)
    frame_iterations.pack(fill="x", pady=(0, 15))

    label_iterations = tk.Label(frame_iterations, text="Iterations", font=("Times New Roman", 20, "bold"), bg=settings.colors['cream'], fg="black")
    label_iterations.grid(row=0, column=0, padx=3, pady=3, sticky="w")

    scale_iterations = tk.Scale(frame_iterations, from_=1, to=5, orient=tk.HORIZONTAL, bg=settings.colors['cream'], sliderlength=20, length=100, width=10, showvalue=0,
                                command=lambda x: [update_cosmic_web(settings.num_filaments, int(x), settings.density, settings.universe_age), 
                                                   functions.update_value_label(scale_iterations, value_label_iterations)])
    scale_iterations.grid(row=0, column=1, padx=7, pady=(7,0), sticky="ew")

    value_label_iterations = tk.Label(frame_iterations, text="1", font=("Times New Roman", 10), bg=settings.colors['cream'], fg="black", width=3)
    value_label_iterations.grid(row=0, column=2, padx=(5, 0), sticky="w")

    desc_label_iterations = tk.Label(frame_iterations, text="Controls the depth of the fractal filaments.", font=("Times New Roman", 15, "italic"), bg=settings.colors['cream'], fg="black")
    desc_label_iterations.grid(row=1, column=0, padx=3, pady=3, sticky="w", columnspan=3)

    frame_iterations.grid_columnconfigure(0, weight=0, minsize=200)  
    frame_iterations.grid_columnconfigure(1, weight=1, minsize=200) 
    frame_iterations.grid_columnconfigure(2, weight=0)

    frame_iterations.grid_rowconfigure(0, weight=0)  
    frame_iterations.grid_rowconfigure(1, weight=1)

    # Zoom control
    frame_zoom = tk.Frame(main_frame, bg=settings.colors['cream'], padx=5, pady=3)
    frame_zoom.pack(fill="x", pady=(0, 15))

    label_zoom = tk.Label(frame_zoom, text="Zoom", font=("Times New Roman", 20, "bold"),
                          bg=settings.colors['cream'], fg="black")
    label_zoom.grid(row=0, column=0, padx=3, pady=3, sticky="w")

    scale_zoom = tk.Scale(frame_zoom, from_=25, to=1, orient=tk.HORIZONTAL,
                          bg=settings.colors['cream'], sliderlength=20,
                          length=100, width=10, showvalue=0,
                          command=functions.update_zoom)
    scale_zoom.set(25)
    scale_zoom.grid(row=0, column=1, padx=7, pady=(7,0), sticky="ew")

    value_label_zoom = tk.Label(frame_zoom, text="", font=("Times New Roman", 10),
                                bg=settings.colors['cream'], fg="black", width=3)
    value_label_zoom.grid(row=0, column=2, padx=(5, 0), sticky="w")

    frame_zoom.grid_columnconfigure(0, weight=0, minsize=200)  
    frame_zoom.grid_columnconfigure(1, weight=1, minsize=200) 
    frame_zoom.grid_columnconfigure(2, weight=0)

    frame_zoom.grid_rowconfigure(0, weight=0)  
    frame_zoom.grid_rowconfigure(1, weight=1)

    # Radiobutton variable
    radvar = tk.StringVar(value="Style 1")

    # Radiobutton frame
    button_frame = tk.Frame(main_frame, bg=settings.colors['cream'], pady=5)
    button_frame.pack(fill="x", pady=(15, 0))

    button_frame.grid_columnconfigure(0, weight=1, uniform="equal")
    button_frame.grid_columnconfigure(1, weight=1, uniform="equal")
    button_frame.grid_columnconfigure(2, weight=1, uniform="equal")

    # Style 1 radiobutton
    style1_radio = tk.Radiobutton(button_frame, text="Style 1", font=("Times New Roman", 20, "bold"), pady=10, padx=10,
                                fg="white",
                                bg=settings.colors['grey'],
                                bd=0.45,
                                selectcolor="black",

                                variable=radvar,
                                value="Style 1",
                                command=functions.set_style_1)
    style1_radio.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

    # Style 2 radiobutton
    style2_radio = tk.Radiobutton(button_frame, text="Style 2", font=("Times New Roman", 20, "bold"), pady=10,
                                fg="white",
                                bg=settings.colors['grey'],
                                bd=0.45,

                                variable=radvar,
                                value="Style 2",
                                command=functions.set_style_2)
    style2_radio.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    #Style 3 radiobutton
    style3_radio = tk.Radiobutton(button_frame, text="Style 3", font=("Times New Roman", 20, "bold"), pady=10,
                                fg="white",
                                bg=settings.colors['grey'],
                                bd=0.45,
                                
                                variable=radvar,
                                value="Style 3",
                                command=functions.set_style_3)
    style3_radio.grid(row=0, column=2, padx=10, pady=5, sticky="ew")

    def take_screenshot():
        settings.scene.capture("Cosmic_Web_Generator")
        screenshot_button.pack(fill='both', expand=True, padx=10, pady=5)

    # Screenshot frame
    screenshot_frame = tk.Frame(main_frame, bg=settings.colors['cream'], pady=5)
    screenshot_frame.pack(fill="x", pady=(15, 0))

    screenshot_frame.grid_columnconfigure(0, weight=1, uniform="equal")
    screenshot_frame.grid_columnconfigure(1, weight=1, uniform="equal")
    screenshot_frame.grid_columnconfigure(2, weight=1, uniform="equal")

    # Screenshot button
    screenshot_button = tk.Button(screenshot_frame, text="Capture your creation!",
                                font=("Times New Roman", 18), pady=10,
                                fg="white",
                                bg=settings.colors['grey'],
                                bd=0,
                                activeforeground="white",
                                activebackground=settings.colors['grey'],
                                highlightbackground=settings.colors['grey'],
                                highlightthickness=0,

                                command=take_screenshot)
    
    screenshot_button.pack(fill='both', expand=True, padx=10, pady=5)

    # Start VPython in the main thread
    window.after(0, functions.run_vpython)

    window.mainloop()


# Initialize settings
settings.init()

# Create the graphical user interface (GUI)
create_gui()