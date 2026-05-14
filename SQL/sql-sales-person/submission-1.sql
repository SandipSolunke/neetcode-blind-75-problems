-- Write your query below

select distinct name from sales_person
where sales_id not in (
select o.sales_id from 
orders o
inner join company c ON c.com_id = o.com_id and c.name='CRIMSON'
)
