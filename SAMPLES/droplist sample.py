import tkinter as tk
from tkinter import ttk

# Define the data
indian_state_cities={
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Hyderabad", "Guntur", "Nellore", "Kurnool", "Rajahmundry", "Tirupati", "Kakinada", "Anantapur", "Kadapa", "Chittoor", "Eluru", "Ongole", "Nandyal"],
    "Arunachal Pradesh": ["Itanagar", "Naharlagun", "Pasighat", "Tawang", "Ziro", "Bomdila", "Roing", "Aalo", "Tezu", "Daporijo", "Khonsa", "Seppa", "Anini", "Changlang", "Yingkiong"],
    "Assam": ["Guwahati", "Dibrugarh", "Silchar", "Jorhat", "Nagaon", "Tinsukia", "Tezpur", "Karimganj", "Hailakandi", "Sivasagar", "Goalpara", "Bongaigaon", "Barpeta", "Nalbari", "Dhubri"],
    "Bihar": ["Patna", "Gaya", "Muzaffarpur", "Bhagalpur", "Darbhanga", "Arrah", "Begusarai", "Katihar", "Chhapra", "Purnia", "Motihari", "Saharsa", "Hajipur", "Siwan", "Gopalganj"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur", "Korba", "Durg", "Raigarh", "Rajnandgaon", "Jagdalpur", "Ambikapur", "Dhamtari", "Mahasamund", "Bilaspur", "Raigarh", "Kanker", "Kabirdham (Kawardha)"],
    "Goa": ["Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda", "Bicholim", "Curchorem", "Cuncolim", "Sanguem", "Valpoi", "Mormugao", "Sanquelim", "Salcete", "Sattari", "Tiswadi"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar", "Nadiad", "Morbi", "Surendranagar", "Bharuch", "Anand", "Porbandar", "Godhra"],
    "Haryana": ["Chandigarh", "Faridabad", "Gurgaon", "Hisar", "Rohtak", "Panipat", "Karnal", "Sonipat", "Yamunanagar", "Panchkula", "Bhiwani", "Sirsa", "Bahadurgarh", "Jind", "Thanesar"],
    "Himachal Pradesh": ["Shimla", "Mandi", "Dharamshala", "Solan", "Palampur", "Una", "Kullu", "Chamba", "Hamirpur", "Bilaspur", "Sirmaur", "Kangra", "Nahan", "Mandi", "Shimla"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro Steel City", "Deoghar", "Phusro", "Hazaribagh", "Giridih", "Ramgarh", "Medininagar (Daltonganj)", "Chirkunda", "Jhumri Tilaiya", "Gumla", "Bhawanathpur", "Chaibasa"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru", "Belagavi", "Davangere", "Ballari", "Vijayapura", "Kalaburagi", "Shivamogga", "Tumakuru", "Raichur", "Hassan", "Gadag-Betageri", "Chitradurga"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur", "Kollam", "Palakkad", "Alappuzha", "Kannur", "Kottayam", "Kasaragod", "Pathanamthitta", "Malappuram", "Idukki", "Ernakulam", "Wayanad"],
    "Madhya Pradesh": ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain", "Sagar", "Dewas", "Satna", "Ratlam", "Rewa", "Chhindwara", "Shivpuri", "Vidisha", "Damoh", "Mandsaur"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Thane", "Nashik", "Kalyan-Dombivli", "Vasai-Virar", "Aurangabad", "Navi Mumbai", "Solapur", "Bhiwandi", "Amravati", "Nanded", "Kolhapur", "Sangli"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur", "Churachandpur", "Senapati", "Ukhrul", "Chandel", "Tamenglong", "Kangpokpi", "Jiribam", "Kakching", "Tengnoupal", "Kamjong", "Noney", "Pherzawl"],
    "Meghalaya": ["Shillong", "Tura", "Nongstoin", "Jowai", "Baghmara", "Williamnagar", "Resubelpara", "Mairang", "Mahendraganj", "Nongpoh", "Nongpoh", "Khliehriat", "Mawkyrwat", "Ampati", "Ranikor"],
    "Mizoram": ["Aizawl", "Lunglei", "Saiha", "Champhai", "Kolasib", "Serchhip", "Lawngtlai", "Hnahthial", "Khawzawl", "Saitual", "Thenzawl", "Tlabung", "Zawlnuam", "Tlungvel", "Tuirial"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang", "Wokha", "Zunheboto", "Phek", "Chumukedima", "Mon", "Pfutsero", "Medziphema", "Kiphire", "Longleng", "Tizit", "Meluri"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Berhampur", "Sambalpur", "Puri", "Brahmapur", "Baleshwar", "Baripada", "Bhadrak", "Balangir", "Jharsuguda", "Bargarh", "Paradip", "Anugul"],
    "Punjab": ["Chandigarh", "Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Hoshiarpur", "Mohali", "Batala", "Pathankot", "Moga", "Abohar", "Malerkotla", "Khanna", "Phagwara"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner", "Ajmer", "Bhilwara", "Alwar", "Sikar", "Pali", "Ganganagar", "Bharatpur", "Sawai Madhopur", "Churu", "Jhunjhunu"],
    "Sikkim": ["Gangtok", "Namchi", "Mangan", "Gyalshing", "Singtam", "Rangpo", "Jorethang", "Soreng", "Ravangla", "Rhenock", "Sakyong", "Lachung", "Gyalshing", "Yumthang", "Melli"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Tiruppur", "Salem", "Erode", "Tirunelveli", "Vellore", "Thoothukudi", "Nagercoil", "Thanjavur", "Dindigul", "Cuddalore", "Kanchipuram"],
    "Telangana": ["Hyderabad", "Warangal", "Karimnagar", "Nizamabad", "Khammam", "Ramagundam", "Mahbubnagar", "Nalgonda", "Adilabad", "Suryapet", "Miryalaguda", "Jagtial", "Nirmal", "Siddipet", "Kothagudem"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailasahar", "Ambassa", "Belonia", "Teliamura", "Khowai", "Sabroom", "Amarpur", "Bishalgarh", "Kumarghat", "Sonamura", "Mohanpur", "Kamalasagar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Varanasi", "Agra", "Meerut", "Allahabad", "Bareilly", "Aligarh", "Moradabad", "Saharanpur", "Gorakhpur", "Faizabad", "Jhansi", "Muzaffarnagar", "Mathura"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Rishikesh", "Haldwani", "Nainital", "Kashipur", "Rudrapur", "Roorkee", "Ramnagar", "Ranikhet", "Pithoragarh", "Kotdwara", "Mussoorie", "Tehri", "Sitarganj"],
    "West Bengal": ["Kolkata", "Howrah", "Asansol", "Siliguri", "Durgapur", "Bardhaman", "Malda", "Baharampur", "Kharagpur", "Haldia", "Jalpaiguri", "Bangaon", "Krishnanagar", "Raiganj", "Medinipur"],
    "Ladakh": ["Leh", "Kargil", "Drass", "Nubra", "Zanskar", "Changthang", "Turtuk", "Hanle", "Hunder", "Diskit", "Tingmosgang", "Tia", "Skurbuchan", "Hemis", "Durbuk"]
}


def on_state_select(event):
    # Get the selected state
    selected_state = state_combo.get()

    # Populate the city drop-down based on the selected state
    city_combo['values'] = indian_state_cities.get(selected_state, [])

# Create the main window
root = tk.Tk()
root.title("User Registration")

# Create a label for state
state_label = ttk.Label(root, text="State:")#yeh mera naam hai 
state_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Create a drop-down list for states
states = list(indian_state_cities.keys())
state_combo = ttk.Combobox(root, values=states, state="readonly")
state_combo.grid(row=0, column=1, padx=5, pady=5)
state_combo.bind("<<ComboboxSelected>>", on_state_select)

# Create a label for city
city_label = ttk.Label(root, text="City:")
city_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Create a drop-down list for cities
cities = []
city_combo = ttk.Combobox(root, values=cities, state="readonly")
city_combo.grid(row=1, column=1, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
