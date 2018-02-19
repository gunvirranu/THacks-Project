drop table if exists users;
create table users (
    id integer primary key autoincrement,
    user text not null,
    email text not null,
    pass text not null,
    first text not null,
    period integer not null default 2,
    max_donation real not null default 0.50,
    min_amount real not null default 25.00
);