DELIMITER //
CREATE PROCEDURE `sp_list_avengers`()
BEGIN
    SELECT AV.id, AV.name, AV.url 
    FROM avengers AV
    ORDER BY AV.name ASC;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE `sp_products_by_category`(IN category VARCHAR(60))
BEGIN
    SELECT PR.id, PR.name, PR.price 
    FROM products PR
    WHERE PR.category = category AND PR.released = 1
    ORDER BY PR.name ASC;
END //
DELIMITER ;