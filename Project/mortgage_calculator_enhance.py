# Find out how long a payoff a mortgage

principal= 500000
payment= 2684.11
rate= 0.05
total_paid= 0

#extra payment info

extra_payment= 1000
extra_payment_start_month= 1
extra_payment_end_month= 60
month= 0

# output to a file 
out=open("mortgage_report.txt",'w') #open a file for writing
print('{:>5s} {:>10s} {:>10s} {:>10s}'.format("Month","Interest","Remaining","Principal"),file=out)
while principal> 0:
    month+=1
    if month>=extra_payment_start_month and month<=extra_payment_end_month:
        total_payment= payment+extra_payment
    else:
        total_payment=payment

    interest=principal*rate/12
    principal=principal+interest-total_payment
    total_paid += total_payment
    print('{:> 5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month,interest,total_payment-interest,principal),file=out)

    #close the file
out.close()    

print("Total_paid",total_paid)