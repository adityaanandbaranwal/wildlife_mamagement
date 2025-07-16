INSERT INTO Species (ScientificName, EnglishName, LocalName, Type, DietType) VALUES
('Panthera tigris tigris', 'Bengal Tiger', 'Baagh', 'Mammal', 'Carnivore'),
('Elephas maximus indicus', 'Indian Elephant', 'Hathi', 'Mammal', 'Herbivore'),
('Python molurus', 'Indian Rock Python', 'Ajgar', 'Reptile', 'Carnivore'),
('Pavo cristatus', 'Indian Peafowl', 'Mor', 'Bird', 'Omnivore'),
('Gavialis gangeticus', 'Gharial', 'Gharial', 'Reptile', 'Carnivore'),
('Bos gaurus', 'Indian Bison (Gaur)', 'Gaur', 'Mammal', 'Herbivore'),
('Macaca mulatta', 'Rhesus Macaque', 'Bandar', 'Mammal', 'Omnivore'),
('Varanus bengalensis', 'Bengal Monitor', 'Goh', 'Reptile', 'Carnivore'),
('Corvus splendens', 'House Crow', 'Kauwa', 'Bird', 'Omnivore'),
('Axis axis', 'Chital (Spotted Deer)', 'Chital', 'Mammal', 'Herbivore'),
('Heteropneustes fossilis', 'Stinging Catfish', 'Singhi', 'Fish', 'Omnivore'),
('Rhinoceros unicornis', 'Indian Rhinoceros', 'Gainda', 'Mammal', 'Herbivore'),
('Bufo melanostictus', 'Common Indian Toad', 'Bhindi Mendak', 'Amphibian', 'Insectivore'),
('Melursus ursinus', 'Sloth Bear', 'Bhaloo', 'Mammal', 'Omnivore'),
('Accipiter badius', 'Shikra', 'Shikra', 'Bird', 'Carnivore'),
('Duttaphrynus melanostictus', 'Asian Common Toad', 'Mendak', 'Amphibian', 'Insectivore'),
('Psittacula krameri', 'Rose-ringed Parakeet', 'Tota', 'Bird', 'Herbivore'),
('Neofelis nebulosa', 'Clouded Leopard', 'Dhundli Chita', 'Mammal', 'Carnivore'),
('Ichthyophis beddomei', 'Beddome’s Caecilian', 'Jal Saap', 'Amphibian', 'Carnivore'),
('Rattus rattus', 'Black Rat', 'Chooha', 'Mammal', 'Omnivore');


INSERT INTO Habitat (HabitatName, Type) VALUES
('Sundarbans Mangrove Forest', 'Mangrove'),
('Western Ghats', 'Rainforest'),
('Thar Desert', 'Desert'),
('Himalayan Alpine Meadows', 'Alpine'),
('Kaziranga Floodplains', 'Grassland'),
('Rann of Kutch', 'Salt Marsh'),
('Keoladeo National Park Wetlands', 'Wetland'),
('Nilgiri Hills', 'Montane'),
('Coringa Mangrove Reserve', 'Mangrove'),
('Jim Corbett Forest', 'Deciduous'),
('Andaman Tropical Rainforest', 'Rainforest'),
('Chilika Lake', 'Brackish'),
('Valley of Flowers', 'Alpine'),
('Deccan Plateau', 'Dry Forest'),
('Sathyamangalam Forests', 'Dry Deciduous'),
('Loktak Lake', 'Freshwater'),
('Anamalai Tiger Reserve', 'Moist Forest'),
('Nallamala Forest', 'Tropical'),
('Dachigam National Park', 'Temperate'),
('Great Himalayan National Park', 'Coniferous');


INSERT INTO Region (State, City_Village) VALUES
('West Bengal', 'Sundarbans'),
('Assam', 'Kaziranga'),
('Rajasthan', 'Jaisalmer'),
('Uttarakhand', 'Nainital'),
('Kerala', 'Wayanad'),
('Tamil Nadu', 'Pollachi'),
('Gujarat', 'Bhuj'),
('Andhra Pradesh', 'Coringa'),
('Karnataka', 'Bandipur'),
('Odisha', 'Chilika'),
('Himachal Pradesh', 'Kullu'),
('Meghalaya', 'Cherrapunji'),
('Madhya Pradesh', 'Kanha'),
('Maharashtra', 'Tadoba'),
('Manipur', 'Moirang'),
('Arunachal Pradesh', 'Ziro'),
('Sikkim', 'Yuksom'),
('Jammu & Kashmir', 'Dachigam'),
('Bihar', 'Valmikinagar'),
('Punjab', 'Harike');

