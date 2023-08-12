import tkinter  as tk
import parcel_calculator
from database import *
from tkinter import messagebox

class ParcelCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Parcel Calculator")
        master.geometry("600x300")
        master.configure(bg="purple")
        font = ("Arial",15)
        font2 = ("Arial",25)

        # Create length input label and entry field
        self.length_label = tk.Label(master, text="Welcome to Lelemove",font=font2,bg="purple",fg="white")
        self.length_label.grid(row=0, column=0,columnspan=2)

        # Create length input label and entry field
        self.length_label = tk.Label(master, text="Length (cm):",font=font,bg="purple",fg="white")
        self.length_label.grid(row=1, column=0)
        self.length_entry = tk.Entry(master,width=40,font=font)
        self.length_entry.grid(row=1, column=1)

        # Create width input label and entry field
        self.width_label = tk.Label(master, text="Width (cm):",font=font,bg="purple",fg="white")
        self.width_label.grid(row=2, column=0)
        self.width_entry = tk.Entry(master,width=40,font=font)
        self.width_entry.grid(row=2, column=1)

        # Create height input label and entry field
        self.height_label = tk.Label(master, text="Height:",font=font,bg="purple",fg="white")
        self.height_label.grid(row=3, column=0)
        self.height_entry = tk.Entry(master,width=40,font=font)
        self.height_entry.grid(row=3, column=1)

        # Create weight input label and entry field
        self.weight_label = tk.Label(master, text="Weight (kg):",font=font,bg="purple",fg="white")
        self.weight_label.grid(row=4, column=0)
        self.weight_entry = tk.Entry(master,width=40,font=font)
        self.weight_entry.grid(row=4, column=1)

        # Create weight input label and entry field
        self.id_label = tk.Label(master, text="Item id:",font=font,bg="purple",fg="white")
        self.id_label.grid(row=5, column=0)
        self.id_entry = tk.Entry(master,width=40,font=font)
        self.id_entry.grid(row=5, column=1)

        
       # Create calculate button
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_price,width=15)
        self.calculate_button.grid(row=7, column=0, columnspan=2)


        #Create insert button
        self.calculate_button = tk.Button(master, text="Insert",command=self.insert_data,width=15)
        self.calculate_button.grid(row=8, column=0, columnspan=2)

        # Create price label
        self.price_label = tk.Label(master, text="")
        self.price_label.grid(row=6, column=0, columnspan=2)

    

    def calculate_price(self):
            # Get parcel dimensions and weight from entry fields
            global length
            global width
            global height
            global weight
            global price
            global itemId
            global volume
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            itemId = self.id_entry.get()
            volume = length * width * height

            
            # Calculate parcel price using imported function
            price = parcel_calculator.calculate_price(length,width,height,weight)


            # Update price label with calculated price
            self.price_label.config(text="The price of your parcel is: $" + str(price))
    def insert_data(self):
        try:
            sql = "INSERT INTO package VALUES (%s,%s,%s,%s,%s,%s)"
            data = (str(itemId),str(height),str(width),str(length),str(volume),str(price))
            mycursor.execute(sql,data)
            messagebox.showinfo(message="Your application has been submitted",title="Record Success")
            mydb.commit()

        except:
            messagebox.showinfo(message="Fail enter data into database",title="Failed")
            mydb.rollback()
            print(str(itemId),str(height),str(width),str(length),str(volume),str(price))


master = tk.Tk()
parcel_calculator_gui = ParcelCalculatorGUI(master)
master.mainloop()
