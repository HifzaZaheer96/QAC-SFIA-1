BEGIN;

-- Database: `shoppingapp_db`
--
-- --------------------------------------------------------
--
-- Table structure for table `tops`
--
DROP DATABASE IF EXISTS shoppingapp;
CREATE DATABASE shoppingapp;
use shoppingapp;
DROP TABLE IF EXISTS tops;


--
-- Table structure for table `wardrobe`
--

DROP TABLE IF EXISTS wardrobe;

CREATE TABLE `wardrobe` (
  `Wardrobe_ID` int(6) NOT NULL AUTO_INCREMENT,
  `Wardrobe_Description` varchar(30) NOT NULL,
  `Wardrobe_Capacity` varchar(30) NOT NULL,
  `Wardrobe_Colour` varchar(30) NOT NULL,
  PRIMARY KEY(Wardrobe_ID)
);


-- Insert content for table `tops`
--
INSERT INTO wardrobe (Wardrobe_Description, Wardrobe_Capacity, Wardrobe_Colour) 
VALUES ('Summer','79x176cm','White'), ('Winter','82x180cm','Black');


CREATE TABLE `tops` (
  `Top_ID` int(6) NOT NULL AUTO_INCREMENT,
  `Top_Image` varchar(500) NULL,
  `Top_Description` varchar(30) NOT NULL,
  `Top_Size` int(2) NOT NULL,
  `Top_Colour` varchar(30) NOT NULL,
  `Top_Price` varchar(10) NOT NULL,
  `Wardrobe_ID` int(6) NOT NULL,
  PRIMARY KEY(Top_ID), FOREIGN KEY(Wardrobe_ID) REFERENCES wardrobe (Wardrobe_ID)
);
-- --------------------------------------------------------

-- Insert content for table `tops`
--
INSERT INTO tops (Top_Description, Top_Image,Top_Size, Top_Colour,Top_Price,Wardrobe_ID) 
VALUES 
('Smock Chiffon Top','https://i.pinimg.com/originals/d4/e0/7f/d4e07fb33814fb2050da67aae88661cc.jpg','6','Pink','10', (SELECT Wardrobe_ID from wardrobe WHERE Wardrobe_ID = 1)),
('Jersey T-shirt','https://img.ltwebstatic.com/images3_pi/2019/09/27/1569574094d7a0820ed3b28c55ae5a8248e5a33440_thumbnail_600x.webp','8','White','8', (SELECT Wardrobe_ID from wardrobe WHERE Wardrobe_ID = 1)), 
('Jumper','https://m.media-amazon.com/images/I/61-yYdvj5gL._SR500,500_.jpg','12','Blue','20', (SELECT Wardrobe_ID from wardrobe WHERE Wardrobe_ID = 2)),
('Sweatshirt','https://www.dhresource.com/webp/m/0x0s/f2-albu-g8-M00-65-A1-rBVaVFwJDfOAIpZxAAsOD1Q5y2w173.jpg/2019-women-039-s-clothing-winter-sweatershirts.jpg','6','Brown','30', (SELECT Wardrobe_ID from wardrobe WHERE Wardrobe_ID = 2)),
('Raglan Sleeve Jumper','https://img.ltwebstatic.com/images3_pi/2019/10/31/1572507911dac54d6fb142d8ef08d845414b692803_thumbnail_600x.webp','6','White','15', (SELECT Wardrobe_ID from wardrobe WHERE Wardrobe_ID = 2)),
('Rose-Pink T-shirt','https://img.ltwebstatic.com/images2_pi/2019/07/03/1562143662675996227_thumbnail_600x799.webp','6','Red','25', (SELECT Wardrobe_ID from wardrobe WHERE Wardrobe_ID = 1));


CREATE TABLE `USER` (
  `user_id` int(6) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `second_name` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY(user_id)
);




-- --------------------------------------------------------

-- ----------

COMMIT;
