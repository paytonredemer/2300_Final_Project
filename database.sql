/* Create  table */
CREATE TABLE User (
    ID VARCHAR(80),
    Password VARCHAR(80) NOT NULL,
    Name VARCHAR(80),
    Phone INTEGER,
    PRIMARY KEY(ID)
);

CREATE TABLE Location (
    Address VARCHAR(80),
    Name VARCHAR(80),
    PRIMARY KEY(Address)
);

CREATE TABLE Bin (
    Address VARCHAR(80),
    Bin_no INTEGER NOT NULL,
    Room VARCHAR(80), 
    FOREIGN KEY(Address) REFERENCES Location(Address)
);

CREATE TABLE Charger (
    Charger_ID VARCHAR(80),
    Brand VARCHAR(80),
    Power INTEGER,
    Input VARCHAR(80) NOT NULL,
    Address VARCHAR(80),
    Bin_no INTEGER,
    PRIMARY KEY(Charger_ID)
);

CREATE TABLE Storage (
    Storage_ID VARCHAR(80),
    Brand VARCHAR(80),
    Storage_Size INTEGER CHECK (Storage_Size > 0),
    Connector VARCHAR(80) NOT NULL,
    Medium VARCHAR(80),
    Address VARCHAR(80),
    Bin_no INTEGER,
    PRIMARY KEY(Storage_ID)
);

CREATE TABLE Cable (
    Cable_ID VARCHAR(80),
    Brand VARCHAR(80),
    Length INTEGER CHECK (Length > 0),
    Color VARCHAR(80) NOT NULL,
    Address VARCHAR(80),
    Bin_no INTEGER,
    PRIMARY KEY(Cable_ID)
);

CREATE TABLE Connector (
    Cable_ID INTEGER,
    Connector_no INTEGER NOT NULL,
    End VARCHAR(80),
    FOREIGN KEY(Cable_ID) REFERENCES Cable(Cable_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Output (
    Charger_ID INTEGER,
    Output_no INTEGER NOT NULL,
    Type VARCHAR(80),
    FOREIGN KEY(Charger_ID) REFERENCES Charger(Charger_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Cable_checkout (
    Cable_ID INTEGER,
    User_ID VARCHAR(80),
    Checkout_date INTEGER,
    FOREIGN KEY(Cable_ID) REFERENCES Cable(Cable_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(User_ID) REFERENCES User(ID)
);

CREATE TABLE Storage_checkout (
    Storage_ID INTEGER,
    User_ID VARCHAR(80),
    Checkout_date INTEGER,
    FOREIGN KEY(Storage_ID) REFERENCES Storage(Storage_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(User_ID) REFERENCES User(ID)
);

CREATE TABLE Charger_checkout (
    Charger_ID INTEGER,
    User_ID VARCHAR(80),
    Checkout_date INTEGER,
    FOREIGN KEY(Charger_ID) REFERENCES Charger(Charger_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(User_ID) REFERENCES User(ID)
);

/* Insert data */
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

INSERT INTO Charger_checkout(Charger_ID, User_ID , Checkout_date ) VALUES(6,'payton', 1683155912);
INSERT INTO Charger_checkout(Charger_ID, User_ID , Checkout_date ) VALUES(3,'payton', 1682983112);
INSERT INTO Charger_checkout(Charger_ID, User_ID , Checkout_date ) VALUES(1, 'grader', 1682810312);


INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(1, 1000, 'Toshiba', 'USB-A', 'HDD', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(2, 32, 'Sandisk', 'USB-A', 'Flashdrive', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(3, 32, 'Kingston', 'USB-A', 'Flashdrive', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Storage(Storage_ID, Storage_Size, Brand, Connector, Medium, Address, Bin_no) VALUES(4, 2000, 'Samsung', 'USB-C', 'SSD', 'Apt Dr, Rolla, MO 65409', 1);

INSERT INTO Storage_checkout(Storage_ID, User_ID , Checkout_date ) VALUES(2,'payton', 1683155912);
INSERT INTO Storage_checkout(Storage_ID, User_ID , Checkout_date ) VALUES(4, 'grader', 1682810312);

INSERT INTO Cable(Cable_ID, Brand, Length, Color, Address, Bin_no) VALUES(1, 'Anker', 3, 'Red', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(1, 1, 'USB-A');
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(1, 2, 'USB-C');
INSERT INTO Cable(Cable_ID, Brand, Length, Color, Address, Bin_no) VALUES(2, 'Anker', 6, 'Black', 'Apt Dr, Rolla, MO 65409', 1);
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(2, 1, 'USB-A');
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(2, 2, 'USB-C');
INSERT INTO Cable(Cable_ID, Brand, Length, Color, Address, Bin_no) VALUES(3, 'HP', 3, 'Black', 'Apt Dr, Rolla, MO 65409', 2);
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(3, 1, 'USB-A');
INSERT INTO Connector(Cable_ID, Connector_no, End) VALUES(3, 2, 'USB-B');

INSERT INTO Cable_checkout(Cable_ID, User_ID , Checkout_date ) VALUES(1, 'payton', 1683047912);
INSERT INTO Cable_checkout(Cable_ID, User_ID , Checkout_date ) VALUES(2, 'grader', 1683047912);
