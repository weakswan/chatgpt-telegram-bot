-- Alter users table
ALTER TABLE users
    ALTER COLUMN user_id TYPE BIGINT;

-- Alter current_costs table
ALTER TABLE current_costs
    ALTER COLUMN user_id TYPE BIGINT USING user_id::BIGINT,
    ALTER COLUMN day TYPE INTEGER,
    ALTER COLUMN month TYPE INTEGER;

-- Alter usage_history table
ALTER TABLE usage_history
    ALTER COLUMN user_id TYPE BIGINT USING user_id::BIGINT;

-- Alter payments table
ALTER TABLE payments
    ALTER COLUMN user_id TYPE BIGINT USING user_id::BIGINT,
    ALTER COLUMN amount TYPE DECIMAL(10, 2),
    ALTER COLUMN payment_date TYPE TIMESTAMP;

-- Update foreign key relationships
-- You might need to drop and recreate the foreign keys if required.
