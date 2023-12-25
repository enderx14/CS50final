CREATE TRIGGER enforce_date_format
BEFORE INSERT ON bookings
BEGIN
    SELECT CASE
        WHEN new.EventDate NOT LIKE '__-__-____' THEN
            RAISE (ABORT, 'Invalid date format. Use DD-MM-YYYY.');
    END;
END;


CREATE TRIGGER set_default_field2
AFTER INSERT ON my_table
BEGIN
    UPDATE my_table
    SET field2 = NEW.field1
    WHERE id = NEW.id;
END;