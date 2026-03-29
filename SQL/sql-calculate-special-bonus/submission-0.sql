-- Write your query below
select employee_id,
Case
when employee_id%2=1 AND name NOT LIKE 'M%' THEN salary Else 0
end as bonus
from employees
order by employee_id;