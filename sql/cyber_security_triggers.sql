DELIMITER //

CREATE TRIGGER update_cyber_security
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    IF NEW.section = 'cyber security' THEN
        INSERT INTO cyber_security (roll_no, name, section, email, contact)
        VALUES (NEW.roll_no, NEW.name, NEW.section, NEW.email, NEW.contact);
    END IF;
END //

DELIMITER ;
