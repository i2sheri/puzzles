Best Value Meal in Town
=======================
The Comptroller of a town has decided to publish the prices of every item on every menu of every restaurant all in a single CSV file.  In addition, the restaurants may offer Value Meals, which are groups of several items, at a discounted price.  The Comptroller has also included these Value Meals in the file.

The file's format is:
=====================
Single item:
restaurant_id,price,item_label

Value Meal (there can be any number of items in a value meal)
restaurant_id,price,item_1_label,item_2_label,...

restaurant_ids are integers,
item_labels are lower case letters with underscores,
price is a decimal number.
 
Write a program that accepts the town's price file, a list of item labels and print the restaurant they should go to, and the total price.
It is okay to purchase extra items, as long as the total cost is minimized.
 
Here are some sample data sets, program inputs, and the expected result:

Data File data.csv
1, 4.00, burger
1, 8.00, tofu_log
2, 5.00, burger
2, 6.50, tofu_log
program data.csv burger tofu_log
=> 2, 11.5

Data File data.csv
3, 4.00, chef_salad
3, 8.00, steak_salad_sandwich
4, 5.00, steak_salad_sandwich
4, 2.50, wine_spritzer
program data.csv chef_salad wine_spritzer
=> Menu Does not Exist

Data File data.csv
5, 4.00, extreme_fajita
5, 8.00, fancy_european_water
6, 5.00, fancy_european_water
6, 6.00, extreme_fajita, jalapeno_poppers, extra_salsa
program data.csv fancy_european_water extreme_fajita
=> 6, 11.0

