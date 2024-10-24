select distinct t1.product_id, IFNULL(t2.price, 10) as price
from Products t1
left join (
    select
    product_id,
    first_value(new_price) over (partition by product_id order by change_date desc) as price
    from Products
    where change_date <= '2019-08-16'
    ) as t2
on t1.product_id = t2.product_id;