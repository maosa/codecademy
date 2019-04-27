select *
from orders
order by id
limit 100;

select *
from order_items
order by id
limit 100;


select date(ordered_at)
from orders
order by 1
limit 100;


select date(ordered_at), count(1)
from orders
group by 1
order by 1;

Get daily revenue from kale smoothies

select date(ordered_at), round(sum(amount_paid), 2)
from orders
join order_items
on orders.id = order_items.order_id
where name = 'kale-smoothie'
group by 1
order by 1;

-- #####

select name, round(sum(amount_paid), 2)
from order_items
group by name
order by 2 desc;

-- ##### Subquery

select name,
    round(sum(amount_paid) / (select sum(amount_paid) from order_items) * 100, 2)
from order_items
group by 1
order by 2 desc;

-- #####

-- 1.0 * is a shortcut to ensure the database represents the percent as a decimal

select
    case name
      	when 'kale-smoothie' then 'smoothie'
        when 'banana-smoothie' then 'smoothie'
        when 'orange-juice' then 'drink'
        when 'soda' then 'drink'
        when 'blt' then 'sandwich'
        when 'grilled-cheese' then 'sandwich'
        when 'tikka-masala' then 'dinner'
        when 'chicken-parm' then 'dinner'
        else 'other'
    end as 'category', round(1.0 * sum(amount_paid) / (select sum(amount_paid) from order_items) * 100, 2) as 'pct'
from order_items
group by 1
order by 2 desc;

/*

We’ll define reorder rate as the ratio of the total number of orders to the number of people making those orders.

A lower ratio means most of the orders are reorders.

A higher ratio means more of the orders are first purchases.

*/

-- Get the number of orders per dish

select name, count(distinct order_id)
from order_items
group by 1
order by 1;


select name,
    round(1.0 * count(distinct order_id) / count( distinct delivered_to), 2)
from order_items
join orders
on orders.id = order_items.order_id
group by 1
order by 2 desc;

/*

Let’s generalize what we’ve learned so far:

Data aggregation is the grouping of data in summary form.

Daily Count is the count of orders in a day.

Daily Revenue Count is the revenue on orders per day.

Product Sum is the total revenue of a product.

Subqueries can be used to perform complicated calculations and create filtered or aggregate tables on the fly.

Reorder Rate is the ratio of the total number of orders to the number of people making orders.

*/
