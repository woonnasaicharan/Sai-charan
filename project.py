class Customer:
    def __init__(self,name,age,mail_id,phone,preferences):
        self.name = name
        self.age = age
        self.mail_id = mail_id
        self.phone = phone
        self.preferences = preferences
 
customer = Customer('Priya Sharma',25,'pr123@gmail.com','+913244455432',['electronics','accessories'])
 
 
class Vendor:
    def __init__(self,vendor_id, name, commission_rate):
        self.vendor_id = vendor_id
        self.name = name
        self.commission_rate = commission_rate
 
vendor = Vendor('E425','TechGear Solutions',15)
 
Payment_choice = ['UPI','Credit/Debit card','Cash on Delivery','Digital wallet']
while True:
    p = input('enter your payment choice:')
    if p in Payment_choice:
        print(f'you selected {p}')
        break
 
class Product():
    def __init__(self,vendor,product_id,name, price, category, specifications):
        self.vendor = vendor
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.specifications = specifications
 
product_1 = Product(vendor.name,'EP1001','Wireless Bluetooth Headphone',2999,customer.preferences[0],{'color':'black','warranty':'2 years'})
product_2 = Product(vendor.name,'EP1002','Phone Case',1299,customer.preferences[1],{'quality':'Premium Leather'})
product_3 = Product(vendor.name,'EP1003','Screen Protector',299,customer.preferences[1],{'material':'tempered glass'})
product_4 = Product(vendor.name,'EP1004',' Wireless Mouse pro',999,customer.preferences[0],{'color':'white','warranty':'3 years'})
product_5 = Product(vendor.name,'EP1005','USB-C Hub',199,customer.preferences[0],{'color':'red'})
product_6 = Product(vendor.name,'EP1006','Laptop Stand',499,customer.preferences[1],{'color':'grey','material':'steel'})
products = [product_1,product_2,product_3,product_4,product_5,product_6]
 
class Add_to_cart():
    def __init__(self,customer_id,add_cart):
        self.customer_id = customer_id
        self.add_cart = add_cart
 
 
items = [product_1.product_id,product_2.product_id,product_3.product_id,product_4.product_id,product_5.product_id,product_6.product_id]
 
cart = []
selected_products = []
while True:
    prod_id = input('enter product id(or done to stop):')
    if prod_id == 'done':
        break
    if prod_id in items:
        qty = int(input('enter quantity: '))
        cart.append({'id':prod_id,'qty':qty})
        for a in products:
            if a.product_id == prod_id:
                b = a.name
                t = a.price
                selected_products.append({b:t})
        print(f'Added {qty} of {prod_id} product ' )
print('Products added to cart:', cart)
print('Products you have selected are:', selected_products)
 
total_quantity = sum(item['qty'] for item in cart)
print('Total quantity:', total_quantity)
 
total_amount = 0
for i in cart:
    product_id = i['id']
    for j in products:
        if j.product_id == product_id :
            total_amount += j.price*i['qty']
print('Total amount:',total_amount)
 
 
added_to_cart = Add_to_cart(customer.mail_id,cart)
 
class update_iventory():
    def __init__(self,quantity_change, warehouse_id):
        self.quantity_change = quantity_change
        self.warehouse_id = warehouse_id
   
    def change_in_quanitity(self):
        self.quantity_change -= total_quantity
        return f'{self.quantity_change} stocks are left!!'
 
inventory = update_iventory(50,'WH_HYD')
print(inventory.change_in_quanitity())
 
class apply_discount():
    def __init__(self,cart_id,discount_code,discount_type):
        self.cart_id = cart_id
        self.discount_code = discount_code
        self.discount_type = discount_type
   
    def discount_process(self):
        if self.discount_type == 'percentage':
            if self.discount_code == 'NEWUSER20':
                discount_amount = total_amount*0.20
                final_amount = total_amount - discount_amount
                print('the amount with 20 percent discount is:',final_amount)
                return final_amount
 
discount = apply_discount(items,'NEWUSER20','percentage')
final_price = discount.discount_process()
 
