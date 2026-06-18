-- Trigger to update score once the result has been announced

delimiter //

create trigger update_score
after insert 
on Match_Result
for each row
begin

    insert into Score
        select r.Match_number, (r.Robin = new.Result), 
                (r.Tanya = new.Result), 
                (r.Nevin =new.Result), 
                (r.Niya = new.Result)
        from Response r 
        where r.Match_number = new.Match_number;
end //

delimiter ;