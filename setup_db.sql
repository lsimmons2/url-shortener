
CREATE USER 'url_user'@'localhost'
IDENTIFIED BY 'url_pass';

GRANT ALL PRIVILEGES ON *.* TO 'url_user'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS urldb;

DROP TABLE IF EXISTS urldb.urls;

CREATE TABLE urldb.urls
(
  id INT NOT NULL AUTO_INCREMENT,
  true_url VARCHAR(255) NOT NULL,
  created DATETIME NOT NULL,
  UNIQUE (true_url),
  PRIMARY KEY(id)
);
