-- Write your query below
select c.name
from customers c left join orders r
on c.id=r.customer_id
where r.customer_id is null;