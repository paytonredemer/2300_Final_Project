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
/* FOREIGN KEY(Bin_no) REFERENCES Bin(Bin_no) */

CREATE TABLE Charger (
    Charger_ID VARCHAR(80),
    Brand VARCHAR(80),
    Power INTEGER,
    Input VARCHAR(80) NOT NULL,
    Address VARCHAR(80),
    Bin_no INTEGER,
    PRIMARY KEY(Charger_ID),
    FOREIGN KEY(Address) REFERENCES Location(Address)
);

CREATE TABLE Storage (
    Storage_ID VARCHAR(80),
    Brand VARCHAR(80),
    Storage_Size INTEGER CHECK (Storage_Size > 0),
    Connector VARCHAR(80) NOT NULL,
    Medium VARCHAR(80),
    Address VARCHAR(80),
    Bin_no INTEGER,
    PRIMARY KEY(Storage_ID),
    FOREIGN KEY(Address) REFERENCES Location(Address)
);
/* FOREIGN KEY(Bin_no) REFERENCES Bin(Bin_no) */

CREATE TABLE Cable (
    Cable_ID VARCHAR(80),
    Brand VARCHAR(80),
    Length INTEGER CHECK (Length > 0),
    Color VARCHAR(80) NOT NULL,
    Address VARCHAR(80),
    Bin_no INTEGER,
    PRIMARY KEY(Cable_ID),
    FOREIGN KEY(Address) REFERENCES Location(Address)
);

CREATE TABLE Connector (
    Cable_ID INTEGER,
    Connector_no INTEGER NOT NULL, /* checkout constraints like unique */
    End VARCHAR(80),
    FOREIGN KEY(Cable_ID) REFERENCES Cable(Cable_ID)
);

CREATE TABLE Output (
    Charger_ID INTEGER,
    Output_no INTEGER NOT NULL, /* checkout constraints like unique */
    Type VARCHAR(80),
    FOREIGN KEY(Charger_ID) REFERENCES Charger(Charger_ID)
);

/* TODO: Check data type for checkout */

CREATE TABLE Cable_checkout (
    Cable_ID INTEGER,
    User_ID VARCHAR(80),
    Checkout_date INTEGER,
    FOREIGN KEY(Cable_ID) REFERENCES Cable(Cable_ID),
    FOREIGN KEY(User_ID) REFERENCES User(ID)
);

CREATE TABLE Storage_checkout (
    Storage_ID INTEGER,
    User_ID VARCHAR(80),
    Checkout_date INTEGER,
    FOREIGN KEY(Storage_ID) REFERENCES Storage(Storage_ID),
    FOREIGN KEY(User_ID) REFERENCES User(ID)
);

CREATE TABLE Charger_checkout (
    Charger_ID INTEGER,
    User_ID VARCHAR(80),
    Checkout_date INTEGER,
    FOREIGN KEY(Charger_ID) REFERENCES Charger(Charger_ID),
    FOREIGN KEY(User_ID) REFERENCES User(ID)
);
