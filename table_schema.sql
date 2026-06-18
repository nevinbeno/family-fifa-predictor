create table Matches 
    (Match_number int primary key auto_increment, 
    date_of_match date, 
    Team_1 varchar(20), 
    Team_2 varchar(20));

create table Response
    (Match_number int primary key,
    Robin varchar(20), 
    Tanya varchar(20), 
    Nevin varchar(20), 
    Niya varchar(20),
    foreign key (Match_number) references Matches(Match_number));
    
create table Match_Result
    (Match_number int primary key, 
    Result varchar(20), 
    foreign key (Match_number) references Matches(Match_number));

create table Score
    (Match_number int primary key, 
    Robin int,
    Tanya int, 
    Nevin int, 
    Niya int, 
    foreign key (Match_number) references Matches(Match_number));

create view Total_Score as
    select sum(Robin) as Robin, 
    sum(Tanya) as Tanya, 
    sum(Nevin) as Nevin, 
    sum(Niya) as Niya
    from score