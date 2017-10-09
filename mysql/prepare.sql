DELETE FROM mysql.user WHERE User='';
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1');
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
CREATE DATABASE gyazai DEFAULT CHARACTER SET utf8;
USE gyazai;
CREATE TABLE card_data
    (
    jan_name varchar(255),
    eng_name varchar(255),
    jan_text varchar(1023),
    eng_text varchar(1023),
    type varchar(127),
    power_toughness varchar(15),
    mana_cost varchar(15)
    );
GRANT SELECT,UPDATE,INSERT,DELETE ON `gyazai`.card_data TO `gyazai_user`@`localhost`;
