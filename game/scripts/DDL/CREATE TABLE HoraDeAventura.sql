begin transaction; 
CREATE TABLE Mundo (
	Nome VARCHAR (20) PRIMARY KEY,
	Mundo_de_Destino CHAR(20) default 'Cubo do prismo'
);
 
CREATE TABLE Regiao (
	Nome VARCHAR(50) PRIMARY KEY,
	Mundo VARCHAR(20),
	FOREIGN KEY (Mundo) REFERENCES Mundo(Nome)
);

CREATE TABLE Local(
	Coordenada int PRIMARY KEY,
	Descricao VARCHAR(1000) NOT NULL,
	Nome VARCHAR(20) NOT NULL,
	Tipo BOOLEAN NOT NULL,
	Regiao VARCHAR(50) NOT NULL,
	FOREIGN KEY (Regiao) REFERENCES Regiao(Nome)
);

CREATE TABLE Personagem(
	IDpersonagem INT PRIMARY KEY,
	AtC BOOLEAN NOT NULL
);

CREATE TABLE PC(
	Personagem INT PRIMARY KEY,
	Nome VARCHAR(20),
	XP INT,
	Vida INT NOT NULL,
	Lvl INT NOT NULL,
	Dinheiro INT NOT NULL,
	Especie VARCHAR(20) NOT NULL,
	Forca INT NOT NULL,
	Defesa INT NOT NULL,
	Local INT NOT null default 0,
	FOREIGN KEY(Personagem) REFERENCES Personagem(IDpersonagem),
	FOREIGN KEY(Local) REFERENCES Local(Coordenada)
);

CREATE TABLE NPC (
	Personagem INT PRIMARY KEY,
	Nome CHAR(20),
	VidaMax INT,
	Conduta BOOLEAN,
	Lvl INT, 
	Especie CHAR(20), 
	Forca INT,
	Defesa INT, 
	FOREIGN KEY (Personagem) REFERENCES Personagem (IDpersonagem)
);

CREATE TABLE Instancia(
	Personagem INT,
	Numero  INT,
	Vida INT NOT NULL,
	Local INT NOT NULL,
	IdPersonagem int, 
	primary key(personagem, numero),
	FOREIGN KEY (Personagem) REFERENCES NPC(Personagem),
	foreign key (local) references local(coordenada),
	foreign key (IdPersonagem) references PC(personagem)
); 

CREATE TABLE Missao (
	Nome CHAR(20) PRIMARY KEY,
	Chefe boolean,
	Descricao VARCHAR(100) NOT NULL,
	Recompensa int NOT null 
	 
);

create table PreRequisitoMissao(
	NomePreRequisito CHAR(20),
	RequisitoMissao CHAR(20),
	foreign key(NomePreRequisito) references Missao(Nome),
	foreign key(RequisitoMissao) references Missao(Nome),
	primary key(NomePreRequisito , RequisitoMissao)	
);

--Tabela d en pra n de missao pra PC
create table fazMissao(
	Personagem int , 
	nomeMissao char(20), 
	status boolean, 
	foreign key(Personagem) references PC(Personagem), 
	foreign key(nomeMissao) references Missao(Nome), 
	primary key(personagem, nomeMissao)
); 

--Tabela de n pra n de missao e instancia 
create table chefe(
	Numero int , 
	nomeMissao char(20),
	Personagem int, 
	Foreign key(Personagem, Numero) references Instancia(Personagem, Numero),
    Foreign key(nomeMissao) references Missao(Nome),
	primary key(Personagem, nomeMissao, Numero)
);

--Tabela de n pra n local pra missao 
CREATE TABLE Contem(
	Local int,
	Missao CHAR(20),
	FOREIGN KEY (Local) REFERENCES Local(coordenada),
	FOREIGN KEY (Missao) REFERENCES Missao(nome),	
	primary key(Local, Missao)	
);

CREATE TABLE Item(
	IDitem INT PRIMARY KEY,
 	AtcItem INT 
);

create table Armamento(
	Item INT primary key, 
	Nome CHAR(20),
	Dano INT,
	Elemento CHAR(20),
	foreign key (Item) references Item(IDItem)
);

create table Armadura(
	Item INT primary key, 
	Nome CHAR(20), 
	Durabilidade INT,
	Defesa INT,  
	foreign key (Item) references Item(IDitem)

);
create table Consumivel(
	Item INT primary key,
	Nome CHAR(20),
	Cura INT,
	Usos INT,
    foreign key (Item) references Item(IDItem)
);

--Tabela de n pra instanciaItem pra NPC 
CREATE TABLE Dropa(
	NPC INT,
	numeroItem INT, 
	IDitem INT, 
	Chance FLOAT NOT NULL,
	primary key(NPC, numeroItem, IDitem),
	FOREIGN KEY (NPC) REFERENCES NPC(Personagem),
	FOREIGN KEY (IDitem, numeroItem) REFERENCES InstanciaItem(IDitem, numeroItem)
);

CREATE TABLE Inventario (
	IDinv INT PRIMARY KEY,
	QTD_de_itens INT,
	Personagem int,
	foreign key(personagem) references Personagem(IDpersonagem)
);

CREATE TABLE Habilidade(
	IDhabilidade INT PRIMARY KEY,
	Nome CHAR(20) NOT NULL,
	Tempo_de_recarga INT NOT NULL,
	Dano INT NOT NULL
	
);
create table PreRequisitoHab(
	IDhabilidade INT not null,
	Requisito int not null,
	foreign key(IDhabilidade) references Habilidade(IDhabilidade),
	foreign key(Requisito) references Habilidade(IDhabilidade),
	primary key(IDhabilidade, Requisito)

);

--Tabela de n pra n personagem pra habilidade 
CREATE TABLE PossuiHab(
	Personagem INT,
	Habilidade INT,
	FOREIGN KEY(Personagem) REFERENCES Personagem (IDpersonagem),
	FOREIGN KEY(Habilidade) REFERENCES Habilidade (IDhabilidade),
	primary key(Personagem, Habilidade)
);

CREATE TABLE InstanciaItem (
    IDitem INT,
    numeroItem INT, 
    durabilidade INT,
    IDinv int , 
    primary key (IDitem, numeroItem),
    FOREIGN KEY (IDitem) REFERENCES Item(IDitem),
    foreign key (IDinv) references Inventario(IDinv)
);

Create Table Loja(
	Nome char(20),
	Tipo varchar(20),
	Dano int,
	Elemento char(1),
	Local int,		
	primary key(Nome, Tipo),
	Foreign key	(Local)	references Local(Coordenada)
);
--Tabela de n pra n item pra instanciaItem 
Create Table PossuiItem(
	IDitem int,
	Loja char(20),
	Tipo varchar(20),
	PrecoItem int Not Null,
	primary key(IDitem, Loja,Tipo),	
	Foreign key	(IDitem) references Item(IDitem),
	Foreign key	(Loja,Tipo)	references Loja(Nome,Tipo)
);

commit;
end transaction; 
	