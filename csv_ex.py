line_counter = 0
data_header = []
customer_list = []
Customer_USA_only_list = []
customer = None


#csv파일 읽기

with open ("customers.csv") as customer_data:

    while 1:
        data = customer_data.readline()
        if not data: break
        if line_counter==0:
            data_header = data.split(",")
        else:
            customer_list.append(data.split(","))
        line_counter += 1

print("Header : \t", data_header)
for i in range(0, 10):
    print ("Data",i,":\t\t",customer_list[i])
print(len(customer_list))


#csv파일 쓰기


with open ("customers.csv","r") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data: break
        if line_counter==0:
            data_header = data.split(",")
        else:
            customer = data.split(",")
            if customer[10].upper() == "USA":
                Customer_USA_only_list.append(customer)
        line_counter+=1

print("Header : \t", data_header)

for i in range(0, 10):
    print ("Data",i,":\t\t",Customer_USA_only_list[i])
print(len(Customer_USA_only_list))



with open ("NEWCustomer_USA_only","w") as Customer_USA_only_csv:
    for customer in Customer_USA_only_list:
        Customer_USA_only_csv.write(",".join(customer).strip('\n')+"\n")
