
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'C064D8830D78A85D31C9D67427D7B6DB'
    
_lr_action_items = {'NOTEQ':([41,44,45,60,62,63,64,65,66,67,70,80,81,82,83,84,],[-49,-49,72,-42,-43,-47,-48,-35,-46,-30,-31,-34,-44,-45,-33,-32,]),'CTEED':([33,34,35,40,42,43,46,47,54,59,61,68,69,72,73,75,],[-49,-49,-49,-49,63,-38,-37,-36,-49,-49,-49,-49,-49,-49,-49,-49,]),'PRINT':([13,19,20,21,26,77,79,92,],[22,-16,22,-17,-18,-19,-25,-39,]),')':([37,38,39,41,44,45,48,53,55,56,58,60,62,63,64,65,66,67,70,71,74,78,80,81,82,83,84,85,86,87,],[-49,-49,57,-49,-49,-49,76,-26,-28,-27,80,-42,-43,-47,-48,-35,-46,-30,-31,-20,-21,-29,-34,-44,-45,-33,-32,-24,-23,-22,]),'(':([22,23,33,34,35,40,54,59,61,68,69,72,73,75,],[33,34,40,40,40,40,40,40,40,40,40,40,40,40,]),'+':([33,34,35,40,41,44,54,59,60,61,62,63,64,65,66,68,69,72,73,75,80,81,82,],[46,46,46,46,-49,69,46,46,-42,46,-43,-47,-48,-35,-46,46,46,46,46,46,-34,-44,-45,]),'*':([41,63,64,65,66,80,],[59,-47,-48,-35,-46,-34,]),'-':([33,34,35,40,41,44,54,59,60,61,62,63,64,65,66,68,69,72,73,75,80,81,82,],[43,43,43,43,-49,68,43,43,-42,43,-43,-47,-48,-35,-46,43,43,43,43,43,-34,-44,-45,]),',':([11,37,38,41,44,45,60,62,63,64,65,66,67,70,71,74,80,81,82,83,84,85,86,87,],[17,54,54,-49,-49,-49,-42,-43,-47,-48,-35,-46,-30,-31,-20,-21,-34,-44,-45,-33,-32,-24,-23,-22,]),'/':([41,63,64,65,66,80,],[61,-47,-48,-35,-46,-34,]),';':([3,27,28,29,31,41,44,45,49,57,60,62,63,64,65,66,67,70,71,74,80,81,82,83,84,85,86,87,88,89,91,93,],[4,36,-11,-12,-13,-49,-49,-49,77,79,-42,-43,-47,-48,-35,-46,-30,-31,-20,-21,-34,-44,-45,-33,-32,-24,-23,-22,-49,92,-40,-41,]),':':([10,11,15,16,30,],[14,-49,-8,-9,-10,]),'=':([24,],[35,]),'<':([41,44,45,60,62,63,64,65,66,67,70,80,81,82,83,84,],[-49,-49,73,-42,-43,-47,-48,-35,-46,-30,-31,-34,-44,-45,-33,-32,]),'$end':([1,12,31,],[0,-1,-13,]),'ELSE':([31,88,],[-13,90,]),'VAR':([4,],[6,]),'ID':([2,6,13,17,19,20,21,26,33,34,35,36,40,42,43,46,47,54,59,61,68,69,72,73,75,77,79,92,],[3,11,24,11,-16,24,-17,-18,-49,-49,-49,11,-49,66,-38,-37,-36,-49,-49,-49,-49,-49,-49,-49,-49,-19,-25,-39,]),'IF':([13,19,20,21,26,77,79,92,],[23,-16,23,-17,-18,-19,-25,-39,]),'CTES':([33,54,],[38,38,]),'INT':([14,],[28,]),'FLOAT':([14,],[29,]),'CTEF':([33,34,35,40,42,43,46,47,54,59,61,68,69,72,73,75,],[-49,-49,-49,-49,64,-38,-37,-36,-49,-49,-49,-49,-49,-49,-49,-49,]),'PROG':([0,],[2,]),'{':([4,5,7,8,9,36,50,51,52,76,90,],[-49,-3,13,-2,-4,-49,-7,-5,-6,13,13,]),'>':([41,44,45,60,62,63,64,65,66,67,70,80,81,82,83,84,],[-49,-49,75,-42,-43,-47,-48,-35,-46,-30,-31,-34,-44,-45,-33,-32,]),'}':([13,18,19,20,21,25,26,32,77,79,92,],[-49,31,-16,-49,-17,-14,-18,-15,-19,-25,-39,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'vars':([4,],[5,]),'termino':([33,34,35,40,54,59,61,68,69,72,73,75,],[44,44,44,44,44,81,82,44,44,44,44,44,]),'bloque':([7,76,90,],[12,88,93,]),'varcte':([42,],[65,]),'tipo':([14,],[27,]),'estatuto':([13,20,],[20,20,]),'condicion':([13,20,],[21,21,]),'asignacion':([13,20,],[19,19,]),'factor':([33,34,35,40,54,59,61,68,69,72,73,75,],[41,41,41,41,41,41,41,41,41,41,41,41,]),'empty':([4,11,13,20,33,34,35,36,37,38,40,41,44,45,54,59,61,68,69,72,73,75,88,],[8,16,25,25,47,47,47,52,55,55,47,62,70,74,47,47,47,47,47,47,47,47,91,]),'expresion':([33,34,35,40,54,],[37,48,49,58,37,]),'a':([6,36,],[9,50,]),'c':([11,],[15,]),'b':([6,17,36,],[10,30,10,]),'d':([13,20,],[18,32,]),'g':([33,54,],[39,78,]),'f':([36,],[51,]),'i':([45,],[71,]),'h':([37,38,],[53,56,]),'k':([44,],[67,]),'j':([88,],[89,]),'m':([33,34,35,40,54,59,61,68,69,72,73,75,],[42,42,42,42,42,42,42,42,42,42,42,42,]),'l':([41,],[60,]),'programa':([0,],[1,]),'exp':([33,34,35,40,54,68,69,72,73,75,],[45,45,45,45,45,83,84,85,86,87,]),'v':([4,],[7,]),'escritura':([13,20,],[26,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROG ID ; v bloque','programa',5,'p_programa','patito.py',82),
  ('v -> empty','v',1,'p_v','patito.py',87),
  ('v -> vars','v',1,'p_v','patito.py',88),
  ('vars -> VAR a','vars',2,'p_vars','patito.py',92),
  ('a -> b : tipo ; f','a',5,'p_a','patito.py',96),
  ('f -> empty','f',1,'p_f','patito.py',100),
  ('f -> a','f',1,'p_f','patito.py',101),
  ('b -> ID c','b',2,'p_b','patito.py',105),
  ('c -> empty','c',1,'p_c','patito.py',109),
  ('c -> , b','c',2,'p_c','patito.py',110),
  ('tipo -> INT','tipo',1,'p_tipo','patito.py',114),
  ('tipo -> FLOAT','tipo',1,'p_tipo','patito.py',115),
  ('bloque -> { d }','bloque',3,'p_bloque','patito.py',119),
  ('d -> empty','d',1,'p_d','patito.py',124),
  ('d -> estatuto d','d',2,'p_d','patito.py',125),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','patito.py',129),
  ('estatuto -> condicion','estatuto',1,'p_estatuto','patito.py',130),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','patito.py',131),
  ('asignacion -> ID = expresion ;','asignacion',4,'p_asignacion','patito.py',135),
  ('expresion -> exp i','expresion',2,'p_expresion','patito.py',140),
  ('i -> empty','i',1,'p_i','patito.py',144),
  ('i -> > exp','i',2,'p_i','patito.py',145),
  ('i -> < exp','i',2,'p_i','patito.py',146),
  ('i -> NOTEQ exp','i',2,'p_i','patito.py',147),
  ('escritura -> PRINT ( g ) ;','escritura',5,'p_escritura','patito.py',151),
  ('g -> expresion h','g',2,'p_g','patito.py',155),
  ('g -> CTES h','g',2,'p_g','patito.py',156),
  ('h -> empty','h',1,'p_h','patito.py',160),
  ('h -> , g','h',2,'p_h','patito.py',161),
  ('exp -> termino k','exp',2,'p_exp','patito.py',165),
  ('k -> empty','k',1,'p_k','patito.py',169),
  ('k -> + exp','k',2,'p_k','patito.py',170),
  ('k -> - exp','k',2,'p_k','patito.py',171),
  ('factor -> ( expresion )','factor',3,'p_factor','patito.py',175),
  ('factor -> m varcte','factor',2,'p_factor','patito.py',176),
  ('m -> empty','m',1,'p_m','patito.py',180),
  ('m -> +','m',1,'p_m','patito.py',181),
  ('m -> -','m',1,'p_m','patito.py',182),
  ('condicion -> IF ( expresion ) bloque j ;','condicion',7,'p_condicion','patito.py',186),
  ('j -> empty','j',1,'p_j','patito.py',190),
  ('j -> ELSE bloque','j',2,'p_j','patito.py',191),
  ('termino -> factor l','termino',2,'p_termino','patito.py',195),
  ('l -> empty','l',1,'p_l','patito.py',199),
  ('l -> * termino','l',2,'p_l','patito.py',200),
  ('l -> / termino','l',2,'p_l','patito.py',201),
  ('varcte -> ID','varcte',1,'p_varcte','patito.py',205),
  ('varcte -> CTEED','varcte',1,'p_varcte','patito.py',206),
  ('varcte -> CTEF','varcte',1,'p_varcte','patito.py',207),
  ('empty -> <empty>','empty',0,'p_empty','patito.py',211),
]
