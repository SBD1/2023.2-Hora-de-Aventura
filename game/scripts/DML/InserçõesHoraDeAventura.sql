begin transaction;

insert into mundo values('Cubo do Prismo','Cubo do prismo');

insert into mundo values('Mundo de O','Cubo do prismo');

insert into mundo values('Noitosfera','Mundo de O');

insert into mundo values('Espaço','Mundo de O');



insert into regiao values('Reino Doce', 'Mundo de O'); 

insert into regiao values('Planice', 'Mundo de O');

insert into regiao values('WaterWorld', 'Mundo de O');

insert into regiao values('Selva', 'Mundo de O');

insert into regiao values('Reino Gelado', 'Mundo de O');

insert into regiao values('Deserto', 'Mundo de O');

insert into regiao values('Pantano', 'Mundo de O');

insert into regiao values('Reino de Fogo', 'Mundo de O');

insert into regiao values('Céu', 'Mundo de O');

insert into regiao values('Reino Caroço', 'Mundo de O');

insert into regiao values('Terra do Litch', 'Mundo de O');

insert into regiao values('Exosfera', 'Espaço');

insert into regiao values('Inferno', 'Noitosfera');





insert into local values('0','Foi aqui que tudo começou!' ,'Início', false, 'Reino Doce');

insert into local values('1','Estes portões guardam o castelo da princesa Jujuba' ,'Portão Castelo Doce', false, 'Reino Doce');

insert into local values('2','Casa onde habita o canelinha' ,'Casa do canelinha', false, 'Reino Doce');

insert into local values('3','Aqui você vai encontrar armas importantes pra começar sua jornada' ,'Loja do Doan', false, 'Reino Doce');

insert into local values('4','As gramas brancas de maria mole aos poucos dão lugar a grama de verdade' ,'Planices Doces', false, 'Reino Doce');

insert into local values('5','Aqui tem grama até onde a vista alcança' ,'Planices Verdes', true, 'Planice');

insert into local values('6','Uma luz mística emana no fundo do laguinho' ,'Laguinho', true, 'Planice');

insert into local values('7','Luzes coloridas passam por você, aqui parece que você se encontra entre dois mundos' ,'Portal do Laguinho', false, 'Planice');

insert into local values('8','Eca é esgoto!' ,'Esgoto', true, 'WaterWorld');

insert into local values('9','Susana forte, uma moça muito grande e forte mora aqui. Sua casa é muito fofa' ,'Casa da Susana Forte', false, 'WaterWorld');

insert into local values('10','Aqui vive um povo peixe que parece humano' ,'Cidade subterranea', false, 'WaterWorld');

insert into local values('16','Jardins da princesa Jujuba' ,'Jardins doce', false, 'Reino Doce');

insert into local values('19','Aqui você vai encontrar armas importantes pra começar sua jornada' ,'Loja do Arthur', false, 'Planice');

insert into local values('20','Aqui mora o Jake e seu amigo Finn' ,'Casa na árvore', false, 'Planice');

insert into local values('23','Aqui morava o toucinho do mar, está abandonado' ,'Casa do Toucinho', true, 'WaterWorld');

insert into local values('24','Quase não dá pra ver algo aqui. Como estamos respirando?' ,'Profundezas', true, 'WaterWorld');

insert into local values('25','A água aqui é muito quente e é um local muito grande' ,'Toca do monstro', true, 'WaterWorld');

insert into local values('26','Um vulcão se encontra em um buraco em baixo da agua' ,'Vulcão submerso', true, 'WaterWorld');

insert into local values('27','Uma praia de águas mornas. Que maravilha' ,'Prainha', false, 'Reino de Fogo');

insert into local values('28','O malvado rei de fogo prende sua filha aqui' ,'Sela da princesa', false, 'Reino de Fogo');

insert into local values('29','Dói pisar aqui' ,'Areia quente', false, 'Reino de Fogo');

insert into local values('30','Aqui a princesa jujuba dorme' ,'Quarto da Jujuba', false, 'Reino Doce');

insert into local values('31','Aqui é o lobby' ,'Salão castelo doce', false, 'Reino Doce');

insert into local values('33','Um parquinho onde o BMO brinca' ,'Parquinho', true, 'Planice');

insert into local values('34','Tem algumas árvores antigas aqui' ,'Arvoreado', true, 'Planice');

insert into local values('35','Tem muitas árvores antigas aqui' ,'Bosque', true, 'Planice');

insert into local values('36','Tem velharias e cheiro de poeira aqui, Nada de muito útil' ,'Depósito velho', false, 'Planice');

insert into local values('43','O mais puro piso de obsidiana. O rei de fogo mora aqui' ,'Sala do trono', true, 'Reino de Fogo');

insert into local values('45','Muitos bandidos são presos aqui' ,'calabouço', true, 'Reino Doce');

insert into local values('46','Aqui a princesa fabrica seu povo. Literalmente' ,'Laboratório', false, 'Reino Doce');

insert into local values('49','Aqui a mata é muito densa e traiçoeira' ,'Inicio da Selva', true, 'Selva');

insert into local values('50','A floresta aqui uiva como um lobo' ,'Floresta uivante', true, 'Selva');

insert into local values('51','Aqui começa a neve do reino gelado' ,'Entrada do gelo', true, 'Reino Gelado');

insert into local values('52','Aqui é muito frio' ,'Salão do rei gelado', true, 'Reino Gelado');

insert into local values('53','Rei gelado dorme aqui' ,'Quarto do rei gelado', false, 'Reino Gelado');

