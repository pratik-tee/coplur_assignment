import csv
book=[
      ["Name","Address","Mobile","E-Mail"],
      ["Shubham","Jaipur","13456789","abc@gmail.xon"],
      ["Kartik","Bhartpur","859674123","def@gmail.coml"],
      ["Aman","Dolpur","7586489123","ghi@gmail.com"]
      ]
with open("book.csv","w",newline="") as file:
    writer=csv.writer(file)
    for x in book:
        writer.writerow(x)
    
with open("book.csv","r") as file:
    reader=csv.reader(file)
    for x in book:
        print(x)