# Online Store's Inventory Management System Database Schema
## Relationships

The schema is shown in the attached image, original drawio file is also attached.

The relationships of the schema are listed as below:

1. The Product table has a many-to-one relationship with the ProductType table. Each product can have only one product type, but a product type can be associated with multiple products.

2. The OrderItem table has a many-to-one relationship with both the Order table and the Product table. Each order item is associated with one order and one product, while an order can have multiple order items.

3. The Transaction table has a many-to-one relationship with the Product table. Each inventory transaction is associated with one product, while a product can have multiple inventory transactions.

## Constraints

Data value's size constraints may varies accordingly with DB specifications, so only null constraints are applied to properties that are required in each table.