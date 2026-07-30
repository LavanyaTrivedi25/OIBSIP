import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import io
import datetime

apiKey = "e2d69e21e5d2afbf40fa4a20166ce1fd"
initial_url = "http://api.openweathermap.org/data/2.5/weather"

class WeatherForecaster:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Weather App")
        self.root.geometry("540x800")
        self.root.resizable(False, False)
        self.is_celsius = True
        self.current_data = None


        input_frame = tk.Frame(root, pady=10)
        input_frame.pack()
        tk.Label(input_frame, text="City / ZIP:", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)
        self.city_entry = tk.Entry(input_frame, width=16, font=("Arial", 11))
        self.city_entry.pack(side=tk.LEFT, padx=5)
        btn_get = tk.Button(input_frame, text="Get Weather", bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), command=self.get_weather)
        btn_get.pack(side=tk.LEFT, padx=3)
        btn_auto = tk.Button(input_frame, text="Auto Detect", bg="#2196F3", fg="white", font=("Arial", 9, "bold"), command=self.auto_detect_location)
        btn_auto.pack(side=tk.LEFT, padx=3)
        self.btn_unit = tk.Button(root, text="Switch to °F", font=("Arial", 9), command=self.toggleOption)
        self.btn_unit.pack(pady=2)
        self.result_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief="groove", padx=10, pady=10)
        self.result_frame.pack(fill="x", padx=20, pady=5)
        self.lbl_city = tk.Label(self.result_frame, text="Location: ---", font=("Arial", 11, "bold"), bg="#f0f0f0")
        self.lbl_city.pack(anchor="w")
        self.lbl_icon = tk.Label(self.result_frame, bg="#f0f0f0")
        self.lbl_icon.pack(pady=2)
        self.lbl_temp = tk.Label(self.result_frame, text="Temperature: --", font=("Arial", 10), bg="#f0f0f0")
        self.lbl_temp.pack(anchor="w")
        self.lbl_high_low = tk.Label(self.result_frame, text="High: -- | Low: --", font=("Arial", 10), bg="#f0f0f0")
        self.lbl_high_low.pack(anchor="w")
        self.lbl_feels = tk.Label(self.result_frame, text="Feels Like: --", font=("Arial", 10), bg="#f0f0f0")
        self.lbl_feels.pack(anchor="w")
        self.lbl_desc = tk.Label(self.result_frame, text="Condition: --", font=("Arial", 10), bg="#f0f0f0")
        self.lbl_desc.pack(anchor="w")
        self.lbl_details = tk.Label(self.result_frame, text="Humidity: -- | Wind: --", font=("Arial", 9), bg="#f0f0f0")
        self.lbl_details.pack(anchor="w", pady=2)
        hourly_frame = tk.LabelFrame(root, text=" Hourly Forecast (Next 6 Intervals) ", font=("Arial", 9, "bold"), padx=10, pady=5)
        hourly_frame.pack(fill="x", padx=20, pady=5)
        self.lbl_hourly = tk.Label(hourly_frame, text="---", font=("Courier", 8), justify="left")
        self.lbl_hourly.pack(anchor="w")
        daily_frame = tk.LabelFrame(root, text=" 5-Day Daily Forecast ", font=("Arial", 9, "bold"), padx=10, pady=5)
        daily_frame.pack(fill="x", padx=20, pady=5)
        self.lbl_daily = tk.Label(daily_frame, text="---", font=("Courier", 8), justify="left")
        self.lbl_daily.pack(anchor="w")


    def enter_city(self):
        c = str(self.city_entry.get())
        city = c.strip()
        if not city:
            messagebox.showwarning("Validation Error", "Invalid input. Please enter a valid city name or zip code.")
            return None
        return city

    def get_wether_info(self, query):
        url = f"{initial_url}?q={query}&appid={apiKey}&units=metric"
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return resp.json()
            elif resp.status_code == 404:
                messagebox.showerror("API Error", "City not found. Please check the spelling and try again.")
                return None
            elif resp.status_code == 401:
                messagebox.showerror("API Error", "Invalid API key. Please check the credentials.")
                return None
            else:
                messagebox.showerror("API Error", f"Server returned status code: {resp.status_code}")
                return None
        except requests.exceptions.Timeout:
            messagebox.showerror("Network Error", "Request timed out. Please check your internet connection.")
            return None
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error occurred: {e}")
            return None

    def auto_detect_location(self):
        try:
            res = requests.get("https://ipinfo.io/json", timeout=5)
            if res.status_code == 200:
                data = res.json()
                city = data.get("city")
                if city:
                    self.city_entry.delete(0, tk.END)
                    self.city_entry.insert(0, city)
                    self.get_weather()
                else:
                    messagebox.showerror("Error", "Could not detect city from IP address.")
            else:
                messagebox.showerror("Error", "Failed to fetch IP location.")
        except Exception as e:
            messagebox.showerror("Network Error", f"IP detection failed: {e}")

    def update_display(self):
        if not self.current_data:
            return

        data = self.current_data
        city_name = data.get("name")
        countryName = data.get("sys", {}).get("country")
        main_data = data.get("main", {})
        
        humidity = main_data.get("humidity")
        temp_c = main_data.get("temp")
        feels_like_c = main_data.get("feels_like")
        temp_max_c = main_data.get("temp_max")
        temp_min_c = main_data.get("temp_min")
        
        # Conversions from celsius to fahrenheit
        temp_f = (temp_c * 9/5) + 32 if temp_c is not None else None
        feels_like_f = (feels_like_c * 9/5) + 32 if feels_like_c is not None else None
        temp_max_f = (temp_max_c * 9/5) + 32 if temp_max_c is not None else None
        temp_min_f = (temp_min_c * 9/5) + 32 if temp_min_c is not None else None

        weather_desc = data.get("weather", [{}])[0].get("description", "N/A").title()
        icon_code = data.get("weather", [{}])[0].get("icon", "01d")
        speed_wind = data.get("wind", {}).get("speed")

        if self.is_celsius:
            temp_str = f"{temp_c:.2f}°C"
            feels_str = f"{feels_like_c:.2f}°C"
            high_str = f"{temp_max_c:.2f}°C"
            low_str = f"{temp_min_c:.2f}°C"
        else:
            temp_str = f"{temp_f:.2f}°F"
            feels_str = f"{feels_like_f:.2f}°F"
            high_str = f"{temp_max_f:.2f}°F"
            low_str = f"{temp_min_f:.2f}°F"

        self.lbl_city.config(text=f"Weather info for {city_name}, {countryName}")
        self.lbl_temp.config(text=f"Temperature: {temp_str}")
        self.lbl_high_low.config(text=f"High: {high_str}  |  Low: {low_str}")
        self.lbl_feels.config(text=f"Feels Like: {feels_str}")
        self.lbl_desc.config(text=f"Description: {weather_desc}")
        self.lbl_details.config(text=f"Humidity: {humidity}% | Wind: {speed_wind} m/s")

        try: #icon for weather visualization
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            img_data = requests.get(icon_url, timeout=5).content
            img = Image.open(io.BytesIO(img_data))
            img = img.resize((40, 40))
            self.photo = ImageTk.PhotoImage(img)
            self.lbl_icon.config(image=self.photo)
        except Exception:
            self.lbl_icon.config(image="")

        forecast = data.get('forecast_list', [])
        
        hourlyT = ""
        for h in forecast[:6]:
            dt_txt = h.get("dt_txt", "")
            time_str = dt_txt.split(" ")[1][:5] if " " in dt_txt else ""
            h_temp = h.get("main", {}).get("temp")
            if h_temp is not None and not self.is_celsius:
                h_temp = (h_temp * 9/5) + 32
            h_desc = h.get("weather", [{}])[0].get("main", "")
            temp_unit = 'C' if self.is_celsius else 'F'
            if h_temp is not None:
                hourlyT += f"{time_str} -> {h_temp:.1f}°{temp_unit} | {h_desc}\n"
        self.lbl_hourly.config(text=hourlyT.strip() if hourlyT else "Hourly data unavailable")

        daily_text = ""
        for d in forecast[4::8][:5]:
            dt_txt = d.get("dt_txt", "")
            date_str = dt_txt.split(" ")[0] if " " in dt_txt else ""
            d_temp = d.get("main", {}).get("temp")
            if d_temp is not None and not self.is_celsius:
                d_temp = (d_temp * 9/5) + 32
            d_desc = d.get("weather", [{}])[0].get("main", "")
            temp_unit = 'C' if self.is_celsius else 'F'
            if d_temp is not None:
                daily_text += f"{date_str}: Temp: {d_temp:.1f}°{temp_unit} | {d_desc}\n"
        self.lbl_daily.config(text=daily_text.strip() if daily_text else "Daily data unavailable")

    def toggleOption(self): # for toggle
        self.is_celsius = not self.is_celsius
        if self.is_celsius:
            self.btn_unit.config(text="Switch to °F")
        else:
            self.btn_unit.config(text="Switch to °C")
        if self.current_data:
            self.update_display()

    def get_weather(self):
        quer = self.enter_city()
        if not quer:
            return

        data = self.get_wether_info(quer)
        if not data:
            return

        self.current_data = data
        
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={quer}&appid={apiKey}&units=metric"
        try:
            fc_res = requests.get(forecast_url, timeout=10)
            if fc_res.status_code == 200:
                self.current_data['forecast_list'] = fc_res.json().get("list", [])
        except Exception:
            pass

        self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherForecaster(root)
    root.mainloop()