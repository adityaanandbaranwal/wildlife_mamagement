-- drop table UserContributions;
-- drop table UserDonations;
-- drop table Communities_Users;
-- drop table Community_User;
-- drop table CommunityRegions;
-- drop table LocationThreats;
-- drop table Location;
-- drop table Habitat_Region;
-- drop table PopulationTrend;
-- drop table Contributions_to_Species;
-- drop table Habitat;
-- drop table Region;
-- drop table Threats;
-- drop table Species;
-- drop table Contributions;
-- drop table Users;
-- drop table Communities;
-- drop table Donations;

-- Create Habitat Table
CREATE TABLE Habitat (
    Habitat_ID INT PRIMARY KEY AUTO_INCREMENT,
    HabitatName VARCHAR(255) NOT NULL,
    Type VARCHAR(50) NOT NULL
);

-- Create Region Table
CREATE TABLE Region (
    Region_ID INT PRIMARY KEY AUTO_INCREMENT,
    State VARCHAR(100) NOT NULL,
    City_Village VARCHAR(100) NOT NULL
);

-- Create Habitat_Region Relationship Table
CREATE TABLE Habitat_Region (
    Habitat_ID INT,
    Region_ID INT,
    Area FLOAT NOT NULL,
    Conservation_Status VARCHAR(255),
    Climate VARCHAR(100),
    PRIMARY KEY (Habitat_ID, Region_ID),
    FOREIGN KEY (Habitat_ID) REFERENCES Habitat(Habitat_ID),
    FOREIGN KEY (Region_ID) REFERENCES Region(Region_ID)
);

-- Create Threats Table
CREATE TABLE Threats (
    Threat_ID INT PRIMARY KEY AUTO_INCREMENT,
    ThreatName VARCHAR(255) NOT NULL
);

-- Create Location Aggregate Table (HabitatRegion)
CREATE TABLE Location (
    Location_ID INT PRIMARY KEY AUTO_INCREMENT,
    Habitat_ID INT NOT NULL,
    Region_ID INT NOT NULL,
    Area FLOAT NOT NULL,
    Conservation_Status VARCHAR(255),
    Climate VARCHAR(100),
    FOREIGN KEY (Habitat_ID) REFERENCES Habitat(Habitat_ID),
    FOREIGN KEY (Region_ID) REFERENCES Region(Region_ID)
);

-- Create LocationThreats Relationship Table
CREATE TABLE LocationThreats (
    Location_ID INT,
    Threat_ID INT,
    PRIMARY KEY (Location_ID, Threat_ID),
    FOREIGN KEY (Location_ID) REFERENCES Location(Location_ID),
    FOREIGN KEY (Threat_ID) REFERENCES Threats(Threat_ID)
);

-- Create Species Table
CREATE TABLE Species (
    Species_ID INT PRIMARY KEY AUTO_INCREMENT,
    ScientificName VARCHAR(255) NOT NULL,
    EnglishName VARCHAR(255),
    LocalName VARCHAR(255),
    Type VARCHAR(50) NOT NULL,
    DietType VARCHAR(50) NOT NULL
);

-- Create PopulationTrend Relationship Table
CREATE TABLE PopulationTrend (
    Species_ID INT,
    Location_ID INT,
    Year YEAR NOT NULL,
    PopulationCount INT NOT NULL,
    PRIMARY KEY (Species_ID, Location_ID, Year),
    FOREIGN KEY (Species_ID) REFERENCES Species(Species_ID),
    FOREIGN KEY (Location_ID) REFERENCES Location(Location_ID)
);

-- Create Users Table
CREATE TABLE Users (
    User_ID INT PRIMARY KEY AUTO_INCREMENT,
    Email_ID VARCHAR(255) UNIQUE NOT NULL,
    UserName VARCHAR(100) NOT NULL,
    UserAddress TEXT,
    PasswordHash VARCHAR(255) NOT NULL,
    No_of_donations INT DEFAULT 0,
    No_of_contributions INT DEFAULT 0,
    Subscribed TINYINT(1) DEFAULT 0
);

-- Create Communities Table
CREATE TABLE Communities (
    Community_ID INT PRIMARY KEY AUTO_INCREMENT,
    CommunityName VARCHAR(255) NOT NULL,
    No_of_Users INT DEFAULT 0,
    Total_contributions INT DEFAULT 0,
    Total_donations FLOAT DEFAULT 0
);

-- Create Community_User Relationship Table
CREATE TABLE Community_User (
    User_ID INT,
    Community_ID INT,
    PRIMARY KEY (User_ID, Community_ID),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID),
    FOREIGN KEY (Community_ID) REFERENCES Communities(Community_ID)
);

-- Create CommunityRegions Relationship Table
CREATE TABLE CommunityRegions (
    Region_ID INT,
    Community_ID INT,
    PRIMARY KEY (Region_ID, Community_ID),
    FOREIGN KEY (Region_ID) REFERENCES Region(Region_ID),
    FOREIGN KEY (Community_ID) REFERENCES Communities(Community_ID)
);

-- Create Communities_Users Aggregate Table
CREATE TABLE Communities_Users (
    CU_ID INT PRIMARY KEY AUTO_INCREMENT,
    Community_ID INT NOT NULL,
    User_ID INT NOT NULL,
    No_of_contributions INT DEFAULT 0,
    FOREIGN KEY (Community_ID) REFERENCES Communities(Community_ID),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);

-- Create Contributions Table
CREATE TABLE Contributions (
    Contribution_ID INT PRIMARY KEY AUTO_INCREMENT,
    Date DATE NOT NULL,
    Image VARCHAR(255),
    ObservationType VARCHAR(255),
    Report TEXT
);

-- Create UserContributions Relationship Table
CREATE TABLE UserContributions (
    Contribution_ID INT,
    CU_ID INT,
    PRIMARY KEY (Contribution_ID, CU_ID),
    FOREIGN KEY (Contribution_ID) REFERENCES Contributions(Contribution_ID),
    FOREIGN KEY (CU_ID) REFERENCES Communities_Users(CU_ID)
);

-- Create Contributions_to_Species Relationship Table
CREATE TABLE Contributions_to_Species (
    Contribution_ID INT,
    Species_ID INT,
    PRIMARY KEY (Contribution_ID, Species_ID),
    FOREIGN KEY (Contribution_ID) REFERENCES Contributions(Contribution_ID),
    FOREIGN KEY (Species_ID) REFERENCES Species(Species_ID)
);

-- Create Donations Table
CREATE TABLE Donations (
    Donation_ID INT PRIMARY KEY,
    Transaction_ID VARCHAR(255),
    MemberType VARCHAR(50),
    DonationAmount FLOAT NOT NULL,
    DonationDate DATE NOT NULL
);

-- Create UserDonations Relationship Table
CREATE TABLE UserDonations (
    Donation_ID INT,
    CU_ID INT,
    PRIMARY KEY (Donation_ID, CU_ID),
    FOREIGN KEY (Donation_ID) REFERENCES Donations(Donation_ID),
    FOREIGN KEY (CU_ID) REFERENCES Communities_Users(CU_ID)
);

