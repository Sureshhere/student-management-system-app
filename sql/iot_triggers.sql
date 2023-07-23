DELIMITER //

CREATE TRIGGER update_iot
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    IF NEW.section = 'iot' THEN
        INSERT INTO iot (roll_no, name, section, email, contact)
        VALUES (NEW.roll_no, NEW.name, NEW.section, NEW.email, NEW.contact);
    END IF;
END //

DELIMITER ;
