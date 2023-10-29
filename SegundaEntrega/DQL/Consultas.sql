--Visualizando os itens do inventario
SELECT I.nome, I.IDitem, Ia.durabilidade FROM Item I JOIN InstanciaItem Ia ON I.IDitem = Ia.IDitem 
JOIN Inventario Inv ON Ia.IDinv = Inv.IDinv
JOIN Personagem P ON Inv.Personagem = P.IDpersonagem
WHERE P.IDpersonagem = 2;

--Visualizando a tabela de habilidades do personagem
SELECT IDhabilidade, Nome, Tempo_de_recarga, Dano, Nivel_requerido
FROM Habilidade
INNER JOIN PossuiHab ON Habilidade = IDhabilidade
WHERE Personagem = 2;


--Visualizando as missoes do local que o pc tá
SELECT F.NomeMissao, F.Status FROM FazMissao F JOIN Contem C  JOIN Local L JOIN Pc P 
ON P.local = L.Coordenada
ON L.Coordenada = C.Local
ON C.Missao = F.NomeMissao
WHERE P.personagem = 2;

--Vendo os itens da loja
SELECT Item.IDitem, Item.Nome, Item.Durabilidade, Item.Dano, Item.Tipo
FROM Item
INNER JOIN PossuiItem ON Item.IDitem = PossuiItem.IDitem
WHERE PossuiItem.Loja = 'Loja de Arma';

