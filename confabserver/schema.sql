CREATE TABLE IF NOT EXISTS login_data(
user_id SERIAL PRIMARY KEY,
username varchar(100) NOT NULL,
password varchar (100) NOT NULL,
token varchar (100),
last_login TIMESTAMP,
client_data varchar(100));



