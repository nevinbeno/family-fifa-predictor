-- Procedure to insert a Fixture

delimiter //
create procedure add_match(in team1 varchar(20), in team2 varchar(20))
begin
    insert into Matches(date_of_match, Team_1, Team_2) 
    values (curdate(), team1, team2);
end //

-- to add the response
create procedure add_response
    (in id int, in rob varchar(20), in tan varchar(20),
    in nev varchar(20), in niy varchar(20));
begin
    insert into Response values (id, rob, tan, nev, niy);
end //

delimiter ;

-- to add match result
CREATE DEFINER=`manager`@`localhost` PROCEDURE `add_result`(in id int, in result varchar(20))
BEGIN
	insert into Match_Result values (id, result);
END