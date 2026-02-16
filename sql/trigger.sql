use ecom;
create table order_cancellations (
	log_id int primary key auto_increment,
    order_id int,
    cancelled_on datetime,
    reason varchar (100)
);

DELIMITER //

CREATE TRIGGER trg_log_order_cancel
AFTER UPDATE ON orders
FOR each row
begin
	if new.order_status = 'cancelled'
		and old.order_status <> 'cancelled' then
        
			insert into order_cancellations
            (order_id, cancelled_on, reason)
            values
            (new.order_id, now(), 'order cancelled by user');
	END if;
END //

DELIMITER ;

update orders
set order_status = 'cancelled'
where order_id = 3;

select * from order_cancellations;
