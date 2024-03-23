CREATE TABLE test_user (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE kyakuhon (
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(30) NOT NULL,
    author VARCHAR(30) NOT NULL,
    genre INT NOT NULL,
    price INT NOT NULL,
    PRIMARY KEY (id)
);
