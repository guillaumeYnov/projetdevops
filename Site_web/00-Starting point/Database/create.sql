create table unite(
    idUnite int auto_increment,
    libelle varchar(100) not null,
    primary key(idUnite)
)
ENGINE=MariaDB;;

create table type(
    idType int auto_increment,
    libelle varchar(100) not null,
    primary key(idType)
)ENGINE=MariaDB;

create table Automate(
    numeroAutomate int auto_increment,
    libelle varchar(100) not null,
	idUnit int,
	idTp int,
    primary key(numeroAutomate),
    CONSTRAINT `fk_automate_unite`
    FOREIGN KEY (idUnit) REFERENCES unite (idUnite),
    CONSTRAINT `fk_automate_type`
    FOREIGN KEY (idTp) REFERENCES type (idType)
)ENGINE=MariaDB;

create table Mesure(
	
	idMesure int auto_increment,
	 created_at timestamp default current_timestamp,
	Temperaturecuve float,
	TemperatureExterieur float,
	Poidsdulaitencuve float,
	PoidsDuProduitFini float,
	MesurePH float,
	MesureK int,
	niveauBacterienSalmonelle int,
	niveauBacterienEColi int,
	niveauBacterienListeria int,
	idAutomot int,
	primary key(idMesure),
	CONSTRAINT `fk_automate_Mesure`
    FOREIGN KEY (idAutomot) REFERENCES Automate (numeroAutomate)
	
	
)ENGINE=MariaDB;