insert into local values('54','aqui tem muitos brinquedos' ,'Quarto do gunter', false, 'Reino Gelado');

insert into local values('55','aqui o rei gelado tortura as princesas com sua voz' ,'Karâoke', false, 'Reino Gelado');

insert into local values('57','aqui tem flores que parecem velas' ,'Jardim de velas', true, 'Reino de Fogo');

insert into local values('58','Os portões vermelhos de calor aquecem até sua alma' ,'Portões flamejantes', true, 'Reino de Fogo');

insert into local values('59','aqui tem flores que parecem luminárias' ,'Jardim de lumos', true, 'Reino de Fogo');

insert into local values('63','aqui mora a belíssima maga caçadora' ,'porta da maga', false, 'Selva');

insert into local values('64','aqui o cheiro de carniça das vítimas é tanto que é tonteante' ,'floresta dos perigos', true, 'Selva');

insert into local values('65','A floresta aqui uiva ainda mais' ,'floresta UIVADORA', true, 'Selva');

insert into local values('66','Tem muita lama aqui, é até difícil andar' ,'floresta pantanosa', true, 'Pantano');

insert into local values('68','Muitas princesas já passaram por aqui' ,'Calabouço gelado', false, 'Reino Gelado');

insert into local values('69','Muitos cadernos preenchem as prateleiras, repletos de histórias de Fiona e Cake, escritas pelo rei gelado' ,'Biblioteca', false, 'Reino Gelado');

insert into local values('73','Ao invés de copas de folhas, as daqui tem cópas de fogo e metal derretido' ,'Floresta Forno', true, 'Reino de Fogo');

insert into local values('76','Aqui a maga da floresta ora para seus deuses' ,'totem de oração', false, 'Selva');

insert into local values('77','Aqui a maga guarda suas armas. Não roube ela ein' ,'Arsenal da maga', false, 'Selva');

insert into local values('78','Aqui a maga dorme' ,'Quarto da Maga', false, 'Selva');

insert into local values('80','Tem olinhos nesse poço pedindo moedas em troca de itens' ,'Poço velho', false, 'Selva');

insert into local values('84','A temperatura começa a se elevar na saída do reino gelado' ,'Saída reino gelado', true, 'Reino Gelado');

insert into local values('87','A temperatura arde ' ,'Campos Flamejantes', true, 'Reino de Fogo');

insert into local values('88','A temperatura arde ' ,'Floresta de Fogo', true, 'Reino de Fogo');

insert into local values('89','A temperatura arde MUITO ' ,'Bosque de Fogo', true, 'Reino de Fogo');

insert into local values('90','A rainha vampira Marceline vive aqui ' ,'Casa da Marceline', false, 'Pantano');

insert into local values('94','Festas Iradas acontecem aqui a noite ' ,'Mata das festas', false, 'Pantano');

insert into local values('95','a floresta chama seu nome, ao olhar pra trás você vê verdades ocultas que te atormentam. Ao olhar para frente você já se esqueceu ' ,'Floresta Macabra', true, 'Pantano');

insert into local values('96','Um cometa Catalisador já caiu aqui séculos atrás' ,'Grande cratéra', true, 'Deserto');

insert into local values('97','Um casal de idosos vive nessas terras inospistas com seu cão' ,'Lugar nenhum', false, 'Deserto');

insert into local values('98','Já houve muitas criaturas aqui. Hoje apenas baratas e poeira' ,'Prédio em ruínas', true, 'Deserto');

insert into local values('99', 'Monstros habitam estas terras' ,'Prédio em ruínas', true, 'Deserto');

insert into local values('100', 'Destroços de uma velha ponte' ,'ponte velha', true, 'Deserto');

insert into local values('101', 'O chão começa a ferver, revelando uma terra de chamas' ,'pedreira ígnea', true, 'Reino de Fogo');

insert into local values('102', 'Aqui do alto dá pra ver muito longe mesmo' ,'Monte do fogo', true, 'Reino de Fogo');

insert into local values('103', 'aqui queima como o inferno' ,'campos ardentes', true, 'Reino de Fogo');

insert into local values('104', 'um lago de magma borbulha aqui' ,'lago de magma', true, 'Reino de Fogo');

insert into local values('105', 'Quadra de basquete da marceline' ,'Quadra de basquete', false, 'Pantano');

insert into local values('106', 'não dá pra ver os próprios pés na água' ,'Águas turvas', true, 'Pantano');

insert into local values('107', 'Caverna' ,'Caverna3', true, 'Pantano');

insert into local values('108', 'Caverna' ,'Caverna2', true, 'Pantano');

insert into local values('109', 'Caverna' ,'Caverna', true, 'Pantano');

insert into local values('110', 'Uma velharia de tempos passados' ,'Nave abandonada', true, 'Deserto');

insert into local values('112', 'mal dá pra ver um palmo a sua frente' ,'Caverna Mais escura', true, 'Deserto');

insert into local values('114', 'Aqui tem tecnologias do passado que estão anos a frente da nossa' ,'Ferro Velho', true, 'Deserto');

insert into local values('115', 'Aqui tem tecnologias do passado que estão anos a frente da nossa. esqueletos de criaturas mortas cobrem o chão.' ,'Laboratorio velho', true, 'Deserto');

insert into local values('117', 'Um adorável ser de fogo vive aqui' ,'Casa do Foguin', false, 'Reino de Fogo');

insert into local values('118', 'Um vulcão frio está aqui, ele pode te mandar pro céu' ,'Vulcão Frio', false, 'Reino de Fogo');

