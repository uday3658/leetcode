-- select department,Employee,Salary 
-- from Employee e join Department d
--     on e.departmentId=d.id
with t as(
    select
        d.name AS department,
        e.name AS Employee,
        e.salary AS Salary,
    DENSE_RANK() over(partition by e.departmentId order by e.salary desc) as rnk
    from Employee e join Department d
        on e.departmentId=d.id
)
select department,
    Employee,
    Salary from t where rnk<=3;

