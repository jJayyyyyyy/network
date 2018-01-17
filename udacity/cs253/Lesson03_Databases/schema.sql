drop table if exists entries;
create table entries (
	art_id integer primary key autoincrement,
	subject text not null,
	content text not null
);
