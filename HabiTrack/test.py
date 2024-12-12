from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import Database

class HabiTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HabiTrack")
        self.root.geometry("1000x600+230+70")
        self.root.config(background="#eefae5")
        self.root.resizable(0, 0)
        
        # Initialize Frames
        self.init_frames()
        self.init_buttons()
        self.pages = {}

        # Load default page
        self.set_active_page("StatusPage")

    def init_frames(self):
        """Initialize the main layout frames."""
        self.top_frame = CTkFrame(self.root, width=1000, height=50, fg_color="#1c2a19", corner_radius=0)
        self.top_frame.pack()

        self.left_frame = CTkFrame(self.root, width=150, height=600, fg_color="#3b4e21", corner_radius=0)
        self.left_frame.pack(side=LEFT)

        self.right_frame = CTkFrame(self.root, width=790, height=600, fg_color="#eefae5", corner_radius=0)
        self.right_frame.pack(side=RIGHT)

        # Load Images
        logo = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\New Folder\\logo.png')
        logo = logo.resize((280, 170))
        self.logo_photo = ImageTk.PhotoImage(logo)
        
        logo_label = CTkLabel(self.left_frame, image=self.logo_photo, text="")
        logo_label.grid(row=0, column=0, padx=10, pady=(20, 35))

    def init_buttons(self):
        """Initialize navigation buttons."""
        self.buttons = {}

        status_button = CTkButton(
            self.left_frame, height=40, text="STATUS", font=("bookman old style", 17),
            text_color="White", fg_color="#1c2a19", corner_radius=80,
            command=lambda: self.set_active_page("StatusPage")
        )
        status_button.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.buttons[status_button] = "StatusPage"

        track_button = CTkButton(
            self.left_frame, height=40, text="TRACK", font=("bookman old style", 17),
            text_color="White", fg_color="#1c2a19", corner_radius=80,
            command=lambda: self.set_active_page("TrackPage")
        )
        track_button.grid(row=2, column=0, padx=10, pady=(0, 20))
        self.buttons[track_button] = "TrackPage"

        sdg_button = CTkButton(
            self.left_frame, height=40, text="SDG", font=("bookman old style", 17),
            text_color="White", fg_color="#1c2a19", corner_radius=80,
            command=lambda: self.set_active_page("SDGPage")
        )
        sdg_button.grid(row=3, column=0, padx=10, pady=(0, 20))
        self.buttons[sdg_button] = "SDGPage"

    def set_active_page(self, page_name):
        """Switch between different pages."""
        for button, associated_page in self.buttons.items():
            if associated_page == page_name:
                button.configure(
                    fg_color="#bfd8af", text_color="#1c2a19",
                    font=("bookman old style", 17), hover_color="#bfd8af"
                )
            else:
                button.configure(
                    fg_color="#1c2a19", text_color="white",
                    font=("bookman old style", 17), hover_color="#bfd8af"
                )

        # Clear the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Load the appropriate page
        if page_name not in self.pages:
            self.pages[page_name] = globals()[page_name](self.right_frame)
        self.pages[page_name].display()


class StatusPage:
    def __init__(self, parent):
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Set up UI elements for the status page."""
        self.tracking_image = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\New Folder\\tracking.png')
        self.tracking_image = self.tracking_image.resize((1366, 850))
        self.tracking_photo = ImageTk.PhotoImage(self.tracking_image)

    def display(self):
        """Display the status page."""
        status_label = CTkLabel(self.parent, image=self.tracking_photo, text="")
        status_label.grid(row=0, column=0, padx=(0, 20))

        # Retrieve data
        species_counts = Database.get_species_count()
        counts = {"Avian Animals": 0, "Land Animals": 0, "Ocean Animals": 0}
        for species_type, count in species_counts:
            if species_type in counts:
                counts[species_type] = count

        # Display counts
        aviancount_label = CTkLabel(self.parent, text=str(counts["Avian Animals"]),
                                    font=('bookman old style', 80), fg_color='#cd9c3f')
        aviancount_label.place(relx=0.119, rely=0.190, anchor='center')

        landcount_label = CTkLabel(self.parent, text=str(counts["Land Animals"]),
                                    font=('bookman old style', 80), fg_color='#bda27b')
        landcount_label.place(relx=0.119, rely=0.53, anchor='center')

        oceancount_label = CTkLabel(self.parent, text=str(counts["Ocean Animals"]),
                                    font=('bookman old style', 80), fg_color='#2f54b4')
        oceancount_label.place(relx=0.119, rely=0.878, anchor='center')


class TrackPage:
    def __init__(self, parent):
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Set up UI elements for the track page."""
        # Create left and right frames and populate with elements
        pass

    def display(self):
        """Display the track page."""
        pass


class SDGPage:
    def __init__(self, parent):
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Set up UI elements for the SDG page."""
        pass

    def display(self):
        """Display the SDG page."""
        pass


# Main Application Execution
if __name__ == "__main__":
    root = CTk()
    app = HabiTrackApp(root)
    root.mainloop()
