from time import strftime

def calculate_age(day:int=0,month:int=0,year:int=0)->str:
    y=strftime("%Y")
    d=strftime("%d")
    m=strftime("%m")
    total_years=int(y)-year
    total_days=int(d)-day
    total_months=int(m)-month
    if total_days<0:
        total_days=str(total_days)
        total_days=total_days.replace("-","")
        total_days=int(total_days)
        total_days=30-total_days
        total_months=total_months-1
    if total_months<0:
        total_months=str(total_months)
        total_months=total_months.replace("-","")
        total_months=int(total_months)
        total_months=12-total_months
        total_years=total_years-1
    print(f"Your age is {total_days} Days, {total_months} Months and {total_years} Years")
    if total_days==0 and total_months==0:
        print("Wow! Today is you Birthday...")
        print(".............Happy Birth Day To You........")

    
    
while True:
    user=input("Enter your dateofbirth like this (day month year). Use spaces for difference: ")
    try:
        user=user.split(" ")
        if len(user)>3:
            print("You entered wrong age.... try again...")
        else:
            d=user[0]
            m=user[1]
            y=user[2]
            calculate_age(int(d),int(m),int(y))
            exit_programe=input("Do you want exit this programe (y or n): ")
            if exit_programe=="y":
                exit()
    except IndexError:
        print("You entered wrong age.... try again...")
    
    