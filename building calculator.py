str_length = input("Please Enter Your Length: \n")
str_width = input("Please Enter Your width: \n")
str_price = input("How much price for 1 meter: \n")
# تحويل المدخلات الى رقم عشري
lenght = float(str_length)
width = float(str_width)
price = float(str_price)
# حساب المساحة و المبلغ
area = lenght * width
amount = area * price
str_area = str(area)
str_amount = str(amount)
curancy = "$"
print("the total Area is: ", str_area, "\n" + "Give The Guy: ",
      curancy + str_amount)
