import pickle
import pandas as pd
import customtkinter as ctk
from tkinter import messagebox

#  Load trained model
try:
    with open('C:/Users/hp/RidgeModel.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    messagebox.showerror("Error", "Model file not found at C:/Users/hp/RidgeModel.pkl")
    exit()

#  Dummy locations (replace with actual model locations if needed)
locations = ['1st Phase JP Nagar', 'Whitefield', 'Indira Nagar', 'HSR Layout', 'Marathahalli']

#  Predict function
def predict_price():
    try:
        location = location_var.get()
        sqft = float(entry_sqft.get())
        bath = int(entry_bath.get())
        bhk = int(entry_bhk.get())

        if sqft <= 0 or bath <= 0 or bhk <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Prepare DataFrame
        input_df = pd.DataFrame({
            'location': [location],
            'total_sqft': [sqft],
            'bath': [bath],
            'bhk': [bhk]
        })

        predicted_price = model.predict(input_df)[0]
        predicted_price = round(predicted_price, 2)
        messagebox.showinfo("Prediction", f"🏠 Estimated Price: ₹{predicted_price} Lakhs")
    except ValueError as ve:
        messagebox.showwarning("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong!\n{e}")

#  Set up CustomTkinter app
ctk.set_appearance_mode("System")  # Light/Dark mode
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"


app = ctk.CTk()
app.title("🏡 Bangalore House Price Predictor")
app.state('zoomed')  # Fullscreen
#app.configure(bg_color="#E0F7FA")  # light teal color
app.configure(bg_color="Lavender")  # soft lavender background



#  Heading
heading = ctk.CTkLabel(app, text="🏡 Bangalore House Price Predictor", font=("Arial Rounded MT Bold", 28))
heading.pack(pady=30)

#  Location Dropdown
location_var = ctk.StringVar(value=locations[0])
ctk.CTkLabel(app, text="Select Location:", font=("Arial", 18)).pack(pady=10)
location_menu = ctk.CTkComboBox(app, values=locations, variable=location_var, width=300, font=("Arial", 16))
location_menu.pack(pady=10)

#  Square Feet
ctk.CTkLabel(app, text="Enter Square Feet:", font=("Arial", 18)).pack(pady=10)
entry_sqft = ctk.CTkEntry(app, width=300, font=("Arial", 16))
entry_sqft.pack(pady=10)

#  Bathrooms
ctk.CTkLabel(app, text="Enter Number of Bathrooms:", font=("Arial", 18)).pack(pady=10)
entry_bath = ctk.CTkEntry(app, width=300, font=("Arial", 16))
entry_bath.pack(pady=10)

# Bedrooms
ctk.CTkLabel(app, text="Enter Number of Bedrooms (BHK):", font=("Arial", 18)).pack(pady=10)
entry_bhk = ctk.CTkEntry(app, width=300, font=("Arial", 16))
entry_bhk.pack(pady=10)

#  Predict Button
predict_btn = ctk.CTkButton(app, text="🔮 Predict Price", command=predict_price, width=200, height=50, font=("Arial", 16))
predict_btn.pack(pady=20)

#  Exit Button
exit_btn = ctk.CTkButton(app, text="❌ Exit", command=app.destroy, width=150, height=40, font=("Arial", 14), fg_color="#FF5C5C", hover_color="#FF1C1C")
exit_btn.pack(pady=10)

app.mainloop()
