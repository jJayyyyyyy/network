drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title text not null,
	art text not null
);