insert into local values('119', 'Henrique montou aqui sua lojinha pra te ajudar' ,'Lojinha fervente', false, 'Reino de Fogo');

insert into local values('125', 'Esqueletos macabros andam por aqui' ,'Cemitério', true, 'Terra do Litch');

insert into local values('127', 'Mutantes da guerra dos cogumelos habitam aqui' ,'Lar dos mutantes', true, 'Deserto');

insert into local values('128', 'Uma vez princesa jujuba, finn e jake se meteram numa confusão com os mutantes nessa nave' ,'Ruinas de uma nave', true, 'Deserto');

insert into local values('130', 'Uma imagem macabra de um monstro cabeçudo' ,'Totem da Noitosfera', true, 'Deserto');

insert into local values('133', 'O vulcão frio tem seu topo aqui' ,'vulcão propulsor', false, 'Reino de Fogo');

insert into local values('138', 'Oba, um báu' ,'Báu', true, 'Terra do Litch');

insert into local values('139', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala1', true, 'Terra do Litch');

insert into local values('140', 'Entrada da dungeon do litch, se eu fosse você,tomaria cuidado com ele que é final boss' ,'Entrada da dungeon', true, 'Terra do Litch');

insert into local values('145', 'Uma imagem macabra de um monstro cabeçudo de trouxe aqui' ,'Tunel misterioso', true, 'Deserto');

insert into local values('147', 'Uma casa literalmente fofinha. O homem nuvem vive aqui com a mulher nuvem' ,'Casa nuvem', false, 'Céu');

insert into local values('148', 'Aqui é um local muito bonito e alto. Veio pelo vulcão?' ,'Porta do Céu', false, 'Céu');

insert into local values('149', 'Lugar de criança' ,'Parque Céu', false, 'Céu');

insert into local values('152', 'Um dracolich malvado vive aqui' ,'Câmara do Dracolich', true, 'Terra do Litch');

insert into local values('155', 'Um corredor comum' ,'corredor 1', true, 'Terra do Litch');

insert into local values('158', 'Um rio de lava macabro' ,'Rio de lava', true, 'Inferno');

insert into local values('159', 'Aqui é onde os demônios pegam seu número pra fila' ,'Central demônio', true, 'Inferno');

insert into local values('160', 'Aqui é a entrada da noitosfera, a dimensão do inferno' ,'Entrada', true, 'Inferno');

insert into local values('162', 'loja bacaninha' ,'Loja do Mr.Mcloud', false, 'Céu');

insert into local values('163', 'núvens que parecem algodão e são tão mácias quanto plumas promovem um campo a perder de vista' ,'Campos fofos', false, 'Céu');

insert into local values('167', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala5', true, 'Terra do Litch');

insert into local values('168', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala4', true, 'Terra do Litch');

insert into local values('169', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala3', true, 'Terra do Litch');

insert into local values('170', 'Um corredor comum' ,'corredor 2', true, 'Terra do Litch');

insert into local values('171', 'Uma Lojinha muito especial e alegre, com tudo que você precisa' ,'Lojinha do Davi', false, 'Terra do Litch');

insert into local values('173', 'Uma poça de lava' ,'Lava1', true, 'Inferno');

insert into local values('174', 'Uma Fila de demônios, muito cuidado' ,'Fila do mal', true, 'Inferno');

insert into local values('175', 'Um rio de lava macabro' ,'Rio de lava2', true, 'Inferno');

insert into local values('178', 'Até o rei gelado é bem vindo aqui' ,'Salão de festas', false, 'Céu');

insert into local values('185', 'Um corredor comum' ,'corredor 3', true, 'Terra do Litch');

insert into local values('189', 'Uma Fila de demônios, muito cuidado eles estão muito furiosos por estarem quase sendo atendidos' ,'Fila do mal2', true, 'Inferno');

insert into local values('193', 'Uma piscina geladinha' ,'Piscina do céu', false, 'Céu');

insert into local values('195', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala8', true, 'Terra do Litch');

insert into local values('196', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala7', true, 'Terra do Litch');

insert into local values('197', 'Os esqueletos mais fortes do reino descansam aqui' ,'Cemitério esqueleto', true, 'Terra do Litch');

insert into local values('198', 'Uma tumba de um ser macabro do passado' ,'Tumba', true, 'Terra do Litch');

insert into local values('199', 'Um corredor comum' ,'corredor 5', true, 'Terra do Litch');

insert into local values('200', 'Um corredor comum' ,'corredor 4', true, 'Terra do Litch');

insert into local values('201', 'Uma sala da dungeon, as vezes tem monstros' ,'Sala6', true, 'Terra do Litch');

insert into local values('202', 'Antigo ferreiro esqueleto. É hora de melhorar as armas' ,'Ferreiro', false, 'Terra do Litch');

insert into local values('204', 'Uma Fila de demônios, muito cuidado eles estão muito, MUITO MESMO furiosos por estarem quase sendo atendidos' ,'Fila do mal3', true, 'Inferno');

insert into local values('208', 'Uma cachoeira mágica geladinha' ,'Piscina do céu', false, 'Céu');

insert into local values('212', 'Um portal bizarro' ,'portal quântico', false, 'Terra do Litch');

insert into local values('218', 'Um Jardim de horrores cósmicos que se devoram e se multiplicam simultâneamente' ,'Jardim maligno', true, 'Inferno');

insert into local values('219', 'Um portão que é o fim da fila' ,'Portão da corte', true, 'Inferno');

insert into local values('220', 'Um Jardim de horrores cósmicos que se devoram e se multiplicam simultâneamente' ,'Jardim maligno2', true, 'Inferno');

insert into local values('222', 'Ilha feita de um caroço gigante' ,'Jardim Caroço', true, 'Reino Caroço');

insert into local values('223', 'Planice feita de um caroço gigante' ,'planice Caroço', true, 'Reino Caroço');

insert into local values('224', 'Restaurante feito em um caroço gigante' ,'Restaurante', false, 'Reino Caroço');


insert into local values('226', 'Espaço Infindável, cuidado você está quase saindo da órbita' ,'Espaço Sideral 2', true, 'Exosfera');

insert into local values('227', 'Espaço Infindável' ,'Espaço Sideral', true, 'Exosfera');

insert into local values('228', 'Um rocheado vagando tranquilo no espaço Infindável, tem uma base espacial nele' ,'Rocheado', true, 'Exosfera');

insert into local values('229', 'Porto espacial para descanso. Quem poderia ter construido ele aqui? Tem uma nave atracada' ,'Porto espacial', false, 'Exosfera');

insert into local values('230', 'Uma nave amarela feita pelo Lemongrab? Achei que ele estivesse morto, como pode ter feito uma nave?' ,'Cyberlimonave', true, 'Exosfera');

insert into local values('234', 'Salão principal do rei da Noitosfera. O devorador de batatinhas e pai de Marceline a rainha vampira' ,'Salão central', true, 'Inferno');

insert into local values('237', 'Uma balada bem parada' ,'Balada Caroço', true, 'Reino Caroço');

insert into local values('238', 'Espaço Infindável' ,'Vazio Infindável', false, 'Reino Caroço');

insert into local values('241', 'Espaço Infindável' ,'Espaço Sideral3', true, 'Exosfera');
insert into local values('242', 'Pedrinhas voadoras' ,'Aerolitos', true, 'Exosfera');

insert into local values('243', 'Cadáver de um gigante celeste, totalmente congelado. Deve ser daqui que vem as crias do espaço' ,'Cadáver celeste', true, 'Exosfera');

insert into local values('252', 'Pequena ilha caroço' ,'Ilihnha', false, 'Reino Caroço');

insert into local values('253', 'Centro da cidade' ,'Centro', false, 'Reino Caroço');

insert into local values('256', 'O restaurante entre esse o fim do universo' ,'Restaurante the end', false, 'Exosfera');

insert into local values('257', 'O planetoide do fim ' ,'Planetoide', true, 'Exosfera');

insert into local values('261', 'Sela onde o Litch aprisionou a Princesa Jujuba!!' ,'Sela Jujuba', false, 'Exosfera');

insert into local values('262', 'O Litch soltou uma aura aterradora nesse lugar' ,'Câmara do litch', true, 'Exosfera');

insert into local values('263', 'O lugar onde as sentinelas são guardadas' ,'Sala de robôs', true, 'Exosfera');

insert into local values('264', 'O lugar mais macabro, dá pra sentir a aura do litch' ,'O corredor escuro', true, 'Exosfera');

insert into local values('268', 'O lugar onde a realeza caroço vive' ,'Castelo Caroço', false, 'Reino Caroço');

insert into local values('270', 'Aqui habita o Elefante de Guerra pré histórico' ,'Câmara do elefante', false, 'Exosfera');

insert into local values('272', 'Porto espacial para cidadela' ,'Porto espacial', true, 'Exosfera');

insert into local values('279', ' Dá pra sentir a aura do litch' ,'O corredor escuro', true, 'Exosfera');

insert into local values('280', ' Se for enfrentar o boss, é sua ultima chance de comprar itens' ,'A ultima loja', false, 'Exosfera');

insert into local values('285', ' Um peculiar cofre. Eba!' ,'Sala do Cofre', true, 'Exosfera');

insert into local values('286', ' Um corredor futurista mas desgastado' ,'corredor', true, 'Exosfera');

insert into local values('287', ' A entrada da temida cidadela, agora abandonda após um infeliz incidente' ,'Entrada da cidadela', true, 'Exosfera');

insert into local values('288', ' Um corredor futurista mas desgastado' ,'corredor2', true, 'Exosfera');

insert into local values('289', ' Catracas velhas, alguns esqueletos estão encostados nelas, totalmente mortos.' ,'Catracas', true, 'Exosfera');

insert into local values('290', ' Um corredor futurista mas desgastado' ,'corredor3', true, 'Exosfera');

insert into local values('291', ' Um corredor futurista mas desgastado e com partes faltando, dando vista pro espaço' ,'corredor4', true, 'Exosfera');

insert into local values('292', ' Um corredor futurista mas desgastado' ,'corredor5', true, 'Exosfera');

insert into local values('293', ' Um corredor futurista com um monte de corpos, no centro um amalgama de carne que forma um olho que pisca freneticamente. Possivelmente feito pelo Litch' ,'corredor de Carne', true, 'Exosfera');

insert into local values('294', ' Uma quina, para a única virada que sobrou da destruida e mal acabada cidadela' ,'virada de corredor', true, 'Exosfera');


insert into personagem values('1',false);

insert into npc values('1','Litch',1000,false, 100,'Primordial', 1000, 1000);

insert into instancia values(1,1 ,1000 ,262);

insert into personagem values('2',false);
insert into npc values(2,'Jake', 80, false, 30, 'cachorro', 30, 50);

insert into instancia values(2,2 ,80 ,20);

insert into personagem values('3',false);
insert into npc values(3,'Finn', 70, false, 15, 'humano', 30, 50);

insert into instancia values(3,3 ,70 ,20);

insert into personagem values('4',false);
insert into npc values(4,'Jujuba', 20, false, 5, 'doce', 20, 20);

insert into instancia values(4,4 ,20 ,261);

insert into personagem values('5',false);
insert into npc values(5,'Mordomo Menta', 60, false, 90, 'doce', 80, 20);

insert into instancia values(5,5 ,60 ,30);

insert into personagem values('6',false);
insert into npc values(6,'Canelinha', 10, false, 1, 'doce', 2, 10);

insert into instancia values(5,6 ,10 ,2);

insert into personagem values('7',false);
insert into npc values(7,'Rato Doce', 20, false, 1, 'doce', 5, 15);

insert into instancia values(7,7 ,20 ,46);

insert into personagem values('8',false);
insert into npc values(8,'Aberração dagua', 30, true, 3, 'besta', 10, 15);

insert into instancia values(8,8 ,30 ,8);
insert into instancia values(8,9 ,40 ,24);
insert into instancia values(8,10 ,70 ,25);

insert into personagem values('9',false);
insert into npc values(9,'Susana Forte', 50, true, 10, 'besta', 60, 80);

insert into instancia values(9,11 ,50 ,9);

insert into personagem values('10',false);
insert into npc values(10,'Prinscesa de Fogo', 70, false, 10, 'fogo', 40, 50);

insert into instancia values(10,12 ,70 ,28);

insert into personagem values('11',false);
insert into npc values(11,'Rei de Fogo', 200, true, 30, 'fogo', 90, 50);

insert into instancia values(11,13 ,200 ,43);

insert into personagem values('12',false);
insert into npc values(12,'Soldado Ardente', 20, true, 5, 'fogo', 11, 9);

insert into instancia values(12,14 ,20 ,73);
insert into instancia values(12,15 ,20 ,87);
insert into instancia values(12,16 ,20 ,88);
insert into instancia values(12,17 ,20 ,89);

insert into personagem values('13',false);
insert into npc values(13,'Cria de Magma', 10, true, 2, 'fogo', 9, 9);

insert into instancia values(13,18 ,10 ,102);
insert into instancia values(13,19 ,10 ,103);
insert into instancia values(13,20 ,10 ,104);

insert into personagem values('14',false);
insert into npc values(14,'Cria vampírica', 10, true, 2, 'Vampiro', 9, 9);

insert into instancia values(14,21 ,10 ,66);
insert into instancia values(14,22 ,10 ,94);
insert into instancia values(14,23 ,10 ,95);

insert into personagem values('15',false);
insert into npc values(15,'Morcego', 5, true, 1, 'Besta', 5, 5);

insert into instancia values(15,24 ,5 ,107);
insert into instancia values(15,25 ,5 ,108);
insert into instancia values(15,26 ,5 ,109);
insert into instancia values(15,33 ,5 ,112);

insert into personagem values('16',false);
insert into npc values(16,'Urso malvado', 17, true, 55, 'Besta', 30, 60);

insert into instancia values(16,27 ,55 ,64);


insert into personagem values('17',false);
insert into npc values(17,'Lobo Raivoso', 7, true, 16, 'Besta', 10, 20);

insert into instancia values(17,28 ,16 ,64);
insert into instancia values(17,29 ,16 ,65);
insert into instancia values(17,30 ,16 ,49);
insert into instancia values(17,31 ,16 ,50);

insert into personagem values('18',false);
insert into npc values(18,'Maga da Floresta', 700, false,45, 'Primordial', 60, 50);

insert into instancia values(18,32 ,700 ,78);

insert into personagem values('19',false);
insert into npc values(19,'Mutante', 100, true,30, 'Aberração', 60, 50);

insert into instancia values(19,34 ,100 ,96);
insert into instancia values(19,35 ,100 ,98);
insert into instancia values(19,36 ,100 ,99);
insert into instancia values(19,37 ,100 ,100);
insert into instancia values(19,38 ,100 ,127);
insert into instancia values(19,39 ,100 ,128);

insert into personagem values('20',false);
insert into npc values(20,'Marceline', 300, false,30, 'Vampiro', 60, 90);

insert into instancia values(20,40 ,300 ,90);

insert into personagem values('21',false);
insert into npc values(21,'Rei Gelado', 300, false,34, 'Humano', 70, 20);

insert into instancia values(21,41 ,300 ,53);

insert into personagem values('22',false);
insert into npc values(22,'Muriel', 40, false,3, 'Humano', 10, 20);

insert into instancia values(22,42 ,40 ,97);

insert into personagem values('23',false);
insert into npc values(23,'Coragem', 40, false,5, 'cachorro', 10, 30);

insert into instancia values(23,43 ,40 ,97);

insert into personagem values('24',false);
insert into npc values(24,'Eustácio', 20, false,3, 'Humano', 10, 20);

insert into instancia values(24,44 ,20 ,97);

insert into personagem values('25',false);
insert into npc values(25,'Gunter', 600, false,999, 'Pinguim', 700, 200);

insert into instancia values(25,45 ,600 ,54);

insert into personagem values('26',false);
insert into npc values(26,'Esqueleto', 100, true,48, 'Besta', 40, 20);

insert into instancia values(26,46 ,100 ,125);
insert into instancia values(26,47 ,100 ,139);
insert into instancia values(26,48 ,100 ,140);
insert into instancia values(26,49 ,100 ,155);
insert into instancia values(26,50 ,100 ,170);
insert into instancia values(26,51 ,100 ,168);
insert into instancia values(26,52 ,100 ,169);
insert into instancia values(26,53 ,100 ,167);
insert into instancia values(26,54 ,100 ,185);
insert into instancia values(26,55 ,100 ,195);
insert into instancia values(26,56 ,100 ,196);
insert into instancia values(26,57 ,100 ,199);
insert into instancia values(26,58 ,100 ,200);
insert into instancia values(26,59 ,100 ,201);

insert into personagem values('27',false);
insert into npc values(27,'Planta do mal', 10, true,8, 'Planta', 20, 9);

insert into instancia values(27,60 ,10 ,218);
insert into instancia values(27,61 ,10 ,220);

insert into personagem values('28',false);
insert into npc values(28,'Demônio', 60, true,32, 'Infernal', 60, 20);

insert into instancia values(28,62 ,60 ,159);
insert into instancia values(28,63 ,60 ,160);
insert into instancia values(28,64 ,60 ,174);
insert into instancia values(28,65 ,60 ,189);
insert into instancia values(28,66 ,60 ,204);

insert into personagem values('29',false);
insert into npc values(29,'Dracolich', 700, true,32, 'Primordial', 50, 200);

insert into instancia values(29,67 ,700 ,152);

insert into personagem values('30',false);
insert into npc values(30,'Hunson Abadeer', 700, true,32, 'Primordial', 106, 200);

insert into instancia values(30,68 ,700 ,234);

insert into personagem values('31',false);
insert into npc values(31,'Homem Nuvem', 2, false,1, 'nuvem', 1, 1);

insert into instancia values(31,69 ,2 ,147);
insert into instancia values(31,70 ,2 ,163);

insert into personagem values('32',false);
insert into npc values(32,'Criança Nuvem', 1, false,1, 'nuvem', 1, 1);

insert into instancia values(32,71 ,1 ,149);

insert into personagem values('33',false);
insert into npc values(33,'Esqueleto mortal', 190, true,80, 'Esqueleto', 100, 300);

insert into instancia values(33,72 ,190 ,197);

insert into personagem values('34',false);
insert into npc values(34,'Faraó', 590, true,99, 'Esqueleto', 500, 500);

insert into instancia values(34,73 ,590 ,198);

insert into personagem values('35',false);
insert into npc values(35,'Cyberlemongrab', 400, true,99, 'doce', 600, 500);

insert into instancia values(35,74 ,400 ,230);

insert into personagem values('36',false);
insert into npc values(36,'Vermes Espaciais', 100, true,99, 'verme', 10, 300);

insert into instancia values(36,75 ,100 ,226);
insert into instancia values(36,76 ,100 ,227);
insert into instancia values(36,77 ,100 ,228);
insert into instancia values(36,78 ,100 ,241);
insert into instancia values(36,79 ,100 ,242);
insert into instancia values(36,80 ,100 ,243);

insert into personagem values('37',false);
insert into npc values(37,'Robô mal', 200, true,99, 'robô', 100, 300);

insert into instancia values(37,81 ,200 ,263);



--Missão

INSERT INTO Missao VALUES ('ganhar arma', false, 'Forje uma espada com o mordo menta', 100);
INSERT INTO Missao VALUES ('AmigoStoyAqui', false, 'ponha alguém na party', 50);
INSERT INTO Missao VALUES ('Mate um monstro', false, 'Mate um bicho no mapa', 150);
INSERT INTO Missao VALUES ('Festa no céu', false, 'chegue no céu', 150);
INSERT INTO Missao VALUES ('Reino de fogo', false, 'Busque o reino de fogo', 200);
INSERT INTO Missao Values ('Salve a dama', false, 'Salve a Princesa de fogo', 100);
INSERT INTO Missao VALUES ('Mate o rei de fogo', true, 'Confronto com o Chefe', 500);
INSERT INTO Missao VALUES ('ficando forte', false, 'Chegue no Deserto', 100);
INSERT INTO Missao VALUES ('Rainha Vampira', false, 'Encontre a Marceline',100);
INSERT INTO Missao VALUES ('Hora de Aventura', false, 'Coloque Finn na sua party', 60);
INSERT INTO Missao VALUES ('inferno é Fogo', false, 'siga pra noitosfera',200);
INSERT INTO Missao VALUES ('Caçar demônios', false, 'Mate três criaturas no inferno', 200);
INSERT INTO Missao VALUES ('Embate a noitosfera', true, 'Mate o Hunson Abadeer', 800);
INSERT INTO Missao VALUES ('Rumo ao Litch', false, 'Chegue ao ferreiro da dungeon', 50);
INSERT INTO Missao VALUES ('Maior, mais forte', false, 'Use o ferreiro',100);
INSERT INTO Missao VALUES ('conquista do espaço', false, 'Encontre o espaço sideral', 200);
INSERT INTO Missao VALUES ('Duro de matar', true, 'mate o lemongrab. Pra sempre', 900);
INSERT INTO Missao VALUES ('Morte ao bruxo', true, 'mate o Litch', 1000);
INSERT INTO Missao VALUES ('Salve Princesa', false, 'Ache a Princesa Jujuba', 999);


INSERT INTO PreRequisitoMissao VALUES ('ganhar arma', 'Mate um monstro');
INSERT INTO PreRequisitoMissao VALUES ('ganhar arma', 'AmigoStoyAqui');
INSERT INTO PreRequisitoMissao VALUES ('Mate um monstro', 'Reino de fogo');
INSERT INTO PreRequisitoMissao VALUES ('Mate um monstro', 'Festa no céu');
INSERT INTO PreRequisitoMissao VALUES ('Reino de fogo', 'Mate o rei de fogo');
INSERT INTO PreRequisitoMissao VALUES ('Reino de fogo', 'Salve a dama');
INSERT INTO PreRequisitoMissao VALUES ('ganhar arma', 'ficando forte');
INSERT INTO PreRequisitoMissao VALUES ('Mate um monstro', 'Rainha Vampira');
INSERT INTO PreRequisitoMissao VALUES ('AmigoStoyAqui', 'Hora de Aventura');
INSERT INTO PreRequisitoMissao VALUES ('Mate o rei de fogo', 'inferno é Fogo');
INSERT INTO PreRequisitoMissao VALUES ('inferno é Fogo', 'Caçar demônios');
INSERT INTO PreRequisitoMissao VALUES ('Caçar demônios', 'Embate a noitosfera');
INSERT INTO PreRequisitoMissao VALUES ('Embate a noitosfera', 'Rumo ao Litch');
INSERT INTO PreRequisitoMissao VALUES ('Rumo ao Litch', 'Maior, mais forte');
INSERT INTO PreRequisitoMissao VALUES ('Rumo ao Litch', 'conquista do espaço');
INSERT INTO PreRequisitoMissao VALUES ('conquista do espaço', 'Duro de matar');
INSERT INTO PreRequisitoMissao VALUES ('Duro de matar', 'Morte ao bruxo');
INSERT INTO PreRequisitoMissao VALUES ('Morte ao bruxo', 'Salve Princesa');

INSERT INTO Contem VALUES (1, 'ganhar arma');
INSERT INTO Contem VALUES (1, 'AmigoStoyAqui');
INSERT INTO Contem VALUES (5, 'Mate um monstro');
INSERT INTO Contem VALUES (73, 'Festa no céu');
INSERT INTO Contem VALUES (5, 'Reino de fogo');
INSERT INTO Contem VALUES (43, 'Salve a dama');
INSERT INTO Contem VALUES (43, 'Mate o rei de fogo');
INSERT INTO Contem VALUES (43, 'ficando forte');
INSERT INTO Contem VALUES (5, 'Rainha Vampira');
INSERT INTO Contem VALUES (20, 'Hora de Aventura');
INSERT INTO Contem VALUES (115, 'inferno é Fogo');
INSERT INTO Contem VALUES (145, 'Caçar demônios');
INSERT INTO Contem VALUES (204, 'Embate a noitosfera');
INSERT INTO Contem VALUES (204, 'Rumo ao Litch');
INSERT INTO Contem VALUES (202, 'Maior, mais forte');
INSERT INTO Contem VALUES (202, 'conquista do espaço');
INSERT INTO Contem VALUES (202, 'Duro de matar');
INSERT INTO Contem VALUES (230, 'Morte ao bruxo');
INSERT INTO Contem VALUES (262, 'Salve Princesa');

INSERT INTO chefe VALUES (13, 'Mate o rei de fogo', 11);
INSERT INTO chefe VALUES (68, 'Embate a noitosfera', 30);
INSERT INTO chefe VALUES (74, 'Duro de matar', 35);
INSERT INTO chefe VALUES (1, 'Morte ao bruxo', 1);

--HABILIDADES



insert into habilidade values(1, 'Elasticidade', 0, 100); --Cachorro
insert into habilidade values(2, 'Elasticidade lvl 2', 0, 150); 
insert into habilidade values(3, 'Baforada de fogo', 10, 350); 
insert into habilidade values(4, 'Mordida', 0, 30); -- Vampiro
INSERT INTO Habilidade VALUES (5, 'Chuva de Flechas', 0, 20); 
insert into habilidade values(6, 'porrada', 0, 10); 
INSERT INTO Habilidade VALUES (7, 'Setas de Gelo', 18, 60); -- Cristal
INSERT INTO Habilidade VALUES (8, 'Setas de Gelo2', 18, 120);
INSERT INTO Habilidade VALUES (9, 'Setas de Gelo3', 18, 400);
INSERT INTO Habilidade VALUES (10, 'Onda de morte', 30, 1800); 
INSERT INTO Habilidade VALUES (11, 'Bola de fogo', 4, 60); -- Povo de Fogo
INSERT INTO Habilidade VALUES (12, 'Bola de fogo2', 8, 235);
INSERT INTO Habilidade VALUES (13, 'mísseis mágicos', 1, 180);
INSERT INTO Habilidade VALUES (14, 'Magia da luz', 10, 999);
INSERT INTO Habilidade VALUES (15, 'Cura reversa', 4, 60);
INSERT INTO Habilidade VALUES (16, 'Bola de cocô', 4, 60); 
INSERT INTO Habilidade VALUES (17, 'Cuspe ácido', 2, 60);
INSERT INTO Habilidade VALUES (18, 'Cuspe ácido2', 4, 340);
INSERT INTO Habilidade VALUES (19, 'Vento gelado', 4, 360);
INSERT INTO Habilidade VALUES (20, 'Estalinho', 0, 10); -- Humano
INSERT INTO Habilidade VALUES (21, 'Estalinho2', 0, 20);
INSERT INTO Habilidade VALUES (22, 'Estalinho3', 0, 99);
INSERT INTO Habilidade VALUES (23, 'Estalinho4', 0, 200);
INSERT INTO Habilidade VALUES (24, 'Xbox', 0, 360);
INSERT INTO Habilidade VALUES (25, 'Tornado', 9, 100);
INSERT INTO Habilidade VALUES (26, 'Luz', 0, 30);
INSERT INTO Habilidade VALUES (27, 'Lazer', 65, 1900);
INSERT INTO Habilidade VALUES (28, 'Jato de agua', 0, 90);
insert into habilidade values(29, 'Elasticidade3', 0, 200);
insert into habilidade values(30, 'Elasticidade4', 0, 500);
INSERT INTO Habilidade VALUES (31, 'Cuspe ácido3', 4, 740);
INSERT INTO Habilidade VALUES (32, 'Estalinho5', 0, 600);
INSERT INTO Habilidade VALUES (33, 'Ataque sonoro', 0, 600); 

insert into prerequisitohab values(3,12);
insert into prerequisitohab values(12,11);
insert into prerequisitohab values(25,26);
insert into prerequisitohab values(9,8);
insert into prerequisitohab values(8,7);
insert into prerequisitohab values(19,25);
insert into prerequisitohab values(18,17);
insert into prerequisitohab values(7,19);
insert into prerequisitohab values(32,23);
insert into prerequisitohab values(23,22);
insert into prerequisitohab values(22,21);
insert into prerequisitohab values(21,20);
insert into prerequisitohab values(27,14);

insert into possuihab values('37',24);
insert into possuihab values('36',18);
insert into possuihab values('35',27);
insert into possuihab values('35',23);
insert into possuihab values('34',12);
insert into possuihab values('33',5);
insert into possuihab values('32',25);
insert into possuihab values('31',25);
insert into possuihab values('30',3);
insert into possuihab values('30',18);
insert into possuihab values('29',31);
insert into possuihab values('28',11);
insert into possuihab values('27',17);
insert into possuihab values('26',4);
insert into possuihab values('25',9);
insert into possuihab values('24',6);
insert into possuihab values('23',4);
insert into possuihab values('22',6);
insert into possuihab values('21',9);
insert into possuihab values('21',19);
insert into possuihab values('20',33);
insert into possuihab values('19',18);
insert into possuihab values('18',13);
insert into possuihab values('18',5);
insert into possuihab values('17',4);
insert into possuihab values('16',4);
insert into possuihab values('15',4);
insert into possuihab values('14',17);
insert into possuihab values('13',11);
insert into possuihab values('12',11);
insert into possuihab values('11',12);
insert into possuihab values('11',3);
insert into possuihab values('10',12);
insert into possuihab values('9',6);
insert into possuihab values('8',28);
insert into possuihab values('7',4);
insert into possuihab values('6',6);
insert into possuihab values('5',6);
insert into possuihab values('4',13);
insert into possuihab values('3',6);
insert into possuihab values('2',2);
insert into possuihab values('1',10);
insert into possuihab values('1',24);
insert into possuihab values('1',32);

--Lojas

insert into loja values('Loja do Doan', 'Loja');
insert into loja values('Loja do Mr.Mcloud', 'Loja');
insert into loja values('A ultima loja', 'Loja');
insert into loja values('Loja do Arthur', 'Ferreiro', '5', 'S', '19');

update loja set local = 280 where nome = 'A ultima loja';
update loja set local = 162 where nome = 'Loja do Mr.Mcloud';
update loja set local = 3 where nome = 'Loja do Doan';


--Espadas

insert into item values('1','1');
insert into item values('2','1');
insert into item values('3','1');
insert into item values('4','1');
insert into item values('5','1');
insert into item values('6','1');
insert into item values('7','1');
insert into item values('8','2');
insert into item values('9','3');

insert into armamento values('1','Scarlet','11');
insert into armamento values('2','Espada Raiz','13');
insert into armamento values('3','Espada de Grama','17');
insert into armamento values('4','Espada Finn','15');
insert into armamento values('5','Florete','13');
insert into armamento values('6','Espada da Noite','23');
insert into armamento values('7','Espada Rei Demonio','24');

insert into armadura values('8', 'Escudo de Prata', '10', '15');

insert into consumivel values('9', 'Elixir Tunadasso', '100', '1');

insert into instanciaitem values('1', '1', '10');
insert into instanciaitem values('2', '1', '10');
insert into instanciaitem values('3', '1', '10');
insert into instanciaitem values('4', '1', '10');
insert into instanciaitem values('5', '1', '10');
insert into instanciaitem values('6', '1', '10');
insert into instanciaitem values('7', '1', '10');

insert into possuiitem values('1', 'Loja do Doan', 'Loja', '45');
insert into possuiitem values('2', 'Loja do Arthur', 'Ferreiro', '47');
insert into possuiitem values('3', 'Loja do Doan', 'Loja', '51');
insert into possuiitem values('4', 'Loja do Mr.Mcloud', 'Loja', '40');
insert into possuiitem values('5', 'Loja do Doan', 'Loja', '45');
insert into possuiitem values('6', 'Loja do Arthur', 'Ferreiro', '67');
insert into possuiitem values('7', 'Loja do Arthur', 'Ferreiro', '68');
insert into possuiitem values('8', 'Loja do Doan', 'Loja', '50');
insert into possuiitem values('9', 'Loja do Doan', 'Loja', '30');
insert into possuiitem values('8', 'Loja do Arthur', 'Ferreiro', '50');
insert into possuiitem values('9', 'Loja do Arthur', 'Ferreiro', '30');

commit;
end transaction; 
