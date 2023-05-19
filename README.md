# Zennode-Task
Project Overview:
The project aims to create a program that simulates a shopping cart. It allows users to input quantities and gift wrap information for products from a catalog, applies discount rules based on the cart contents, calculates fees for shipping and gift wrapping, and provides a final total for the purchase.

Technologies and Approach:
To implement this project, we are using the Python programming language. Python is known for its simplicity and readability, making it an excellent choice for this task. We are coding the project using procedural programming, where the program flow follows a sequence of steps to achieve the desired functionality.

Code Explanation:
Let's break down the code and explain each part:

Catalog and Discount Rules:

The catalog dictionary stores the available products and their prices.
The discount_rules dictionary holds the discount rules and their corresponding thresholds and discount values.
Cart Calculation and Discounts:

The calculate_discount function determines the most beneficial discount rule applicable to the cart based on the discount rules and cart details.
It iterates through each discount rule and checks if the cart satisfies the rule's conditions. If it does, the rule is added to the applicable_discounts list.
The function returns the most beneficial discount by sorting the applicable discounts in descending order of discount amount and selecting the first rule.
If no discounts are applicable, the function returns None.
Cart Calculation and Details:

The calculate_cart function initializes a cart dictionary to store the cart details.
It prompts the user to input the quantity and gift wrap information for each product in the catalog, and it updates the cart dictionary accordingly.
The function calls calculate_discount to determine the applicable discount and updates the cart with the discount name and amount.
It calculates the shipping fee based on the total quantity of products, and it calculates the gift wrap fee for products that are selected for gift wrapping.
The subtotal, total, and other cart details are calculated and added to the cart dictionary.
Finally, the calculate_cart function returns the populated cart dictionary.
Program Execution and Output:

The main program starts by calling calculate_cart to obtain the cart details.
It then outputs the product details, subtotal, discount applied, shipping fee, gift wrap fee, and the final total to the console.
