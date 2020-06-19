

DROP TABLE IF EXISTS Websites;

CREATE TYPE ages AS ENUM ('kids', 'teens', 'adults', 'all');
CREATE TYPE categories AS ENUM ('general', 'typing', 'math', 'reading', 'science');

CREATE TABLE Websites (
    website_id SERIAL PRIMARY KEY,
    name varchar(50) NOT NULL,
    description text,
    url varchar(100) NOT NULL,
    age ages,
    category categories
);

