# parkman

# Setup Instructions

virtualenv env
source env/bin/activate
pip install -r requirements.txt


# CREATE SQL tables
CREATE DATABASE twitter_status;
USE twitter_status;
CREATE TABLE user_status
(
    screen_name VARCHAR(200),
    status_id VARCHAR(200) NOT NULL,
    in_reply_to_status_id VARCHAR(200),
    PRIMARY KEY(screen_name)
);

CREATE TABLE raw_status
(
    id VARCHAR(200),
    text VARCHAR(200),
    PRIMARY KEY(id)
);