class Process_Payment():
    def __init__(self,order_id, payment_method, amount, payment_details):
        self.order_id = order_id
        self.payment_method = payment_method
        self.amount = amount
        self.payment_details = payment_details
 
product_process = Process_Payment('#ORD789123',p,final_price,{p:customer.name,'phone no':customer.phone,})
 
class Create_Order():
    def __init__(self,customer_id, cart_items, shipping_address, payment_info):
        self.customer_id = customer_id
        self.cart_items = cart_items
        self.shipping_address = shipping_address
        self.payment_info = payment_info
 
create_order = Create_Order(customer.mail_id,cart,'Delhi',{'payment method':p,'amount':final_price,'status':'processing'})
 
class Calculate_Shipping_Cost():
    def __init__(self,order_weight, destination, shipping_method, shipping_cost):
        self.order_weight = order_weight
        self.destination = destination
        self.shipping_method = shipping_method
        self.shipping_cost = shipping_cost
 
cal_shipping_cost = Calculate_Shipping_Cost('500 g','Delhi','Ground Shipping',100)
cost = final_price + cal_shipping_cost.shipping_cost
 
class Update_Order_Status():
    def __init__(self,order_id, new_status, tracking_info):
        self.order_id = order_id
        self.new_status = new_status
        self.tracking_info = tracking_info
status = Update_Order_Status('#ORD789123',{'status':'Processing --> Shipped'},{'expected delivery':'18th June,2025','Id':'BP789123456IN'})
 
def generate_invoice(order_id):
    return order_id
c = generate_invoice('#ORD789123')
 
class Analyze_Sales_Trends():
    def __init__(self,time_period, filters):
        self.time_period = time_period
        self.filters = filters
    def show_trends(self):
        print(f"Analyzing sales trends for {self.time_period} with filters: {self.filters}")
        print("Top-selling category: Electronics")
        print("Peak sales time: 7-9 PM")
 
trends = Analyze_Sales_Trends("June 2025", {"category": "Electronics"})
 
class Manage_Returns():
    def __init__(self,order_id,return_reason, return_items):
        self.order_id = order_id
        self.return_reason =  return_reason
        self.return_items = return_items
   
    def process_return(self):
        print(f"Processing return for Order ID: {self.order_id}")
        print(f"Reason: {self.return_reason}")
        print(f"Items being returned: {self.return_items}")
        print("Return request submitted. Refund will be processed in 3-5 days")
 
order_id = input("Enter your Order ID: ")##ORD789123
reason = input("Why are you returning the product? ")#damaged product
item_to_be_returned = input("Which product are you returning? ")#
 
 
print('=== ORDER PROCESSING DASHBOARD ===')
print('Order ',product_process.order_id)
print('Customer: ',customer.name + ' (Premium Member)')
print('Status:',status.new_status['status'])
print(f'Payment: {total_amount},(paid via {p})\n')
print('Items Ordered:\n',selected_products)
print('\nPricing Breakdown:')
print('Subtotal:',total_amount)
print(f'Discount: {discount.discount_code}: {final_price}')
print(f'Shipping: {cal_shipping_cost.shipping_cost},{cal_shipping_cost.shipping_method}')
print(f'Total: {cost}')
print('\nShipping Details:')
print(f"From: {inventory.warehouse_id}\nTo:{cal_shipping_cost.destination}\nExpected Delivery:{status.tracking_info['expected delivery']}\nTracking: {status.tracking_info['Id']}\n\n")
print('=== VENDOR ANALYTICS ===')
print(f'Vendor: {vendor.name}\n,Commission Earned: {vendor.commission_rate}\nRatings:4.7/5\n')
print(f'Top Selling Products:\n {product_4.name}\n{product_5.name}\n{product_6.name}\n\n')
print('=== CUSTOMER DASHBOARD ===')
print(f'Preferred Category: {customer.preferences}\n')
 
print(trends.show_trends())
 
return_request = Manage_Returns(order_id, reason, [item_to_be_returned])
 
print(return_request.process_return())