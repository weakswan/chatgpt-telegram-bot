CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name TEXT UNIQUE
);

CREATE TABLE current_costs (
    user_id INT PRIMARY KEY REFERENCES users,
    day NUMERIC,
    month NUMERIC,
    all_time NUMERIC,
    last_update DATE
);

CREATE TABLE usage_history (
    user_id INT REFERENCES users,
    date DATE,
    chat_tokens JSONB,
    transcription_seconds JSONB,
    number_images JSONB,
    tts_characters JSONB,
    vision_tokens JSONB,
    PRIMARY KEY (user_id, date)
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users,
    amount NUMERIC,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT,
    status TEXT
);
