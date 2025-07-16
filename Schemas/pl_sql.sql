--Trigger that fires after a new row is inserted into the Users table. 
--It checks the new field SelectedCommunity and, if it is not "None", inserts a record into the Community_User table
DELIMITER $$
CREATE TRIGGER after_insert_users_community
AFTER INSERT ON Users
FOR EACH ROW
BEGIN
    -- Check if the user selected a community (i.e. the value is not 'None')
    IF NEW.SelectedCommunity IS NOT NULL AND NEW.SelectedCommunity <> 'None' THEN
        INSERT INTO Community_User (User_ID, Community_ID)
        VALUES (NEW.User_ID, NEW.SelectedCommunity);
    END IF;
END$$
DELIMITER ;

--Trigger to increment no of users in communities table after inserting a community user in the database
DELIMITER $$
CREATE TRIGGER after_insert_community_user
    AFTER INSERT ON Community_User
    FOR EACH ROW
    BEGIN
        UPDATE Communities
        SET No_of_Users = No_of_Users + 1
        WHERE Community_ID = NEW.Community_ID;
    END$$
DELIMITER ;

-- AFTER INSERT trigger on the Contributions table. The trigger will:
-- Retrieve the stored community of the contributor from the Users table.
-- Always update the user's No_of_contributions by +1.
-- If the ContributionCommunity (from the form) is not "None" and matches the user's stored SelectedCommunity, 
-- then also update the corresponding community’s Total_contributions by +1.

DELIMITER $$

CREATE TRIGGER after_insert_contribution
AFTER INSERT ON Contributions
FOR EACH ROW
BEGIN
    DECLARE userCommunity VARCHAR(10);
    
    -- Get the user’s stored community from the Users table.
    SELECT SelectedCommunity INTO userCommunity
      FROM Users
     WHERE User_ID = NEW.Contributor_ID;
    
    -- Always increment the user’s contribution count.
    UPDATE Users
       SET No_of_contributions = No_of_contributions + 1
     WHERE User_ID = NEW.Contributor_ID;
    
    -- If the chosen community is not 'None' and matches the user's stored community,
    -- update the community’s total contributions.
    IF NEW.ContributionCommunity <> 'None' AND NEW.ContributionCommunity = userCommunity THEN
        UPDATE Communities
           SET Total_contributions = Total_contributions + 1
         WHERE Community_ID = NEW.ContributionCommunity;
    END IF;
END$$

DELIMITER ;

--AFTER DELETE Trigger on the Community_User table so that when a user–community link is removed the community’s user count is updated
DELIMITER $$

CREATE TRIGGER after_delete_community_user
AFTER DELETE ON Community_User
FOR EACH ROW
BEGIN
    UPDATE Communities
    SET No_of_Users = No_of_Users - 1
    WHERE Community_ID = OLD.Community_ID;
END$$

DELIMITER ;
