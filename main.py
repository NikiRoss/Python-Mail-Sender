import smtplib
import datetime as dt

sender_email = 'niki.ross49@gmail.com'
password = 'wdpgpsdgfnmljbnj'
now = dt.datetime.now()
year = now.year
day_int = now.weekday()
month_int = now.month


    
def get_day_and_month(day_int, month_int):
    MONTHS = ['Jan','Feb','March','April','May','June','July','Aug','Sept','Oct','Nov','Dec']
    DAYS = ['Sun','Mon','Tues','Wed','Thurs','Fri','Sat','Sun']
    
    month = MONTHS[month_int -1]
    day = DAYS[day_int -1]
    str = f"{day}, {month}"
    return str
    

with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
    gmail_connection.starttls()
    gmail_connection.login(user=sender_email, password=password)
    gmail_connection.sendmail(
        from_addr=sender_email, 
        to_addrs="nikiross2011@icloud.com", 
        msg=f"Subject:Python SMTP\n\nSent from python project!!\n\n {get_day_and_month(day_int, month_int)}"
        )
    print(now)
    gmail_connection.close()
    


