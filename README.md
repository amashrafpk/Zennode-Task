# Zennode-Task
Program Overview:
This program simulates a shopping cart system. It allows users to input the quantity of each product they want to purchase and specify whether they want gift wrapping for each product. The program calculates the subtotal, applies applicable discounts based on predefined rules, calculates shipping and gift wrap fees, and provides a final total for the purchase.

Technologies and Approach:
The program is written in Python, a popular and versatile programming language. Python's simplicity and readability make it suitable for implementing this project. The approach used in this program is procedural programming, where the code follows a sequence of steps to achieve the desired functionality.

Code Explanation:

Catalog and Discount Rules:
The catalog dictionary represents the available products and their corresponding prices. It acts as a reference for product names and prices.
The discount_rules dictionary contains predefined discount rules along with their thresholds and discount amounts. These rules define when and how discounts are applied to the cart.

Cart Calculation and Discounts:

The calculate_discount function takes the cart details as input and determines the most beneficial discount rule based on the cart's subtotal, total quantity, and individual product quantities.
The function iterates through each discount rule and checks if the cart meets the conditions defined by the rule. If it does, the rule is added to the applicable_discounts list.
The applicable discounts are sorted in descending order of discount amount, and the most beneficial rule is returned. If no discounts apply, None is returned.
Cart Calculation and Details:

The calculate_cart function initializes a cart dictionary to store the cart details, such as the products, subtotal, total quantity, discount information, shipping fee, gift wrap fee, and total amount.
The function prompts the user to input the quantity and gift wrap preference for each product in the catalog.
The cart details are updated accordingly, including the subtotal and total quantity.
The calculate_discount function is called to determine the applicable discount rule for the cart. If a discount applies, the discount name and amount are added to the cart.
The shipping fee is calculated based on the total quantity of products, and the gift wrap fee is calculated based on the gift wrap preference for each product.
The final total is calculated by subtracting the discount amount from the subtotal and adding the shipping fee and gift wrap fee.
Finally, the populated cart dictionary is returned by the calculate_cart function.

Program Execution and Output:
The program starts by calling the calculate_cart function to obtain the cart details.
The program then displays the product details (name, quantity, total amount) for each product in the cart.
The subtotal, discount applied, shipping fee, gift wrap fee, and final total are displayed to the user.
