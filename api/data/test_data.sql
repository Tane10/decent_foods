BEGIN;

INSERT OR IGNORE INTO users (id, name, email, wallet_uuid, deleted)
VALUES (1, 'Alice', 'alice@example.com', '1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71', 0),
       (2, 'Bob', 'bob@example.com', '2PwX6KuUC1w6FkTkZ7EsBfT6LpJHn43aC8', 0),
       (3, 'Charlie', 'charlie@example.com', '3NzZifS4T6yC24ERpYzMd6kF3N5GfRRW6Y', 0),
       (4, 'David', 'david@example.com', '4D2b61U4hX5CijWE2f7vB8e5T4U72h39Ls', 1),
       (5, 'Eve', 'eve@example.com', '5EoV2r5iN8mFkXyF1hR8T4bZ4X2Uj9iKtD', 0);



INSERT OR IGNORE INTO transactions (id, timestamp, cost, sellers_wallet_uuid, customer_wallet_uuid, product_uuid,
                                    delivery_option, longitude, latitude)
VALUES (1, 1643155200, 1500, '1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71', '5EoV2r5iN8mFkXyF1hR8T4bZ4X2Uj9iKtD', 1, 'Standard',
        -73.935242, 40.730610),
       (2, 1643068800, 500, '2PwX6KuUC1w6FkTkZ7EsBfT6LpJHn43aC8', '3NzZifS4T6yC24ERpYzMd6kF3N5GfRRW6Y', 2, 'Express',
        -118.243683, 34.052235),
       (3, 1642982400, 2000, '3NzZifS4T6yC24ERpYzMd6kF3N5GfRRW6Y', '1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71', 3, 'Standard',
        -87.629798, 41.878113),
       (4, 1642896000, 100, '4D2b61U4hX5CijWE2f7vB8e5T4U72h39Ls', '2PwX6KuUC1w6FkTkZ7EsBfT6LpJHn43aC8', 1, 'Pickup',
        NULL, NULL),
       (5, 1642809600, 700, '5EoV2r5iN8mFkXyF1hR8T4bZ4X2Uj9iKtD', '4D2b61U4hX5CijWE2f7vB8e5T4U72h39Ls', 2, 'Express',
        -118.243683, 34.052235);


INSERT OR IGNORE INTO products (id, cost, sellers_uuid, description, name, deleted, image)
VALUES (1, 2000, '3NzZifS4T6yC24ERpYzMd6kF3N5GfRRW6Y', 'High-quality laptop for professional use', 'Laptop', NULL,
        NULL),
       (2, 500, '2PwX6KuUC1w6FkTkZ7EsBfT6LpJHn43aC8', 'Stylish headphones with noise cancellation', 'Headphones', NULL,
        NULL),
       (3, 1500, '1Lbcfr7sAHTD9CgdQo3HTMTkV8LK4ZnX71', 'Classic novel loved by readers worldwide', 'Book', NULL, NULL),
       (4, 100, '4D2b61U4hX5CijWE2f7vB8e5T4U72h39Ls', 'Compact umbrella for rainy days', 'Umbrella', 1, NULL),
       (5, 700, '5EoV2r5iN8mFkXyF1hR8T4bZ4X2Uj9iKtD', 'Elegant watch for formal occasions', 'Watch', NULL, NULL);


COMMIT;
