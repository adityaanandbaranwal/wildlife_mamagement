from extensions import db
from flask_login import UserMixin

class Habitat(db.Model):
    __tablename__ = 'Habitat'
    Habitat_ID = db.Column(db.Integer, primary_key=True)
    HabitatName = db.Column(db.String(255), nullable=False)
    Type = db.Column(db.String(50), nullable=False)

class Region(db.Model):
    __tablename__ = 'Region'
    Region_ID = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(100), nullable=False)
    City_Village = db.Column(db.String(100), nullable=False)

class HabitatRegion(db.Model):
    __tablename__ = 'Location'
    Location_ID = db.Column(db.Integer, primary_key=True)
    Habitat_ID = db.Column(db.Integer, db.ForeignKey('habitat.Habitat_ID'), nullable=False)
    Region_ID = db.Column(db.Integer, db.ForeignKey('region.Region_ID'), nullable=False)
    Area = db.Column(db.Float, nullable=False)
    Conservation_Status = db.Column(db.String(255))
    Climate = db.Column(db.String(100))

class Threats(db.Model):
    __tablename__ = 'Threats'
    Threat_ID = db.Column(db.Integer, primary_key=True)
    ThreatName = db.Column(db.String(255), nullable=False)

class LocationThreats(db.Model):
    __tablename__ = 'LocationThreats'
    Location_ID = db.Column(db.Integer, db.ForeignKey('location.Location_ID'), primary_key=True)
    Threat_ID = db.Column(db.Integer, db.ForeignKey('threats.Threat_ID'), primary_key=True)

class Species(db.Model):
    __tablename__ = 'Species'
    Species_ID = db.Column(db.Integer, primary_key=True)
    ScientificName = db.Column(db.String(255), nullable=False)
    EnglishName = db.Column(db.String(255))
    LocalName = db.Column(db.String(255))
    Type = db.Column(db.String(50), nullable=False)
    DietType = db.Column(db.String(50), nullable=False)

class PopulationTrend(db.Model):
    __tablename__ = 'PopulationTrend'
    Species_ID = db.Column(db.Integer, db.ForeignKey('species.Species_ID'), primary_key=True)
    Location_ID = db.Column(db.Integer, db.ForeignKey('location.Location_ID'), primary_key=True)
    Year = db.Column(db.String(4), primary_key=True)  # stored as string (e.g., "2025")
    PopulationCount = db.Column(db.Integer, nullable=False)

class Users(UserMixin, db.Model):
    __tablename__ = 'Users'
    User_ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Email_ID = db.Column(db.String(255), unique=True, nullable=False)
    UserName = db.Column(db.String(100), nullable=False)
    UserAddress = db.Column(db.Text)
    SelectedCommunity = db.Column(db.String(10))
    PasswordHash = db.Column(db.String(255), nullable=False)
    No_of_donations = db.Column(db.Integer, default=0)
    No_of_contributions = db.Column(db.Integer, default=0)
    Subscribed = db.Column(db.Boolean, default=False)

    def get_id(self):
        return str(self.User_ID)

class Communities(db.Model):
    __tablename__ = 'Communities'
    Community_ID = db.Column(db.Integer, primary_key=True)
    CommunityName = db.Column(db.String(255), nullable=False)
    No_of_Users = db.Column(db.Integer, default=0)
    Total_contributions = db.Column(db.Integer, default=0)
    Total_donations = db.Column(db.Float, default=0.0)

class CommunityUser(db.Model):
    __tablename__ = 'Community_User'
    User_ID = db.Column(db.Integer, db.ForeignKey('users.User_ID'), primary_key=True)
    Community_ID = db.Column(db.Integer, db.ForeignKey('communities.Community_ID'), primary_key=True)

class CommunityRegions(db.Model):
    __tablename__ = 'CommunityRegions'
    Region_ID = db.Column(db.Integer, db.ForeignKey('region.Region_ID'), primary_key=True)
    Community_ID = db.Column(db.Integer, db.ForeignKey('communities.Community_ID'), primary_key=True)

class CommunitiesUsers(db.Model):
    __tablename__ = 'Communities_Users'
    CU_ID = db.Column(db.Integer, primary_key=True)
    Community_ID = db.Column(db.Integer, db.ForeignKey('communities.Community_ID'), nullable=False)
    User_ID = db.Column(db.Integer, db.ForeignKey('users.User_ID'), nullable=False)
    No_of_contributions = db.Column(db.Integer, default=0)

class Contributions(db.Model):
    __tablename__ = 'Contributions'
    Contribution_ID = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    Image = db.Column(db.String(255))
    ObservationType = db.Column(db.String(255))
    Report = db.Column(db.Text)
    Contributor_ID = db.Column(db.Integer, db.ForeignKey('Users.User_ID'), nullable=False)
    ContributionCommunity = db.Column(db.String(10))  # will store the drop-down selected community

class UserContributions(db.Model):
    __tablename__ = 'UserContributions'
    Contribution_ID = db.Column(db.Integer, db.ForeignKey('contributions.Contribution_ID'), primary_key=True)
    CU_ID = db.Column(db.Integer, db.ForeignKey('communities_users.CU_ID'), primary_key=True)

class ContributionsToSpecies(db.Model):
    __tablename__ = 'Contributions_to_Species'
    Contribution_ID = db.Column(db.Integer, db.ForeignKey('contributions.Contribution_ID'), primary_key=True)
    Species_ID = db.Column(db.Integer, db.ForeignKey('species.Species_ID'), primary_key=True)

class Donations(db.Model):
    __tablename__ = 'Donations'
    Donation_ID = db.Column(db.Integer, primary_key=True)
    Transaction_ID = db.Column(db.String(255))
    MemberType = db.Column(db.String(50))
    DonationAmount = db.Column(db.Float, nullable=False)
    DonationDate = db.Column(db.Date, nullable=False)

class UserDonations(db.Model):
    __tablename__ = 'UserDonations'
    Donation_ID = db.Column(db.Integer, db.ForeignKey('donations.Donation_ID'), primary_key=True)
    CU_ID = db.Column(db.Integer, db.ForeignKey('communities_users.CU_ID'), primary_key=True)

class NewslettersUpdates(db.Model):
    __tablename__ = 'Newsletters_Updates'
    Newsletter_ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(255), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    Post_Date = db.Column(db.Date, nullable=False)
    Author = db.Column(db.String(255))