INSERT INTO Communities (CommunityName, No_of_Users, Total_contributions, Total_donations) VALUES
('Wildlife Conservation India', 0, 0, 0),
('Green Earth Foundation', 0, 0, 0),
('Clean Rivers Initiative', 0, 0, 0),
('Save the Tigers', 0, 0, 0),
('Forest Conservation Society', 0, 0, 0),
('Earth Warriors', 0, 0, 0),
('Plastic-Free India', 0, 0, 0),
('Ganga Rejuvenation Project', 0, 0, 0),
('Urban Green Spaces India', 0, 0, 0),
('Eco Warriors Network', 0, 0, 0),
('Himalayan Wildlife Rescue', 0, 0, 0),
('Clean Air India', 0, 0, 0),
('Coastal Conservation Trust', 0, 0, 0),
('Earth First India', 0, 0, 0),
('Green India Foundation', 0, 0, 0),
('Save Our Soil Initiative', 0, 0, 0),
('Water Conservation Council', 0, 0, 0),
('Clean India Movement', 0, 0, 0),
('Sustainable Agriculture India', 0, 0, 0),
('Nature Conservation Collective', 0, 0, 0);

INSERT INTO Location (Habitat_ID, Region_ID, Area, Conservation_Status, Climate) VALUES
(1, 1, 5000.5, 'Protected', 'Tropical Monsoon'),  -- Sundarbans Mangrove Forest in Sundarbans
(2, 1, 1200.0, 'Critical', 'Tropical Rainforest'),  -- Western Ghats in Sundarbans
(3, 2, 3500.0, 'Vulnerable', 'Arid'),  -- Thar Desert in Kaziranga
(4, 3, 2000.0, 'Protected', 'Alpine'),  -- Himalayan Alpine Meadows in Jaisalmer
(5, 4, 2500.0, 'Endangered', 'Tropical Savanna'),  -- Kaziranga Floodplains in Nainital
(6, 5, 1500.0, 'Critical', 'Arid'),  -- Rann of Kutch in Wayanad
(7, 6, 1000.0, 'Protected', 'Tropical Rainforest'),  -- Keoladeo National Park Wetlands in Pollachi
(8, 7, 1800.0, 'Vulnerable', 'Montane'),  -- Nilgiri Hills in Bhuj
(1, 8, 3000.0, 'Protected', 'Tropical Monsoon'),  -- Sundarbans Mangrove Forest in Coringa
(9, 9, 2200.0, 'Endangered', 'Tropical Rainforest'),  -- Jim Corbett Forest in Bandipur
(10, 10, 2500.0, 'Critical', 'Tropical Rainforest'),  -- Andaman Tropical Rainforest in Chilika
(11, 11, 1300.0, 'Vulnerable', 'Brackish'),  -- Chilika Lake in Kullu
(12, 12, 1700.0, 'Critical', 'Alpine'),  -- Valley of Flowers in Cherrapunji
(13, 13, 5000.0, 'Protected', 'Tropical Rainforest'),  -- Deccan Plateau in Kanha
(14, 14, 3800.0, 'Vulnerable', 'Moist Forest'),  -- Sathyamangalam Forests in Tadoba
(15, 15, 1600.0, 'Endangered', 'Tropical Rainforest'),  -- Loktak Lake in Moirang
(16, 16, 4000.0, 'Protected', 'Tropical Rainforest'),  -- Anamalai Tiger Reserve in Ziro
(17, 17, 2900.0, 'Critical', 'Tropical Monsoon'),  -- Nallamala Forest in Yuksom
(18, 18, 2100.0, 'Protected', 'Temperate'),  -- Dachigam National Park in Dachigam
(19, 19, 5500.0, 'Protected', 'Alpine');  -- Great Himalayan National Park in Valmikinagar







