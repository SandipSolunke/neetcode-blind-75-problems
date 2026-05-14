-- Write your query below

select 
c.customer_id, c.customer_name
from customers c 
where c.customer_id IN (
    select o.customer_id from orders o 
    where o.product_name IN ('A')
) AND 
c.customer_id IN (
    select o.customer_id from orders o 
    where o.product_name IN ('B')
) AND 
c.customer_id NOT IN (
    select o.customer_id from orders o 
    where o.product_name IN ('C')
) 
order by 2
