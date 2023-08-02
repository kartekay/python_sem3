'''
Consider a show room of electronic products ,where there
are various
salesmen. Each sales man is given acommission of 5% ,
depending on the sales made per month. Incase the sale
done is less than 50000 ,then the sales man is not given any
commission. Write a function to calculate total sales of a
salesman in a month ,commission and remarks for the
salesman.Sales done by each sales man per week is to be
provided as input. Use tuples/list to store data of salesmen.
Assign remarks according to the following criteria:
Excellent:Sales>=80000
Good:Sales>=60000 and<80000
Average:Sales>=40000 and<60000
WorkHard:Sales<40000
'''

def calc(sale1, sale2, sale3, sale4):
    total_sales = sale1+sale2+sale3+sale4
    com_amt = 0 #Commission
    if total_sales >= 50000:
        com_amt = total_sales*0.05
    remarks = ""
    if total_sales >= 80000:
        remarks = "Excellent"
    elif total_sales >= 60000:
        remarks = "Good"
    elif total_sales >= 40000:
        remarks = "Average"
    elif total_sales < 40000:
        remarks = "Work Hard"

    return total_sales, com_amt, remarks

if __name__ == "__main__":
    sale1 = int(input("Enter the sales for week 1: "))
    sale2 = int(input("Enter the sales for week 2: "))
    sale3 = int(input("Enter the sales for week 3: "))
    sale4 = int(input("Enter the sales for week 4: "))
    t_sales, comm, remarks = calc(sale1, sale2, sale3, sale4)

    print("Total Sales: Rs.{:.2f}".format(t_sales))
    print("Commission: Rs.{:.2f}".format(comm))
    print("Remarks:", remarks)
