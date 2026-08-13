# Write your MySQL query statement below
with t as (
select *,
        dense_rank() over(partition by product_id order by year) as rnk
from Sales)
select product_id, 
        year as first_year,
        quantity,price from t where rnk=1;
