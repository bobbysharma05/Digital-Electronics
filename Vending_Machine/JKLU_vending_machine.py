from tkinter import *
from tkinter import ttk, simpledialog
import tkinter.messagebox as tmsg
import json
import os
from datetime import datetime

class VendingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("MUSKII :) Vending Machine")
        self.root.geometry("700x750")
        self.root.configure(bg="light blue")
        
        # Initialize inventory and sales data
        self.inventory_file = "inventory.json"
        self.sales_file = "sales_log.json"
        self.load_inventory()
        
        # Create UI
        self.setup_ui()
    
    def load_inventory(self):
        """Load inventory from file or create default inventory"""
        if os.path.exists(self.inventory_file):
            try:
                with open(self.inventory_file, 'r') as f:
                    self.inventory = json.load(f)
            except:
                self.create_default_inventory()
        else:
            self.create_default_inventory()
    
    def create_default_inventory(self):
        """Create default inventory with initial stock quantities"""
        self.inventory = {
            "French Fries": {"price": 80, "stock": 10},
            "Softy": {"price": 30, "stock": 10},
            "Cup Cake": {"price": 20, "stock": 10},
            "Dora Cake": {"price": 30, "stock": 10},
            "Cold Coffee": {"price": 30, "stock": 10},
            "Hot Coffee": {"price": 40, "stock": 10},
            "Green Tea": {"price": 30, "stock": 10},
            "Tea": {"price": 20, "stock": 10},
            "Ice Tea": {"price": 30, "stock": 10},
            "Coca Cola": {"price": 40, "stock": 10},
            "Pepsi": {"price": 40, "stock": 10},
            "Mirinda": {"price": 40, "stock": 10},
            "Lays": {"price": 20, "stock": 10},
            "Kurkure": {"price": 20, "stock": 10}
        }
        self.save_inventory()
    
    def reset_inventory(self):
        """Reset all inventory items to default stock levels"""
        for item in self.inventory:
            self.inventory[item]["stock"] = 10
        self.save_inventory()
        self.update_all_quantity_options()
        tmsg.showinfo("Reset", "Inventory has been reset to default levels.")
    
    def save_inventory(self):
        """Save inventory to file"""
        with open(self.inventory_file, 'w') as f:
            json.dump(self.inventory, f, indent=4)
    
    def log_sale(self, items, total):
        """Log sale details to sales log file"""
        if os.path.exists(self.sales_file):
            try:
                with open(self.sales_file, 'r') as f:
                    sales_log = json.load(f)
            except:
                sales_log = []
        else:
            sales_log = []
        
        # Create sale record
        sale = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": items,
            "total": total
        }
        
        sales_log.append(sale)
        
        # Save updated sales log
        with open(self.sales_file, 'w') as f:
            json.dump(sales_log, f, indent=4)
    
    def setup_ui(self):
        """Create the main UI elements"""
        # Title
        Label(self.root, text="MUSKII :)\nVending Machine", bg="light blue", 
              fg="black", font="Algerian 20 bold").pack(pady=20)
        
        Label(self.root, text="Choose your item:", bg="light blue", 
              fg="black", font="Algerian 16").pack(anchor=W, padx=50, pady=(10, 0))
        
        # Create frame for items
        items_frame = Frame(self.root, bg="light blue")
        items_frame.pack(fill=BOTH, expand=True, padx=50, pady=10)
        
        # Create left and right columns for items
        left_col = Frame(items_frame, bg="light blue")
        left_col.pack(side=LEFT, fill=BOTH, expand=True)
        
        right_col = Frame(items_frame, bg="light blue")
        right_col.pack(side=RIGHT, fill=BOTH, expand=True)
        
        # Variables to store item selection and quantities
        self.item_vars = {}
        self.quantity_vars = {}
        
        # Split items between columns
        column_frames = [left_col, right_col]
        items_list = list(self.inventory.items())
        items_per_column = len(items_list) // 2 + (1 if len(items_list) % 2 else 0)
        
        for i, (item_name, item_data) in enumerate(items_list):
            col_index = 0 if i < items_per_column else 1
            
            # Create frame for each item
            item_frame = Frame(column_frames[col_index], bg="light blue")
            item_frame.pack(anchor=W, pady=10, fill=X)
            
            # Checkbox variable
            self.item_vars[item_name] = IntVar(value=0)
            
            # Item checkbox with stock display
            stock_text = f"{item_name} = {item_data['price']}Rs (Stock: {item_data['stock']})"
            check = Checkbutton(
                item_frame, 
                text=stock_text,
                bg="light blue",
                variable=self.item_vars[item_name],
                command=lambda name=item_name: self.update_quantity_options(name)
            )
            check.pack(side=LEFT, padx=(0, 10))
            
            # Store checkbox reference for later updates
            setattr(self, f"{item_name}_check", check)
            
            # Quantity combobox
            self.quantity_vars[item_name] = IntVar(value=1)
            quantity_combo = ttk.Combobox(
                item_frame,
                width=5,
                textvariable=self.quantity_vars[item_name],
                state="disabled"
            )
            quantity_combo.pack(side=LEFT)
            
            # Store combobox reference for later state updates
            setattr(self, f"{item_name}_combo", quantity_combo)
        
        # Payment section frame
        payment_frame = Frame(self.root, bg="light blue")
        payment_frame.pack(fill=X, padx=50, pady=10)
        
        # Cash entry
        Label(payment_frame, text="Enter Your Cash:", bg="light blue", fg="black", font=(12)).grid(row=0, column=0, sticky=W, pady=5)
        self.cash_var = IntVar()
        Entry(payment_frame, font=(12), textvariable=self.cash_var).grid(row=0, column=1, sticky=W, pady=5)
        
        # Total bill display
        Label(payment_frame, text="Total Bill:", bg="light blue", fg="black", font=(12)).grid(row=1, column=0, sticky=W, pady=5)
        self.total_var = IntVar()
        Entry(payment_frame, font=(12), textvariable=self.total_var, state="readonly").grid(row=1, column=1, sticky=W, pady=5)
        
        # Change display
        Label(payment_frame, text="Your Change:", bg="light blue", fg="black", font=(12)).grid(row=2, column=0, sticky=W, pady=5)
        self.change_var = IntVar()
        Entry(payment_frame, font=(12), textvariable=self.change_var, state="readonly").grid(row=2, column=1, sticky=W, pady=5)
        
        # Information about persistence
        persistence_note = Label(
            self.root, 
            text="Note: Inventory changes are saved between sessions.\nUse Admin panel to reset inventory.",
            bg="light blue", fg="dark blue", font=("Arial", 10, "italic")
        )
        persistence_note.pack(pady=(0, 10))
        
        # Button frame
        button_frame = Frame(self.root, bg="light blue")
        button_frame.pack(pady=10)
        
        # Buttons
        Button(button_frame, text="Calculate", bg="white", font=(12), fg="black", 
               command=self.calculate_total).pack(side=LEFT, padx=10)
        
        Button(button_frame, text="Submit", bg="white", font=(12), fg="black", 
               command=self.process_order).pack(side=LEFT, padx=10)
        
        Button(button_frame, text="Admin", bg="white", font=(12), fg="black", 
               command=self.admin_access).pack(side=LEFT, padx=10)
        
        Button(button_frame, text="Cancel", bg="white", font=(12), fg="black", 
               command=self.root.destroy).pack(side=LEFT, padx=10)
        
        # Update UI based on current inventory
        self.update_all_quantity_options()
    
    def update_all_quantity_options(self):
        """Update all quantity options and checkboxes based on current inventory"""
        for item_name, item_data in self.inventory.items():
            # Update checkbox text to show current stock
            check = getattr(self, f"{item_name}_check")
            check.config(text=f"{item_name} = {item_data['price']}Rs (Stock: {item_data['stock']})")
            
            # Update quantity options
            self.update_quantity_options(item_name)
    
    def update_quantity_options(self, item_name):
        """Update quantity options for a specific item"""
        combo = getattr(self, f"{item_name}_combo")
        check = getattr(self, f"{item_name}_check")
        
        if self.item_vars[item_name].get() == 1:
            # Item selected, enable combobox if in stock
            max_quantity = min(10, self.inventory[item_name]["stock"])
            if max_quantity > 0:
                values = tuple(range(1, max_quantity + 1))
                combo.config(values=values, state="readonly")
                # Ensure current value is valid
                current_val = self.quantity_vars[item_name].get()
                if current_val > max_quantity:
                    self.quantity_vars[item_name].set(1)
            else:
                # Out of stock
                tmsg.showinfo("Out of Stock", f"{item_name} is out of stock!")
                self.item_vars[item_name].set(0)
                combo.config(state="disabled")
        else:
            # Item not selected, disable combobox
            combo.config(state="disabled")
    
    def calculate_total(self):
        """Calculate the total bill based on selected items"""
        total_bill = 0
        
        for item_name, item_data in self.inventory.items():
            if self.item_vars[item_name].get() == 1:
                quantity = self.quantity_vars[item_name].get()
                total_bill += quantity * item_data["price"]
        
        self.total_var.set(total_bill)
    
    def process_order(self):
        """Process the order and update inventory"""
        # First calculate the total
        self.calculate_total()
        total_bill = self.total_var.get()
        
        # Check if any items are selected
        items_selected = False
        for var in self.item_vars.values():
            if var.get() == 1:
                items_selected = True
                break
        
        if not items_selected:
            tmsg.showinfo("Selection Required", "Please select at least one item.")
            return
        
        # Check if sufficient cash is provided
        cash = self.cash_var.get()
        if cash < total_bill:
            tmsg.showerror('ERROR', "Insufficient amount. Please add more cash.")
            return
        
        # Calculate change
        change = cash - total_bill
        self.change_var.set(change)
        
        # Create list of purchased items
        purchased_items = []
        
        # Update inventory and create list of purchased items
        for item_name in self.inventory:
            if self.item_vars[item_name].get() == 1:
                quantity = self.quantity_vars[item_name].get()
                
                # Ensure we have enough stock
                if quantity > self.inventory[item_name]["stock"]:
                    tmsg.showerror("Stock Error", f"Not enough {item_name} in stock!")
                    return
                
                # Update stock
                self.inventory[item_name]["stock"] -= quantity
                
                # Add to purchased items
                purchased_items.append({
                    "name": item_name,
                    "quantity": quantity,
                    "price": self.inventory[item_name]["price"],
                    "subtotal": quantity * self.inventory[item_name]["price"]
                })
        
        # Save updated inventory
        self.save_inventory()
        
        # Log the sale
        self.log_sale(purchased_items, total_bill)
        
        # Update UI to reflect new stock levels
        self.update_all_quantity_options()
        
        # Show success message
        tmsg.showinfo("Success", "Thank you for your purchase!")
        
        # Reset selection for next purchase
        for var in self.item_vars.values():
            var.set(0)
        
        self.cash_var.set(0)
        self.total_var.set(0)
        self.change_var.set(0)
    
    def admin_access(self):
        """Admin panel for inventory management"""
        password = simpledialog.askstring("Password", "Enter Admin Password:", show='*')
        if password == "admin":
            self.open_admin_panel()
        else:
            tmsg.showerror("Admin Access", "Access Denied! Incorrect Password.")
    
    def open_admin_panel(self):
        """Open admin control panel"""
        admin_window = Toplevel(self.root)
        admin_window.title("Admin Panel")
        admin_window.geometry("600x550")
        admin_window.configure(bg="light gray")
        
        # Title
        Label(admin_window, text="Inventory Management", bg="light gray", 
              fg="black", font="Arial 14 bold").pack(pady=10)
        
        # Create scrollable frame for inventory items
        main_frame = Frame(admin_window, bg="light gray")
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        canvas = Canvas(main_frame, bg="light gray")
        scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="light gray")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor=NW)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Create entries for each inventory item
        inventory_entries = {}
        row = 0
        
        # Header
        Label(scrollable_frame, text="Item", bg="light gray", font="Arial 10 bold").grid(row=row, column=0, padx=5, pady=5, sticky=W)
        Label(scrollable_frame, text="Price (Rs)", bg="light gray", font="Arial 10 bold").grid(row=row, column=1, padx=5, pady=5)
        Label(scrollable_frame, text="Stock", bg="light gray", font="Arial 10 bold").grid(row=row, column=2, padx=5, pady=5)
        row += 1
        
        for item_name, item_data in self.inventory.items():
            Label(scrollable_frame, text=item_name, bg="light gray").grid(row=row, column=0, padx=5, pady=5, sticky=W)
            
            # Price entry
            price_var = IntVar(value=item_data["price"])
            price_entry = Entry(scrollable_frame, textvariable=price_var, width=8)
            price_entry.grid(row=row, column=1, padx=5, pady=5)
            
            # Stock entry
            stock_var = IntVar(value=item_data["stock"])
            stock_entry = Entry(scrollable_frame, textvariable=stock_var, width=8)
            stock_entry.grid(row=row, column=2, padx=5, pady=5)
            
            # Store variables
            inventory_entries[item_name] = {"price": price_var, "stock": stock_var}
            
            row += 1
        
        # Explanation frame
        explanation_frame = Frame(admin_window, bg="light gray")
        explanation_frame.pack(fill=X, padx=20, pady=(10, 0))
        
        Label(
            explanation_frame, 
            text="Note: The vending machine maintains inventory between sessions.\n"
                 "Use 'Reset Stock' to restore all items to 10 units.",
            bg="light gray", 
            fg="dark blue",
            justify=LEFT
        ).pack(anchor=W)
        
        # Button frame
        button_frame = Frame(admin_window, bg="light gray")
        button_frame.pack(pady=15)
        
        # Save button
        Button(
            button_frame, 
            text="Save Changes", 
            command=lambda: self.save_inventory_changes(inventory_entries, admin_window)
        ).pack(side=LEFT, padx=10)
        
        # Reset stock button
        Button(
            button_frame, 
            text="Reset Stock", 
            command=lambda: [self.reset_inventory(), admin_window.destroy()]
        ).pack(side=LEFT, padx=10)
        
        # View sales button
        Button(
            button_frame, 
            text="View Sales Report", 
            command=self.view_sales_report
        ).pack(side=LEFT, padx=10)
        
        # Clear sales data
        Button(
            button_frame, 
            text="Clear Sales Data", 
            command=lambda: self.clear_sales_data(admin_window)
        ).pack(side=LEFT, padx=10)
        
        # Close button
        Button(
            button_frame, 
            text="Close", 
            command=admin_window.destroy
        ).pack(side=LEFT, padx=10)
    
    def clear_sales_data(self, parent_window):
        """Clear all sales data"""
        confirm = tmsg.askyesno("Confirm", "Are you sure you want to clear all sales data?", parent=parent_window)
        if confirm:
            if os.path.exists(self.sales_file):
                try:
                    # Create empty sales log
                    with open(self.sales_file, 'w') as f:
                        json.dump([], f)
                    tmsg.showinfo("Success", "Sales data cleared successfully!", parent=parent_window)
                except:
                    tmsg.showerror("Error", "Failed to clear sales data.", parent=parent_window)
        
    def save_inventory_changes(self, inventory_entries, admin_window):
        """Save changes made to inventory in admin panel"""
        for item_name, entries in inventory_entries.items():
            self.inventory[item_name]["price"] = entries["price"].get()
            self.inventory[item_name]["stock"] = entries["stock"].get()
        
        self.save_inventory()
        self.update_all_quantity_options()
        tmsg.showinfo("Success", "Inventory updated successfully!", parent=admin_window)
    
    def view_sales_report(self):
        """Display sales report from the sales log"""
        if not os.path.exists(self.sales_file):
            tmsg.showinfo("Sales Report", "No sales data available.")
            return
        
        try:
            with open(self.sales_file, 'r') as f:
                sales_log = json.load(f)
        except:
            tmsg.showerror("Error", "Could not read sales log file.")
            return
        
        if not sales_log:
            tmsg.showinfo("Sales Report", "No sales data available.")
            return
        
        # Create report window
        report_window = Toplevel(self.root)
        report_window.title("Sales Report")
        report_window.geometry("700x500")
        
        # Create scrollable text widget
        report_frame = Frame(report_window)
        report_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = Scrollbar(report_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        text_widget = Text(report_frame, wrap=WORD, yscrollcommand=scrollbar.set)
        text_widget.pack(fill=BOTH, expand=True)
        
        scrollbar.config(command=text_widget.yview)
        
        # Insert report header
        text_widget.insert(END, "MUSKII :) VENDING MACHINE - SALES REPORT\n")
        text_widget.insert(END, "="*50 + "\n\n")
        
        # Calculate totals
        total_revenue = 0
        items_sold = {}
        
        # Process each sale
        for i, sale in enumerate(sales_log):
            # Sale header
            text_widget.insert(END, f"Sale #{i+1} - {sale['timestamp']}\n")
            text_widget.insert(END, "-"*50 + "\n")
            
            # Items
            for item in sale['items']:
                text_widget.insert(END, f"{item['name']} x{item['quantity']} @ {item['price']}Rs = {item['subtotal']}Rs\n")
                
                # Update totals
                total_revenue += item['subtotal']
                
                # Update items sold count
                if item['name'] not in items_sold:
                    items_sold[item['name']] = 0
                items_sold[item['name']] += item['quantity']
            
            text_widget.insert(END, f"Total: {sale['total']}Rs\n\n")
        
        # Add summary
        text_widget.insert(END, "SUMMARY\n")
        text_widget.insert(END, "="*50 + "\n")
        text_widget.insert(END, f"Total Sales: {len(sales_log)}\n")
        text_widget.insert(END, f"Total Revenue: {total_revenue}Rs\n\n")
        
        text_widget.insert(END, "Items Sold:\n")
        for item_name, quantity in sorted(items_sold.items()):
            text_widget.insert(END, f"- {item_name}: {quantity}\n")
        
        # Make text widget read-only
        text_widget.config(state=DISABLED)
        
        # Add close button
        Button(report_window, text="Close", command=report_window.destroy).pack(pady=10)

# Main entry point
if __name__ == "__main__":
    root = Tk()
    app = VendingMachine(root)
    
    # Try to set icon
    try:
        root.iconbitmap("MUSKII :).ico")
    except:
        pass  # Silently fail if icon not found
    
    root.mainloop()
