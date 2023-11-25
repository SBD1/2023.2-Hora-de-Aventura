insert into mundo values('Mundo de O','Cubo do prismo');

insert into regiao values('Reino Doce', 'Mundo de O');

insert into local values('1','Casa onde habita o canelinha' ,'Casa do canelinha', false, 'Reino Doce');
 
insert into personagem values('1',false);

insert into npc values('1','Litch',1000,false, 100,'Primordial', 1000, 1000);

insert into instancia values(1,1 ,1000 , 0001);

insert into instancia values(3,1 ,30 , 0001,2);

insert into missao values('Salvar princesa ',true , 'Salvar princesa', 100);

insert into missao values('matar esqueletos ',false , 'Salvar princesa', 100);

insert into prerequisitomissao values('matar esqueletos', 'Salvar princesa');

insert into missao values('ganhar espada',false , 'forjar uma espada ', 100);

insert into prerequisitomissao values('ganhar espada', 'matar esqueletos');

insert into chefe values (1,'Salvar princesa ',1);

insert into personagem  values('2', true);

insert into pc values('2', 'Finn', 50, 40, 40, 0, 'humano', 40, 20, 1);

insert into fazmissao values(2, 'Salvar princesa', false);  

insert into contem values(1,'Salvar princesa', 'Incompleto' );

insert into local values('0002','Casa onde habita Finn' ,'Casa na árvore', false, 'Reino Doce');

insert into habilidade values(1, 'Elasticidade', 0, 100);

insert into habilidade values(2, 'Elasticidade lvl 2', 0, 150);

insert into possuihab values('2',1);

insert into prerequisitohab values(2,1);

--- 1 = armamento , 2 = consumivel, 3 = armadura 

insert into item values('001',1);

insert into item values('002',2 );

insert into item values('003',3 );

insert into armamento values('001', 'Espada', 20, 9 ); 

insert into consumivel values('002', 'Poção de vida', 30, 1 );

insert into armadura values('003', 'Armadura de ferro', 70, 80);

insert into inventario values(1,1,2);

insert  into instanciaitem values(1, 1, 100, 1); 

insert into dropa values(1,1,0.22);

insert into loja values('Loja de Arma', 'Arma','Espadas', 2 );

insert into possuiitem values(1,'Loja de Arma', 'Espadas', 2);

insert into npc values(3,'Jake', 80, false, 30, 'cachorro', 30, 50);

insert into personagem values(3, false);

