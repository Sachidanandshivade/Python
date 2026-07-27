fruit_list = ["apple", "banana", "cherry", "date", "elderberry"];
print(fruit_list);
print(fruit_list[1]);

fruit_list[2] = "coconut";
print(fruit_list);

fruit_list.append("fig");
print(fruit_list);

fruit_list.remove("apple");
print(fruit_list);

fruit_list.pop(0);
del fruit_list[1];
print(fruit_list);