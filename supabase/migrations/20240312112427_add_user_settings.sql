CREATE TABLE user_settings (
    setting_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users,
    model_name TEXT,
    brain TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
