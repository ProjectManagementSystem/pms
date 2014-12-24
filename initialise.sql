create table users(
userid int(8) not null,
name varchar(128) not null,
surname varchar(128) not null,
email varchar(128) not null,
password varchar(512) not null,
phone varchar(128),
facebookid varchar(128),
registrationdate date not null,
primary key (userid)
);

create table organization(
oid int(8) not null,
name varchar(128) not null,
email varchar(512),
webpage varchar(512),
phone varchar(128),
logopath varchar(1000),/*file path. eminim*/
primary key (oid)
);

create table member(
mid int(8) not null,/*member id olmasina o kadar da gerek yok aslinda*/
userid int(8) not null,
foreign key (userid) references users (userid),
accesslevel int not null,
oid int(8) not null,/*bir organizasyona 2 kere kaydolamayacagimiza gore oid + userid primary key olabilirdi*/
foreign key (oid) references organization (oid),
primary key (mid)
);

create table event(
eid int(10) not null,
oid int(8) not null,
foreign key (oid) references organization (oid),
name varchar(128) not null,
edate date,/*event date. time dahil*/
capacity int(8),
repetition int(5),
repetitionend date,
/*haftalik, aylik, 3 gunde 1 gibi)*/
/*repetition software'da bir kurala gore handle edilecek*/
/*3 gunde 1 seklinde olabilir, her gun olmak uzere toplam 4 repetition olabilir*/
photo varchar(1000),
/*filepath, eminim*/
/*eger birden fazla photo olacaksa bunu baska bir table'da tutmamiz lazim*/
location varchar(1000),
primary key(eid)
/*events also may have tasks, we'll look at that*/
);

create table task(
tid int(10) not null,
oid int(10) not null,
foreign key (oid) references organization (oid),
description varchar(1000) not null,
due date,
owner int(8) not null,
foreign key (owner) references member (mid),
primary key (tid)
);
