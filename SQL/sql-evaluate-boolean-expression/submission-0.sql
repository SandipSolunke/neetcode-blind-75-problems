-- Write your query below


select e.*,
case when e.operator='>'
then left_var.value > right_var.value

when e.operator='<'
then left_var.value < right_var.value

when e.operator='='
then left_var.value = right_var.value

end as value
 from 
expressions e
left join variables left_var ON e.left_operand = left_var.name
left join variables right_var ON e.right_operand = right_var.name
