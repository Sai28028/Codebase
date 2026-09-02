print("----------------------------")
print("Student List - DML Operation")
print("----------------------------")
students_list=["Aditi","Rahul","Priya","Rohan"]
print("original list:",students_list)

students_list.append("Sneha")
print("After adding:", students_list)

students_list.remove("Rahul")
print("After deleting:",students_list)

students_list[1]="Neha"
print("After updating:",students_list)
print("Final list:",students_list)

students_tuple=("Aditi","Rahul","Priya","Rohan")
print("original tuple:",students_tuple)
y=list(students_tuple)
y.append("Sneha")

print("After adding:", y)
y.remove("Rahul")
print("After removing:",y)

y[1]="Neha"
students_tuple=tuple(y)

print("After updating:", students_tuple)
print("Final tuple:", students_tuple)

print("----------------------------------")
print("Student Dictionary - DML Operation")
print("----------------------------------")

students_dict={
 "101":"Aditi",
 "102":"Rahul",
 "103":"Priya"
}
print("Original dictionary:",students_dict)

students_dict["104"]="Rohan"
print("After adding:",students_dict)

students_dict.pop("102")
print("After removing:", students_dict)

students_dict["101"]="Neha"
print("After updating:", students_dict)
print("Final dictionary:", students_dict)
