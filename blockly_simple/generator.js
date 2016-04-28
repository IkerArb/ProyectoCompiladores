//PROGRAMA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s5s3x5
Blockly.JavaScript['programa'] = function(block) {
  var statements_vars = Blockly.JavaScript.statementToCode(block, 'vars');
  var statements_funciones = Blockly.JavaScript.statementToCode(block, 'funciones');
  var text_tempo = block.getFieldValue('tempo');
  var statements_cancion = Blockly.JavaScript.statementToCode(block, 'cancion');
  // TODO: Assemble JavaScript into code variable.
  var code = statements_vars +'\n' +statements_funciones +'\n' +'CANCION (' +text_tempo +') ' +statements_cancion +'\n';
  return code;
};

//VARIABLE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#bzj9yt
Blockly.JavaScript['variable'] = function(block) {
  var text_id = block.getFieldValue('id');
  var dropdown_tipo = block.getFieldValue('tipo');
  // TODO: Assemble JavaScript into code variable.
  var code = 'VAR ' +text_id +' : ' +dropdown_tipo ';\n';
  return code;
};

//BLOQUE_CANCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#6xrwfx
Blockly.JavaScript['bloque_cancion'] = function(block) {
  var statements_vars = Blockly.JavaScript.statementToCode(block, 'vars');
  var statements_funcs = Blockly.JavaScript.statementToCode(block, 'funcs');
  // TODO: Assemble JavaScript into code variable.
  var code = statements_vars +'\n' +'{\n' +statements_funcs +'}\n';
  return code;
};

