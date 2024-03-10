-- New migration for altering current_costs table
ALTER TABLE current_costs
    ALTER COLUMN day TYPE FLOAT USING day::FLOAT,
    ALTER COLUMN month TYPE FLOAT USING month::FLOAT;
