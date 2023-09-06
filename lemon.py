import pandas as pd

# Baca data dari file XLSX
df = pd.read_excel('LittleLemon_data.xlsx')

# Tampilkan 10 baris pertama dari data
print(df.head(10))

# Implementasikan prosedur-prosedur yang diminta dalam tugas
def GetMaxQuantity():
    max_quantity = df['Quantity'].max()
    return max_quantity

def ManageBooking(booking_id):
    booking_info = df[df['Booking ID'] == booking_id]
    if booking_info.empty:
        return "Booking not found"
    else:
        return booking_info

def UpdateBooking(booking_id, new_data):
    booking_info = df[df['Booking ID'] == booking_id]
    if booking_info.empty:
        return "Booking not found"
    else:
        df.loc[df['Booking ID'] == booking_id] = new_data
        return "Booking updated successfully"

def AddBooking(new_booking):
    df = df.append(new_booking, ignore_index=True)
    return "New booking added successfully"

def CancelBooking(booking_id):
    booking_info = df[df['Booking ID'] == booking_id]
    if booking_info.empty:
        return "Booking not found"
    else:
        df.drop(df[df['Booking ID'] == booking_id].index, inplace=True)
        return "Booking canceled successfully"

# Contoh penggunaan prosedur-prosedur di atas
max_quantity = GetMaxQuantity()
print("Maximum Quantity:", max_quantity)

booking_info = ManageBooking(1)
print("Booking Info:")
print(booking_info)

new_data = {'Booking ID': 2, 'Delivery Date': '2023-09-10', 'Customer ID': 101, 'Customer Name': 'John Doe', 'City': 'New York', 'Country': 'USA', 'Postal Code': '10001', 'Country Code': '+1', 'Cost': 50.0, 'Sales': 60.0, 'Quantity': 2, 'Discount': 0.1, 'Delivery Cost': 5.0, 'Course Name': 'Dinner', 'Cuisine Name': 'Italian', 'Starter Name': 'Bruschetta', 'Desert Name': 'Tiramisu', 'Drink': 'Wine', 'Sides': 'Garlic Bread'}
update_result = UpdateBooking(2, new_data)
print(update_result)

new_booking = {'Booking ID': 6, 'Delivery Date': '2023-09-15', 'Customer ID': 105, 'Customer Name': 'Alice Smith', 'City': 'Los Angeles', 'Country': 'USA', 'Postal Code': '90001', 'Country Code': '+1', 'Cost': 40.0, 'Sales': 55.0, 'Quantity': 3, 'Discount': 0.2, 'Delivery Cost': 7.0, 'Course Name': 'Lunch', 'Cuisine Name': 'Mexican', 'Starter Name': 'Guacamole', 'Desert Name': 'Churros', 'Drink': 'Soda', 'Sides': 'Nachos'}
add_result = AddBooking(new_booking)
print(add_result)

cancel_result = CancelBooking(3)
print(cancel_result)
