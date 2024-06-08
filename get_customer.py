#create a customer data and find out id, emait and customer billing first name 
# upload the file on git and run the outcome on jenkins 
#create customer data
customer ={
    "id": 1782,
    "email": "test.foo@gmail.com",
    "first_name": "Ruksana",
    "last_name": "Rahman",
    "role": "customer",
    "username": "test.foo",
    "billing": {
        "first_name": "Ruksana",
        "last_name": "Rahman",
         "country": "USA",
        "state": "tx"},
     
}
# find the customer id
customer_info = customer['id']
#find the customer email
customer_email = customer["email"]
#find the customer billing first name
customer_billing_fname = customer["billing"]["first_name"]
print(f"I need the information of customer id:{customer_info}")
print (".........")
print (f"I need the customer email:  {customer_email}")
print (".........")
print (f"I need the customer billing first name:{customer_billing_fname}")



