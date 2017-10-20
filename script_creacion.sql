
-- DROP TABLE especie_pokemon;

CREATE TABLE especie_pokemon
(
  nombre text NOT NULL,
  numero_pokedex integer,
  descripcion text,
  CONSTRAINT pk_especie PRIMARY KEY (nombre ),
  CONSTRAINT ck_especie UNIQUE (numero_pokedex )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE especie_pokemon
  OWNER TO postgres;

-- Table: pokemon

-- DROP TABLE pokemon;

CREATE TABLE pokemon
(
  id integer NOT NULL,
  nombre_especie text,
  exp_acumulada integer,
  stats_def integer,
  stats_atk integer,
  stats_hp integer,
  stats_speed integer,
  stats_spdef integer,
  stats_spatk integer,
  CONSTRAINT pk_pokemon PRIMARY KEY (id ),
  CONSTRAINT fk_nombre_especie FOREIGN KEY (nombre_especie)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pokemon
  OWNER TO postgres;

-- Table: entrenador

-- DROP TABLE entrenador;

CREATE TABLE entrenador
(
  nombre text,
  codigo_entrenador integer NOT NULL,
  dinero integer,
  cant_medallas integer,
  CONSTRAINT pk_entrenador PRIMARY KEY (codigo_entrenador )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE entrenador
  OWNER TO postgres;

-- Table: tipo

-- DROP TABLE tipo;

CREATE TABLE tipo
(
  nombre text NOT NULL,
  CONSTRAINT pk_tipo PRIMARY KEY (nombre )
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tipo
  OWNER TO postgres;

-- Table: ataque

-- DROP TABLE ataque;

CREATE TABLE ataque
(
  nombre text NOT NULL,
  potencia integer,
  nombre_tipo text,
  CONSTRAINT pk_ataque PRIMARY KEY (nombre ),
  CONSTRAINT fk_ataque_tipo FOREIGN KEY (nombre_tipo)
      REFERENCES tipo (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ataque
  OWNER TO postgres;

-- Table: tipo_especie

-- DROP TABLE tipo_especie;

CREATE TABLE tipo_especie
(
  nombre_tipo text NOT NULL,
  nombre_especie text NOT NULL,
  CONSTRAINT pk_tipo_especie PRIMARY KEY (nombre_tipo , nombre_especie ),
  CONSTRAINT fk_tipo_especie_nombre_especie FOREIGN KEY (nombre_especie)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_tipo_especie_nombre_tipo FOREIGN KEY (nombre_tipo)
      REFERENCES tipo (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE tipo_especie
  OWNER TO postgres;


-- Table: pokemon_salvaje

-- DROP TABLE pokemon_salvaje;

CREATE TABLE pokemon_salvaje
(
  numero_ruta integer NOT NULL,
  nombre_especie text NOT NULL,
  CONSTRAINT pk_pokemon_salvaje PRIMARY KEY (nombre_especie , numero_ruta ),
  CONSTRAINT fk_pokemon_salvaje_especie FOREIGN KEY (nombre_especie)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pokemon_salvaje
  OWNER TO postgres;

-- Table: pokemon_capturado

-- DROP TABLE pokemon_capturado;

CREATE TABLE pokemon_capturado
(
  codigo_entrenador integer,
  pokemon_id integer NOT NULL,
  CONSTRAINT pk_pokemon_capturados PRIMARY KEY (pokemon_id ),
  CONSTRAINT fk_pkmn_capturados_cod_entrenador FOREIGN KEY (codigo_entrenador)
      REFERENCES entrenador (codigo_entrenador) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_pkmn_capturados_pkmn_id FOREIGN KEY (pokemon_id)
      REFERENCES pokemon (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pokemon_capturado
  OWNER TO postgres;

-- Table: pokemon_en_equipo

-- DROP TABLE pokemon_en_equipo;

CREATE TABLE pokemon_en_equipo
(
  codigo_entrenador integer,
  pokemon_id integer NOT NULL,
  CONSTRAINT pk_pokemon_en_equipo PRIMARY KEY (pokemon_id ),
  CONSTRAINT fk_pkmn_en_equipo_cod_entrenador FOREIGN KEY (codigo_entrenador)
      REFERENCES entrenador (codigo_entrenador) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
  CONSTRAINT fk_pkmn_en_equipo_pkmn_id FOREIGN KEY (pokemon_id)
      REFERENCES pokemon (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE pokemon_en_equipo
  OWNER TO postgres;

-- Table: ataques_sabidos

-- DROP TABLE ataques_sabidos;

CREATE TABLE ataques_sabidos
(
  pokemon_id integer NOT NULL,
  nombre_ataque text NOT NULL,
  CONSTRAINT pk_ataques_sabidos PRIMARY KEY (pokemon_id , nombre_ataque ),
  CONSTRAINT fk_ataques_sabidos_ataque FOREIGN KEY (nombre_ataque)
      REFERENCES ataque (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_ataques_sabidos_id FOREIGN KEY (pokemon_id)
      REFERENCES pokemon (id) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE ataques_sabidos
  OWNER TO postgres;

-- Table: evolucion_por_nivel

-- DROP TABLE evolucion_por_nivel;

CREATE TABLE evolucion_por_nivel
(
  nombre_preevolucion text NOT NULL,
  nombre_evolucion text NOT NULL,
  nivel integer,
  CONSTRAINT pk_evol_por_nivel PRIMARY KEY (nombre_preevolucion , nombre_evolucion ),
  CONSTRAINT fk_evol_nivel_nombre_evolucion FOREIGN KEY (nombre_evolucion)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_evol_nivel_preevolucion FOREIGN KEY (nombre_preevolucion)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE evolucion_por_nivel
  OWNER TO postgres;

-- Table: evolucion_por_objeto

-- DROP TABLE evolucion_por_objeto;

CREATE TABLE evolucion_por_objeto
(
  nombre_preevolucion text NOT NULL,
  nombre_evolucion text NOT NULL,
  nombre_objeto text,
  CONSTRAINT pk_evol_por_objeto PRIMARY KEY (nombre_preevolucion , nombre_evolucion ),
  CONSTRAINT fk_evol_objeto_nombre_evolucion FOREIGN KEY (nombre_evolucion)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE,
  CONSTRAINT fk_evol_objeto_preevolucion FOREIGN KEY (nombre_preevolucion)
      REFERENCES especie_pokemon (nombre) MATCH SIMPLE
      ON UPDATE CASCADE ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE evolucion_por_objeto
  OWNER TO postgres;

-- Fill table: especie_pokemon

INSERT INTO especie_pokemon(nombre, numero_pokedex, descripcion) 
VALUES('Delcatty', 64, 'Rather than keeping a permanent lair, it habitually seeks comfortable spots and sleeps there. It is nocturnal and becomes active at dusk.'),
('Electrike', 80, 'It generates electricity using friction from the atmosphere. In seasons with especially arid air, its entire body blazes with violent showers of sparks.'),
('Gardevoir', 31, 'It apparently does not feel the pull of gravity because it supports itself with psychic power. It will give its life to protect its Trainer.'),
('Kirlia', 30, 'A Kirlia has the psychic power to create a rip in the dimensions and see into the future. It is said to dance with pleasure on sunny mornings.'),
('Linoone', 13, 'It is exceedingly fast if it only has to run in a straight line. When it spots pond-dwelling prey underwater, it quickly leaps in and catches it with its sharp claws.'),
('Magnemite', 84, 'The units at its sides are extremely powerful magnets. They generate enough magnetism to draw in iron objects from over 300 feet away.'),
('Magneton', 85, 'It is actually three Magnemite linked by magnetism. It generates powerful radio waves that raise temperatures by 3.6 degrees F within a 3,300-foot radius.'),
('Manectric', 81, 'Because lightning falls in their vicinities, Manectric were thought to have been born from lightning. In battle, they create thunderclouds.'),
('Ninetales', 161, 'It has long been said that each of the nine tails embody an enchanted power. A long-lived Ninetales will have fur that shines like gold.'),
('Nuzleaf', 23, 'A forest-dwelling Pokémon that is skilled at climbing trees. Its long and pointed nose is its weak point. It loses power if the nose is gripped.'),
('Pikachu', 163, 'It stores electricity in the electric sacs on its cheeks. When it releases pent-up energy in a burst, the electric power is equal to a lightning bolt.'),
('Poochyena', 10, 'It savagely threatens foes with bared fangs. It chases after fleeing targets tenaciously. It turns tail and runs, however, if the foe strikes back.'),
('Raichu', 164, 'If it stores too much electricity, its behavior turns aggressive. To avoid this, it occasionally discharges excess energy and calms itself down.'),
('Ralts', 29, 'A Ralts has the power to sense the emotions of people and Pokémon with the horns on its head. It takes cover if it senses any hostility.'),
('Seedot', 22, 'It hangs off branches and absorbs nutrients. When it finishes eating, its body becomes so heavy that it drops to the ground with a thump. '),
('Shiftry', 24, 'It is said to arrive on chilly, wintry winds. Feared from long ago as the guardian of forests, this Pokémon lives in a deep forest where people do not venture. '),
('Mightyena', 11, 'In the wild, Mightyena live in a pack. They never defy their leaders orders. They defeat foes with perfectly coordinated teamwork.'),
('Skitty', 63, 'A Skitty adorably cute behavior makes it highly popular. In battle, it makes its tail puff out. It threatens foes with a sharp growl. '),
('Starmie', 149, 'People in ancient times imagined that Starmie were transformed from the reflections of stars that twinkled on gentle waves at night.'),
('Staryu', 148, 'It gathers with others in the night and makes its red core glow on and off with the twinkling stars. It can regenerate limbs if they are severed from its body.'),
('Torkoal', 110, 'It battles using energy it gets from burning coal. When loosing smoke from its nostrils, it lets off a sound that is similar to a locomotive horn.'),
('Vulpix', 160, 'It can freely control fire, making fiery orbs fly like will-o-wisps. Just before evolution, its six tails grow hot as if on fire.'),
('Wailmer', 104, 'While this Pokémon usually lives in the sea, it can survive on land, although not too long. It loses vitality if its body becomes dried out.'),
('Wailord', 105, 'It breathes through nostrils that it raises above the sea. By inhaling to its maximum capacity, a Wailord can dive close to 10,000 feet beneath the waves.'),
('Zangoose', 128, 'When it battles, it stands on its hind legs and attacks with its sharply clawed forelegs. Its fur bristles if it encounters any Seviper.'),
('Zigzagoon', 12, 'Rubbing its nose against the ground, it always wanders about back and forth in search of something. It is distinguished by the zigzag footprints it leaves.');

-- Fill table: tipo

INSERT INTO tipo(nombre) 
VALUES('Normal'), ('Electric'), ('Psychic'), ('Dark'), ('Fire'), ('Grass'), ('Water');

-- Fill table: tipo_especie

INSERT INTO tipo_especie(nombre_especie, nombre_tipo) 
VALUES('Delcatty', 'Normal'), ('Electrike', 'Electric'), ('Gardevoir', 'Psychic'), ('Kirlia', 'Psychic'), 
('Linoone', 'Normal'), ('Magnemite', 'Electric'), ('Magneton', 'Electric'), ('Manectric', 'Electric'), ('Pikachu', 'Electric'), 
('Mightyena', 'Dark'), ('Ninetales', 'Fire'), ('Torkoal', 'Fire'), ('Nuzleaf', 'Dark'), ('Nuzleaf', 'Grass'), ('Poochyena', 'Dark'), ('Raichu', 'Electric'), ('Ralts', 'Psychic'), ('Seedot', 'Grass'), ('Shiftry', 'Grass'), ('Shiftry', 'Dark'), ('Skitty', 'Normal'),
('Staryu', 'Water'), ('Starmie', 'Water'), ('Starmie', 'Psychic'), ('Vulpix', 'Fire'), ('Wailmer', 'Water'), ('Wailord', 'Water'),
('Zangoose', 'Normal'), ('Zigzagoon', 'Normal');

-- Fill table: ataque

INSERT INTO ataque(nombre, potencia, nombre_tipo) 
VALUES('Slash', 70, 'Normal'), ('Spark', 65, 'Electric'), ('Seed bomb', 80, 'Grass'), ('Waterfall', 80, 'Water'),
('Surf', 80, 'Water'), ('Strength', 80, 'Normal'), ('Ember', 40, 'Fire'), ('Flamethrower', 90, 'Fire'), ('Psychic', 90, 'Psychic');

-- Fill table: evolucion_por_nivel

INSERT INTO evolucion_por_nivel(nombre_preevolucion, nombre_evolucion, nivel) 
VALUES('Electrike', 'Manectric', 26), ('Ralts', 'Kirlia', 20), ('Kirlia', 'Gardevoir', 30), ('Zigzagoon', 'Linoone', 20), 
('Magnemite', 'Magneton', 30), ('Poochyena', 'Mightyena', 18), ('Seedot', 'Nuzleaf', 18), ('Wailmer', 'Wailord', 40);


-- Fill table: evolucion_por_objeto

INSERT INTO evolucion_por_objeto(nombre_preevolucion, nombre_evolucion, nombre_objeto) 
VALUES('Vulpix', 'Ninetales', 'Firestone'), ('Nuzleaf', 'Shiftry', 'Leafstone'), ('Skitty', 'Delcatty', 'Moonstone'),
('Pikachu', 'Raichu', 'Thunderstone'), ('Staryu', 'Starmie', 'Waterstone');

-- Fill table: pokemon_salvaje

INSERT INTO pokemon_salvaje(numero_ruta, nombre_especie) 
VALUES(110, 'Electrike'), (118, 'Electrike'), (102, 'Ralts'), (118, 'Linoone'), (119, 'Linoone'), (120, 'Linoone'), (121, 'Linoone'),
(123, 'Linoone'), (110, 'Magnemite'), (110, 'Magneton'), (118, 'Manectric'), (120, 'Mightyena'), (121, 'Mightyena'), (123, 'Mightyena'),
(114, 'Nuzleaf'), (110, 'Pikachu'), (101, 'Poochyena'), (102, 'Poochyena'), (103, 'Poochyena'), (104, 'Poochyena'), (110, 'Poochyena'),
(116, 'Poochyena'), (117, 'Poochyena'), (120, 'Poochyena'), (121, 'Poochyena'), (123, 'Poochyena'), (102, 'Seedot'), (114, 'Seedot'),
(116, 'Seedot'), (117, 'Seedot'), (120, 'Seedot'), (116, 'Skitty'), (121, 'Staryu'), (112, 'Torkoal'),  (122, 'Vulpix'), (103, 'Wailmer'),
(105, 'Wailmer'), (106, 'Wailmer'), (107, 'Wailmer'), (108, 'Wailmer'), (109, 'Wailmer'), (110, 'Wailmer'), (115, 'Wailmer'),
(121, 'Wailmer'), (122, 'Wailmer'), (123, 'Wailmer'), (124, 'Wailmer'), (125, 'Wailmer'), (126, 'Wailmer'), (127, 'Wailmer'), 
(128, 'Wailmer'), (129, 'Wailmer'), (130, 'Wailmer'), (114, 'Zangoose'), (101, 'Zigzagoon'), (102, 'Zigzagoon'), (103, 'Zigzagoon'), 
(104, 'Zigzagoon'), (110, 'Zigzagoon'), (116, 'Zigzagoon'), (117, 'Zigzagoon'), (118, 'Zigzagoon'), (119, 'Zigzagoon'),
(120, 'Zigzagoon'), (121, 'Zigzagoon'), (123, 'Zigzagoon');


-- Fill table: entrenador

INSERT INTO entrenador(nombre, codigo_entrenador, dinero, cant_medallas)
VALUES('ALFA', 125779, 95400, 7), ('BETA', 423788, 145700, 8);


-- Fill table: pokemon

INSERT INTO pokemon(id, nombre_especie, exp_acumulada, stats_def, stats_atk, stats_hp, stats_speed, stats_spdef, stats_spatk)
VALUES(1, 'Ralts', 580, 16, 8, 31, 14, 19, 22),
(2, 'Kirlia', 3140, 36, 24, 82, 34, 44, 49), (3, 'Gardevoir', 8800, 16, 8, 31, 14, 19, 22),
(4, 'Wailmer', 580, 16, 8, 31, 14, 19, 22), (5, 'Pikachu', 580, 16, 8, 31, 14, 19, 22),
(6, 'Raichu', 3140, 36, 24, 82, 34, 44, 49), (7, 'Zigzagoon', 580, 16, 8, 31, 14, 19, 22),
(8, 'Zangoose', 580, 16, 8, 31, 14, 19, 22), (9, 'Staryu', 580, 16, 8, 31, 14, 19, 22),
(10, 'Poochyena', 580, 16, 8, 31, 14, 19, 22), (66, 'Staryu', 580, 16, 8, 31, 14, 19, 22),
(11, 'Mightyena', 5140, 36, 24, 82, 34, 44, 49), (12, 'Mightyena', 5140, 36, 24, 82, 34, 44, 49),
(13, 'Mightyena', 5140, 36, 24, 82, 34, 44, 49), (14, 'Shiftry', 5140, 36, 24, 82, 34, 44, 49),
(15, 'Electrike', 580, 16, 8, 31, 14, 19, 22), (16, 'Vulpix', 5140, 36, 24, 82, 34, 44, 49), 
(17, 'Magneton', 5140, 36, 24, 82, 34, 44, 49), (18, 'Seedot', 580, 16, 8, 31, 14, 19, 22);

-- Fill table: pokemon_capturado

INSERT INTO pokemon_capturado(codigo_entrenador, pokemon_id)
VALUES(125779, 1), (423788, 2), (423788, 3), (125779, 4), (125779, 5), (423788, 6), (125779, 7),
(125779, 8), (125779, 9), (125779, 10), (125779, 11), (423788, 12), (423788, 13), (125779, 14), (125779, 15),
(125779, 16), (125779, 17), (423788, 18), (423788, 66);