//BLOQUE_FUNCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2euwrg
Blockly.JavaScript['bloque_funcion'] = function(block) {
  var text_id = block.getFieldValue('id');
  var dropdown_tipo = block.getFieldValue('tipo');
  var value_params = Blockly.JavaScript.valueToCode(block, 'params', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_vars = Blockly.JavaScript.statementToCode(block, 'vars');
  var statements_funcs = Blockly.JavaScript.statementToCode(block, 'funcs');
  // TODO: Assemble JavaScript into code variable.
  var code = 'FUNC ' +dropdown_tipo +' ' +text_id +'(' +value_params +')' +statements_vars +'\n' +'{\n' +statements_funcs  +'}\n';
  return code;
};

//VAR LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#5o7cym
Blockly.JavaScript['var_lista'] = function(block) {
  var text_id = block.getFieldValue('id');
  var dropdown_tipo = block.getFieldValue('tipo');
  var value_longitud = Blockly.JavaScript.valueToCode(block, 'longitud', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'VAR ' +text_id + ' : ' +dropdown_tipo +' LIST(' +value_longitud +');\n';
  return code;
};

//ASSIG LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#3m49y3
Blockly.JavaScript['assig_lista'] = function(block) {
  var text_id = block.getFieldValue('id');
  var value_expresion = Blockly.JavaScript.valueToCode(block, 'expresion', Blockly.JavaScript.ORDER_ATOMIC);
  var value_resultado = Blockly.JavaScript.valueToCode(block, 'resultado', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = +text_id +'[' +value_expresion +'] = ' +value_resultado +';\n';
  return code;
};

//LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#25ah7o
Blockly.JavaScript['lista'] = function(block) {
  var text_id = block.getFieldValue('id');
  var value_expresion = Blockly.JavaScript.valueToCode(block, 'expresion', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_id +'[' +value_expresion +']';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//NUM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.JavaScript['num'] = function(block) {
  var text_num = block.getFieldValue('num');
  // TODO: Assemble JavaScript into code variable.
  var code = text_num;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//VAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.JavaScript['var'] = function(block) {
  var text_id = block.getFieldValue('id');
  // TODO: Assemble JavaScript into code variable.
  var code = text_id;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//NOT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#azhtpw
Blockly.JavaScript['not'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'NOT ' +value_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//PARENTESIS
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#iu4dcw
Blockly.JavaScript['parentesis'] = function(block) {
  var value_name = Blockly.JavaScript.valueToCode(block, 'NAME', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = '(' +value_name +')';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//EXPRESION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2rrkzb
Blockly.JavaScript['expresion'] = function(block) {
  var value_op1 = Blockly.JavaScript.valueToCode(block, 'op1', Blockly.JavaScript.ORDER_ATOMIC);
  var dropdown_operador = block.getFieldValue('operador');
  var value_op2 = Blockly.JavaScript.valueToCode(block, 'op2', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_op1 +dropdown_operador +value_op2;
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//IF
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#qeu7fd
Blockly.JavaScript['if'] = function(block) {
  var value_exp_if = Blockly.JavaScript.valueToCode(block, 'exp_if', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_bloque_if = Blockly.JavaScript.statementToCode(block, 'bloque_if');
  // TODO: Assemble JavaScript into code variable.
  var code = 'IF (' +value_exp_if +')' +'{\n' +statements_bloque_if +'\n};';
  return code;
};

//IF_ELSE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#c5xuw2
Blockly.JavaScript['if_else'] = function(block) {
  var value_exp_if = Blockly.JavaScript.valueToCode(block, 'exp_if', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_bloque_if = Blockly.JavaScript.statementToCode(block, 'bloque_if');
  var statements_bloque_else = Blockly.JavaScript.statementToCode(block, 'bloque_else');
  // TODO: Assemble JavaScript into code variable.
  var code = 'IF (' +value_exp_if +')' +'{\n' +statements_bloque_if +'\n}' +'\nELSE {\n' +statements_bloque_else +'\n};';
  return code;
};

//FOR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#ts8vpi
Blockly.JavaScript['for'] = function(block) {
  var value_exp_for1 = Blockly.JavaScript.valueToCode(block, 'exp_for1', Blockly.JavaScript.ORDER_ATOMIC);
  var value_exp_for2 = Blockly.JavaScript.valueToCode(block, 'exp_for2', Blockly.JavaScript.ORDER_ATOMIC);
  var value_exp_for3 = Blockly.JavaScript.valueToCode(block, 'exp_for3', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_bloque_for = Blockly.JavaScript.statementToCode(block, 'bloque_for');
  // TODO: Assemble JavaScript into code variable.
  var code = 'FOR (' +value_exp_for1 +value_exp_for2 +value_exp_for3 +')' +'{\n' +statements_bloque_for +'\n};' ;
  return code;
};

//WHILE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#3w2m6p
Blockly.JavaScript['while'] = function(block) {
  var value_exp_while = Blockly.JavaScript.valueToCode(block, 'exp_while', Blockly.JavaScript.ORDER_ATOMIC);
  var statements_bloque_while = Blockly.JavaScript.statementToCode(block, 'bloque_while');
  // TODO: Assemble JavaScript into code variable.
  var code = 'WHILE (' +value_exp_while ')' +'{\n' +statements_bloque_while +'\n};';
  return code;
};

//PLAY
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#yxpjtd
Blockly.JavaScript['play'] = function(block) {
  var text_nota = block.getFieldValue('nota');
  var dropdown_duracion = block.getFieldValue('duracion');
  // TODO: Assemble JavaScript into code variable.
  var code = 'PLAY(' +text_nota +',' +dropdown_duracion +');';
  return code;
};

//PRINT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#cnjojz
Blockly.JavaScript['print'] = function(block) {
  var value_text = Blockly.JavaScript.valueToCode(block, 'text', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'PRINT ' +value_text +';';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//RETURN
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#p8bb66
Blockly.JavaScript['return'] = function(block) {
  var value_text = Blockly.JavaScript.valueToCode(block, 'text', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'RETURN (' +value_text +');';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};

//CALL
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#zz7a3u
Blockly.JavaScript['call'] = function(block) {
  var text_idfunc = block.getFieldValue('idFunc');
  var value_text = Blockly.JavaScript.valueToCode(block, 'text', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'CALL ' +text_idfunc +'(' +value_text +');';
  // TODO: Change ORDER_NONE to the correct strength.
  return [code, Blockly.JavaScript.ORDER_NONE];
};
