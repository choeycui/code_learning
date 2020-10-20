-- For PL/SQL, Oracle doesn't support for the create table as select query with predicates like 'group by', 'join', 'on', 'order by', etc.
-- If you want to create table from the select set, you can use 'with'

--example:

-- This will raise the issue:
create table as
(select * from table1) a
left join
(select * from table2) b
on a.id = b.id

-- Try this
create table as
with temp as (
(select * from table1) a
left join
(select * from table2) b
on a.id = b.id)
select * from temp;
