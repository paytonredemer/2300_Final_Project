INSERT INTO User(ID, Password, Name, Phone) VALUES('payton', 'password', 'Payton Redemer', 8161234612);
INSERT INTO User(ID, Password, Name, Phone) VALUES('grader', 'password', 'San Yueng', 1234567890);


INSERT INTO Location(Address, Name) VALUES('1201 N State St, Rolla, MO 65409', 'Missouri S&T');
INSERT INTO Location(Address, Name) VALUES('Apt Dr, Rolla, MO 65409', 'Apartment');
INSERT INTO Location(Address, Name) VALUES('Home Ave, Hometown, MO 65408', 'Home');


INSERT INTO Bin(Address, Bin_no, Room) VALUES('1201 N State St, Rolla, MO 65409', 1, 'Lab');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('1201 N State St, Rolla, MO 65409', 2, 'Lab');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Apt Dr, Rolla, MO 65409', 1, 'Living Room');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Apt Dr, Rolla, MO 65409', 2, 'Living Room');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Apt Dr, Rolla, MO 65409', 1, 'Closet');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Apt Dr, Rolla, MO 65409', 2, 'Closet');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Home Ave, Hometown, MO 65408', 1, 'Bedroom');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Home Ave, Hometown, MO 65408', 2, 'Bedroom');
INSERT INTO Bin(Address, Bin_no, Room) VALUES('Home Ave, Hometown, MO 65408', 3, 'Bedroom');


INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(1, 5, 'Apple', 'AC','Home Ave, Hometown, MO 65408', 3);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(1, 1, 'USB-A');
INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(2, 5, 'Belkin', 'AC','Home Ave, Hometown, MO 65408', 3);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(2, 1, 'USB-A');
INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(3, 7.5, 'Sony', 'AC','Home Ave, Hometown, MO 65408', 3);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(3, 1, 'USB-A');
INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(4, 7, 'Asus', 'AC','Home Ave, Hometown, MO 65408', 3);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(4, 1, 'USB-A');
INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(5, 15, 'Motorola', 'AC','Apt Dr, Rolla, MO 65409', 2);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(5, 1, 'USB-A');
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(5, 2, 'USB-A');
INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(6, 100, 'Anker', 'AC','Apt Dr, Rolla, MO 65409', 2);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(6, 1, 'USB-C');
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(6, 2, 'USB-C');
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(6, 3, 'USB-A');
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(6, 4, 'USB-A');
INSERT INTO Charger(Charger_ID, Power, Brand, Input, Address, Bin_no) VALUES(7, 10, 'Samsung', 'AC','Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Output(Charger_ID, Output_no, Type) VALUES(7, 1, 'USB-C');


INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(1, 1000, 'Toshiba', 'USB-A', 'HDD', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(2, 32, 'Sandisk', 'USB-A', 'Flashdrive', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(3, 32, 'Kingston', 'USB-A', 'Flashdrive', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(4, 2000, 'Samsung', 'USB-C', 'SSD', 'Apt Dr, Rolla, MO 65409', 1);


INSERT INTO Cable(Cable_ID, Brand, Length, Color, Address, Bin_no) VALUES(1, 'Anker', 3, 'Red', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(1, 1, 'USB-A');
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(1, 2, 'USB-C');
INSERT INTO Cable(Cable_ID, Brand, Length, Color, Address, Bin_no) VALUES(2, 'Anker', 6, 'Black', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(2, 1, 'USB-A');
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(2, 2, 'USB-C');
INSERT INTO Cable(Cable_ID, Brand, Length, Color, Address, Bin_no) VALUES(3, 'HP', 3, 'Black', 'Apt Dr, Rolla, MO 65409', 2);
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(3, 1, 'USB-A');
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(3, 2, 'USB-B');
