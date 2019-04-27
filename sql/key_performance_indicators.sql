/*

As a data scientist, when youre not investigating spikes or dips in your data, you might be building dashboards of KPIs, or key performance indicators for a company.

KPIs are often displayed on TVs on the walls of the office, and serve as high level health metrics for the business. While every companys metrics are defined slightly differently, the basics are usually very similar.

In this lesson well take a look at basic KPIs like Daily Revenue, Daily Active Users, ARPU, and Retention for a video game, Mineblocks.

*/

select *
from purchases
order by id
limit 10;


select *
from gameplays
order by id
limit 10;


-- Daily revenue

select date(created_at),
	round(sum(price), 2)
from purchases
group by 1
order by 1;

/*

That query doesnt take refunds into account. Well update the query to exclude refunds.

Fields like refunded_at will only have data if the transaction was refunded, and otherwise left null.

*/

select date(created_at),
	round(sum(price), 2) as 'daily_rev'
from purchases
where refunded_at is null
group by 1
order by 1;

/*

Daily Active Users

Mineblocks is a game, and one of the core metrics to any game is the number people who play each day. That KPI is called Daily Active Users, or DAU.

DAU is defined as the number of unique players seen in-game each day. Its important not to double count users who played multiple times, so well use distinct in our count function.

Likewise, Weekly Active Users (WAU) and Monthly Active Users (MAU) are in the same family.

*/

select date(created_at),
	count(distinct user_id) as 'dau'
from gameplays
group by 1
order by 1;

/*

Previously we calculated DAU only per day, so the output we wanted was [date, dau_count]. Now we want DAU per platform, making the desired output [date, platform, dau_count].

*/

select date(created_at),
	platform,
	count(distinct user_id) as 'dau'
from gameplays
group by 1, 2
order by 1, 2;

/*

Daily Average Revenue Per Purchasing User

Weve looked at DAU and Daily Revenue in Mineblocks. Now we must understand the purchasing habits of our users.

Mineblocks, like every freemium game, has two types of users:

purchasers: users who have bought things in the game
players: users who play the game but have not yet purchased

*/

select date(created_at),
	round(sum(price) / count(distinct user_id), 2) as 'arppu'
from purchases
where refunded_at is null
group by 1
order by 1;

/*

Daily ARPU is defined as revenue divided by the number of players, per-day. To get that, well need to calculate the daily revenue and daily active users separately, and then join them on their dates.

One way to easily create and organize temporary results in a query is with CTEs, Common Table Expressions, also known as with clauses. The with clauses make it easy to define and use results in a more organized way than subqueries.

These clauses usually look like this:

with {subquery_name} as (
	{subquery_body}
)
select ...
from {subquery_name}
where ...

*/

with daily_revenue as (
	select date(created_at) as 'dt',
  	round(sum(price), 2) as 'rev'
	from purchases
	where refunded_at is null
    group by 1
)
select *
from daily_revenue
order by dt;

/*

You just built the first part of ARPU, daily_revenue. From here we can build the second half of ARPU in our with clause, daily_players, and use both together to create ARPU.

In the final select statement, daily_revenue.dt represents the date, while daily_revenue.rev / daily_players.players is the daily revenue divided by the number of players that day. In full, it represents how much the company is making per player, per day.

*/

with daily_revenue as (
	select date(created_at) as 'dt',
  	round(sum(price), 2) as 'rev'
	from purchases
	where refunded_at is null
    group by 1
),
daily_players as (
	select date(created_at) as 'dt',
  	count(distinct user_id) as 'players'
    from gameplays
    group by 1
)
select daily_revenue.dt,
	daily_revenue.rev / daily_players.players
from daily_revenue
join daily_players
using (dt);

/*

1 Day Retention

Now lets find out what percent of Mineblock players are returning to play the next day. This KPI is called 1 Day Retention.

Retention can be defined many different ways, but well stick to the most basic definition. For all players on Day N, well consider them retained if they came back to play again on Day N+1.

This will let us track whether or not Mineblocks is getting stickier over time. The stickier our game, the more days players will spend in-game.

And more time in-game means more opportunities to monetize and grow our business.

Before we can calculate retention we need to get our data formatted in a way where we can determine if a user returned.

Currently the gameplays table is a list of when the user played, and its not easy to see if any user came back.

By using a self-join, we can make multiple gameplays available on the same row of results. This will enable us to calculate retention.

The power of self-join comes from joining every row to every other row. This makes it possible to compare values from two different rows in the new result set. In our case, well compare rows that are one date apart from each user.

*/

select date(created_at) as 'dt',
	user_id
from gameplays as g1
order by dt
limit 100;

/*

Now well join gameplays on itself so that we can have access to all gameplays for each player, for each of their gameplays.

This is known as a self-join and will let us connect the players on Day N to the players on Day N+1. In order to join a table to itself, it must be aliased so we can access each copy separately.

We aliased gameplays in the query above because in the next step, we need to join gameplays to itself so we can get a result selecting [date, user_id, user_id_if_retained].

*/

select date(g1.created_at) as 'dt',
	g1.user_id
from gameplays as g1
join gameplays as g2
on g1.user_id = g2.user_id
order by 1
limit 100;

/*

Now that we have our gameplays table joined to itself, we can start to calculate retention.

1 Day Retention is defined as the number of players who returned the next day divided by the number of original players, per day. Suppose 10 players played Mineblocks on Dec 10th. If 4 of them play on Dec 11th, the 1 day retention for Dec 10th is 40%.

*/

select date(g1.created_at) as 'dt',
	g1.user_id,
    g2.user_id
from gameplays as g1
join gameplays as g2
on g1.user_id = g2.user_id
	and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
order by 1
limit 100;

/*

The above means 'only join rows where the date in g1 is one less than the date in g2', which makes it possible to see if users have returned!

The query above won’t return meaningful results because we’re using an inner join. This type of join requires that the condition be met for all rows, effectively limiting our selection to only the users that have returned.

Instead, we want to use a left join, this way all rows in g1 are preserved, leaving nulls in the rows from g2 where users did not return to play the next day.

*/

select date(g1.created_at) as 'dt',
	count(distinct g1.user_id) as 'total_users',
    count(distinct g2.user_id) as 'retained_users'
from gameplays as g1
left join gameplays as g2
on g1.user_id = g2.user_id
	and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;

/*

Now that we have retained users as count(distinct g2.user_id) and total users as count(distinct g1.user_id), divide retained users by total users to calculate 1 day retention!

*/

select date(g1.created_at) as 'dt',
	-- count(distinct g1.user_id) as 'total_users',
	-- count(distinct g2.user_id) as 'retained_users',
    round(count(distinct g2.user_id) * 100 / count(distinct g1.user_id)) as 'retention'
from gameplays as g1
left join gameplays as g2
on g1.user_id = g2.user_id
	and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;

/*

Common Metrics Conclusion
While every business has different metrics to track their success, most are based on revenue and usage.

The metrics in this lesson are merely a starting point, and from here you’ll be able to create and customize metrics to track whatever is most important to your company.

And remember, data science is exploratory! The current set of metrics can always be improved and there’s usually more to any spike or dip than what immediately meets the eye.

Let’s generalize what we’ve learned so far:

Key Performance Indicators are high level health metrics for a business.

Daily Revenue is the sum of money made per day.

Daily Active Users are the number of unique users seen each day

Daily Average Revenue Per Purchasing User (ARPPU) is the average amount of money spent by purchasers each day.

Daily Average Revenue Per User (ARPU) is the average amount of money across all users.

1 Day Retention is defined as the number of players from Day N who came back to play again on Day N+1.

*/
