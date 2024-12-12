from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import Database
import Login

def main():

    root = CTk()

    # FUNCTIONS
    def set_active_page(active_page):
        for button, page_name in buttons.items():
            if page_name == active_page:
                button.configure(fg_color="#bfd8af", text_color="#1c2a19",font=("bookman old style", 17), hover_color="#bfd8af")  # Active style
            else:
                button.configure(fg_color="#1c2a19", text_color="white",font=("bookman old style", 17), hover_color="#bfd8af")  # Inactive style
        update_right_frame(active_page)

    #function for updating the right side frame whenever a button is clicked
    def update_right_frame(page_name):
        for widget in rightFrame.winfo_children():
            widget.destroy()
        if page_name == "status_page":
            status_page()
        elif page_name == "track_page":
            track_page()
        elif page_name == "sdg_page":
            sdg_page()

    #function for the status page, consists of the number of species in the system.
    def status_page():
        species_counts = Database.get_species_count()
        counts = {"Avian Animals": 0, "Land Animals": 0, "Ocean Animals": 0}
        
        for species_type, count in species_counts:
            if species_type in counts:
                counts[species_type] = count

        statusLabel = CTkLabel(rightFrame, image=trackingPhoto, text="")
        statusLabel.grid(row=0, column=0, padx=(0, 20))

        aviancount_label = CTkLabel(rightFrame, text=str(counts["Avian Animals"]),font=('bookman old style', 80), fg_color='#cd9c3f')
        aviancount_label.place(relx=0.119, rely=0.190, anchor='center')

        landcount_label = CTkLabel(rightFrame, text=str(counts["Land Animals"]),font=('bookman old style', 80), fg_color='#bda27b')
        landcount_label.place(relx=0.119, rely=0.53, anchor='center')

        oceancount_label = CTkLabel(rightFrame, text=str(counts["Ocean Animals"]),font=('bookman old style', 80), fg_color='#2f54b4')
        oceancount_label.place(relx=0.119, rely=0.878, anchor='center')

    #function for showing all of the data when a data is selected
    def show_all():
        treeview_data()
        searchEntry.delete(0,END)
        searchBox.set('Search By')

    #function for searching a specific data in the track page
    def search_track():
        if searchEntry.get()=='':
            messagebox.showerror('Error', "Enter a value to search")
        elif searchBox.get()=='Search by':
            messagebox.showerror('Error', "Please select an option")
        else: 
            searched_track = Database.search(searchBox.get(),searchEntry.get())
            tree.delete(*tree.get_children())
            for tracks in searched_track:
                tree.insert('', 'end', values=(tracks[0], tracks[3], tracks[4], tracks[5], tracks[1], tracks[2]))

    #function for deletion of data in the view box
    def delete_track():
        selected_track = tree.selection()
        if not selected_track:
            messagebox.showerror('Error', 'Select a track to delete')
        else:
            Database.delete(trackingIDEntry.get())
            treeview_data()
            clear()
            messagebox.showerror('Error', "Data is deleted")

    #function for updating the data in the view box
    def update_track():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Error', "Select data to update")
        else:
            Database.update(nameEntry.get(),addressEntry.get(), typeBox.get(), speciesEntry.get(), numofSpeciesEntry.get(),trackingIDEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo("Success", "Data is updated")

    #function for selecting a data for it to be updated or deleted or as the user wants
    def selection(event):
        selected_item = tree.selection()
        if selected_item:
            row = tree.item(selected_item)['values']
            clear()
            trackingIDEntry.insert(0,row[0])
            nameEntry.insert(0,row[4])
            addressEntry.insert(0,row[5])
            typeBox.set(row[1])
            speciesEntry.insert(0,row[2])
            numofSpeciesEntry.insert(0,row[3])

    #function for displaying the view box.
    def treeview_data():
        track = Database.fetch_tracks()
        tree.delete(*tree.get_children())
        for tracks in track:
            tree.insert('', 'end', values=(tracks[0], tracks[3], tracks[4], tracks[5], tracks[1], tracks[2]))

    # fuunction for clearing the entry fields so that you don't have to manually remove them one by one
    def clear(value=False):
        if value:
            tree.selection_remove(tree.focus())
        trackingIDEntry.delete(0,END)
        nameEntry.delete(0,END)
        addressEntry.delete(0,END)
        speciesEntry.delete(0,END)
        typeBox.set("")
        numofSpeciesEntry.delete(0,END)

    # function for inserting a track in the view box and in the sql database
    def add_track():
        if trackingIDEntry.get()=='' or nameEntry.get()=='' or addressEntry.get()=='' or speciesEntry.get()=='' or numofSpeciesEntry.get()=='':
            messagebox.showerror('Error', 'All fields are required')
        elif Database.id_exists(trackingIDEntry.get()):
            messagebox.showerror('Error', 'Id already exists')
        else:
            Database.insert(trackingIDEntry.get(),nameEntry.get(),addressEntry.get(), typeBox.get(),speciesEntry.get(),numofSpeciesEntry.get())
            treeview_data()
            messagebox.showinfo('Success', "Data is added")

    def sdg_page():
        sdgLabel = CTkLabel(rightFrame, image=sdgPhoto, text="")
        sdgLabel.grid(row=0, column=0, padx=(0, 20))
        

    # a function for the track page, this handles all of the styles, buttons, entry points,  and the whole output of the track page
    def track_page():
        global trackingIDEntry, nameEntry, addressEntry, speciesEntry, numofSpeciesEntry, typeBox, tree, searchEntry, searchBox

        leftsideFrame = CTkFrame(rightFrame, width=200, height=520, fg_color="#d0f0c0")
        leftsideFrame.grid(row=0, column=0, padx=(8,0))

        trackingIDLabel = CTkLabel(leftsideFrame, text="TrackingID" , font=("bookman old style",15,"bold"), text_color="Black")
        trackingIDLabel.grid(row=0, column=0, pady=(25,0))

        trackingIDEntry = CTkEntry(leftsideFrame, font=("bookman old style", 15,"bold"),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        trackingIDEntry.grid(row=0, column=1,pady=(25,0))

        nameLabel = CTkLabel(leftsideFrame, text="Name" , font=("bookman old style",15,"bold"), text_color="Black")
        nameLabel.grid(row=1, column=0,pady=40)

        nameEntry = CTkEntry(leftsideFrame, font=("bookman old style", 15,"bold"),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        nameEntry.grid(row=1, column=1, pady=40)

        addressLabel = CTkLabel(leftsideFrame, text="Address" , font=("bookman old style", 15,"bold"), text_color="Black")
        addressLabel.grid(row=2, column=0, pady=(0,40), padx=10)

        addressEntry = CTkEntry(leftsideFrame, font=("bookman old style", 15,"bold"),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        addressEntry.grid(row=2, column=1,pady=(0,40), padx=10)

        typeLable = CTkLabel(leftsideFrame, text="Type of Species" , font=("bookman old style", 15,"bold"), text_color="Black")
        typeLable.grid(row=3, column=0, pady=(0,40), padx=10)

        type_options = ["Avian Animals", "Land Animals", "Ocean Animals"]
        typeBox = CTkComboBox(leftsideFrame, values=type_options, font=("bookman old style", 15,"bold"),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        typeBox.grid(row=3, column=1, pady=(0,40), padx=10)

        speciesLabel = CTkLabel(leftsideFrame, text="Species" , font=("bookman old style", 15,"bold"), text_color="Black")
        speciesLabel.grid(row=4, column=0, pady=(0,40), padx=10)

        speciesEntry = CTkEntry(leftsideFrame, font=("bookman old style", 15,"bold"),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        speciesEntry.grid(row=4, column=1, pady=(0,40), padx=10)

        numofSpeciesLabel = CTkLabel(leftsideFrame, text="No. of Species" , font=("bookman old style", 15,"bold"), text_color="Black")
        numofSpeciesLabel.grid(row=5, column=0, pady=(0,20), padx=10)

        numofSpeciesEntry = CTkEntry(leftsideFrame, font=("bookman old style", 15,"bold"),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        numofSpeciesEntry.grid(row=5, column=1, pady=(0,20), padx=10)


        # RIGHT SIDE FRAME
        rightsideFrame = CTkFrame(rightFrame, fg_color="#d0f0c0")
        rightsideFrame.grid(row=0, column=1, padx=(15,50), pady=13)

        # search options 
        search_options=[ "Tracking ID", "Species Type", "Species", "No. of Species", "Name", "Address"]
        searchBox = CTkComboBox(rightsideFrame, values=search_options, font=("bookman old style", 12),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10, state='readonly', width=100)
        searchBox.grid(row=0,column=0, pady=(10,0))
        searchBox.set('Search by')

        #Buttons for the right side frame of the track page
        searchEntry = CTkEntry(rightsideFrame, font=("bookman old style", 15),text_color="black", fg_color="white", border_color="#bdbdbd",corner_radius=10)
        searchEntry.grid(row=0, column=1, pady=(10,0))

        searchButton = CTkButton(rightsideFrame, text="Search",font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80, width=70, command=search_track)
        searchButton.grid(row=0, column=2, pady=(10,0))

        show_allButton = CTkButton(rightsideFrame, text="Show All",font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80, width=90,command= show_all)
        show_allButton.grid(row=0, column=3, pady=(10,0))

        #The view box of the data
        tree=ttk.Treeview(rightsideFrame, height=23)
        tree.grid(row=1, column=0, columnspan=4, padx=40, pady=40)

        tree.config(show="headings")

        tree["columns"] = ("Tracking ID", "Species Type", "Species", "No. of Species", "Name", "Address")
        tree.heading('Tracking ID', text='Tracking ID')
        tree.heading('Species Type', text='Species Type')
        tree.heading('Species', text='Species')
        tree.heading('No. of Species', text='No. of Species')
        tree.heading('Name', text='Name')
        tree.heading('Address', text='Address')

        tree.column('Tracking ID', anchor=CENTER,width=90)
        tree.column('Species Type', anchor=CENTER,width=100)
        tree.column('Species', anchor=CENTER,width=70)
        tree.column('No. of Species', anchor=CENTER,width=105)
        tree.column('Name', anchor=CENTER,width=120)
        tree.column('Address', anchor=CENTER,width=120)

        style=ttk.Style()

        style.configure('Treeview.Heading', font=("bookman old style", 10,"bold"))
        
        treeview_data()

        #Buttons for the insertion, deletion, update, and clear of input in the entry
        buttonTrackFrame = CTkFrame(rightFrame,fg_color="#d0f0c0" )
        buttonTrackFrame.grid(row=1, column=0, columnspan=2, padx=(0,45))

        clearButton = CTkButton(buttonTrackFrame, text="Clear Input", height=60,font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80, command=lambda: clear(True))
        clearButton.grid(row=0, column=0, pady=35, padx=(15,20))

        addButton = CTkButton(buttonTrackFrame, text="Add Track",height=60 ,font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80, command=add_track)
        addButton.grid(row=0, column=1, pady=35, padx=(15,20))

        updateButton = CTkButton(buttonTrackFrame, text="Update Track",height=60,font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80, command=update_track)
        updateButton.grid(row=0, column=2, pady=35, padx=(15,20))

        deleteButton = CTkButton(buttonTrackFrame, text="Delete Track",height=60,font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80, command=delete_track)
        deleteButton.grid(row=0, column=3, pady=35, padx=(15,20))


    #This handles all of the styles of the whole system itself, the buttons for each pages, the background and the pictures

    # FRAMES
    topFrame = CTkFrame(root, width=1000, height=50, fg_color="#1c2a19", corner_radius=0)
    topFrame.pack()

    leftFrame = CTkFrame(root, width=150, height=600, fg_color="#3b4e21", corner_radius=0)
    leftFrame.pack(side=LEFT)

    rightFrame = CTkFrame(root, width=790, height=600, fg_color="#eefae5", corner_radius=0)
    rightFrame.pack(side=RIGHT)

    # IMAGES
    logo = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\HabiTrack\\logo.png')
    logo = logo.resize((280, 170))
    logoPhoto = ImageTk.PhotoImage(logo)

    tracking = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\HabiTrack\\tracking.png')
    tracking = tracking.resize((1366, 850))
    trackingPhoto = ImageTk.PhotoImage(tracking)

    sdg = Image.open('C:\\Users\\cadev\\projects\\Final Project (Python)\\HabiTrack\\sdg.png')
    sdg = sdg.resize((1250,850))
    sdgPhoto = ImageTk.PhotoImage(sdg)

    # LABELS
    logoLabel = CTkLabel(leftFrame, image=logoPhoto, text="")
    logoLabel.grid(row=0, column=0, padx=10, pady=(20, 35))

    # BUTTONS
    buttons = {}

    statusButton = CTkButton(leftFrame,height=40,text="STATUS",font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80,command=lambda: set_active_page("status_page"),)
    statusButton.grid(row=1, column=0, padx=10, pady=(0, 20))
    buttons[statusButton] = "status_page"

    trackButton = CTkButton(leftFrame,height=40,text="TRACK",font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80,command=lambda: set_active_page("track_page"),)
    trackButton.grid(row=2, column=0, padx=10, pady=(0, 20))
    buttons[trackButton] = "track_page"

    SDGButton = CTkButton(leftFrame,height=40,text="SDG",font=("bookman old style", 17),text_color="White",fg_color="#1c2a19",corner_radius=80,command=lambda: set_active_page("sdg_page"),)
    SDGButton.grid(row=3, column=0, padx=10, pady=(0, 600))
    buttons[SDGButton] = "sdg_page"

    # Initialize with the status page
    set_active_page("status_page")

    # ROOT
    root.title("HabiTrack")
    root.geometry("1000x600+230+70")
    root.config(background="#eefae5")
    root.resizable(0, 0)

    root.bind('<ButtonRelease>', selection)

    root.mainloop()

if __name__ == "__main__":
    main()