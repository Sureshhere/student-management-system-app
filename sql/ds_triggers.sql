DELIMITER //

CREATE TRIGGER update_data_science
AFTER INSERT ON students
FOR EACH ROW
BEGIN
    IF NEW.section = 'data science' THEN
        INSERT INTO data_science (roll_no, name, section, email, contact)
        VALUES (NEW.roll_no, NEW.name, NEW.section, NEW.email, NEW.contact);
    END IF;
END //

DELIMITER ;
