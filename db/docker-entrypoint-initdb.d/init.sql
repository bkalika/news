create user bohdan password 'bohdan';

create database news encoding 'utf-8';
grant all privileges on database news to bohdan;
alter database news owner to bohdan;
