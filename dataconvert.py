from khayyam import JalaliDate

# دریافت تاریخ شمسی از کاربر
shamsi_date = input("لطفاً تاریخ شمسی را به صورت (YYYY/MM/DD) وارد کنید: ")

# جدا کردن سال، ماه و روز از تاریخ وارد شده
year, month, day = map(int, shamsi_date.split('/'))

# تبدیل تاریخ شمسی به میلادی
miladi_date = JalaliDate(year, month, day).todate()

print(f"تاریخ میلادی معادل: {miladi_date}")
