DELIMITER //

CREATE TRIGGER update_aiml
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    IF NEW.section = 'aiml' THEN
        INSERT INTO aiml (roll_no, name, section, email, contact)
        VALUES (NEW.roll_no, NEW.name, NEW.section, NEW.email, NEW.contact);
    END IF;
END //

DELIMITER ;
