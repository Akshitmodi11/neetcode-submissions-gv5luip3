-- Write your query below
select   c.customer_id, c.customer_name
from customers c
where c.customer_id In (
    select customer_id from orders where product_name='A'
)AND c.customer_id In 
(select customer_id from orders where product_name='B')
AND c.customer_id Not IN
(select customer_id from orders where product_name='C')
group by c.customer_id
order by c.customer_name;