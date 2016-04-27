//PROGRAMA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s5s3x5
Blockly.Blocks['programa'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("PROGRAMA");
    this.appendDummyInput()
        .appendField("VARS");
    this.appendStatementInput("vars")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("FUNCIONES");
    this.appendStatementInput("funciones")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("CANCION")
        .appendField(new Blockly.FieldTextInput("90"), "tempo");
    this.appendStatementInput("cancion")
        .setCheck(null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//VARIABLE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#bzj9yt
Blockly.Blocks['variable'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("VARIABLE")
        .appendField(new Blockly.FieldTextInput("nombreVar"), "id")
        .appendField(new Blockly.FieldDropdown([["int", "INT"], ["float", "FLOAT"], ["char", "CHAR"], ["bool", "BOOL"]]), "tipo");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//BLOQUE_CANCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#6xrwfx
Blockly.Blocks['bloque_cancion'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("VARS CANCION");
    this.appendStatementInput("vars")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("FUNCS CANCION");
    this.appendStatementInput("funcs")
        .setCheck(null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//BLOQUE_FUNCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2euwrg
Blockly.Blocks['bloque_funcion'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("FUNCION")
        .appendField(new Blockly.FieldTextInput("nombreFunc"), "id")
        .appendField(new Blockly.FieldDropdown([["int", "INT"], ["float", "FLOAT"], ["char", "CHAR"], ["bool", "BOOL"]]), "tipo")
        .appendField("PARAMS");
    this.appendValueInput("params")
        .setCheck(null);
    this.appendStatementInput("vars")
        .setCheck(null)
        .appendField("VARS CANCION");
    this.appendStatementInput("funcs")
        .setCheck(null)
        .appendField("FUNCS CANCION");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//VAR LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#5o7cym
Blockly.Blocks['var_lista'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("VAR LISTA")
        .appendField(new Blockly.FieldTextInput("nombreVar"), "id")
        .appendField(new Blockly.FieldDropdown([["int", "INT"], ["float", "FLOAT"], ["char", "CHAR"], ["bool", "BOOL"]]), "tipo");
    this.appendValueInput("longitud")
        .setCheck(null)
        .appendField("longitud");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//ASSIG LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#3m49y3
Blockly.Blocks['assig_lista'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("ASSIG LISTA")
        .appendField(new Blockly.FieldTextInput("idVar"), "id");
    this.appendValueInput("expresion")
        .setCheck(null)
        .appendField("[");
    this.appendValueInput("resultado")
        .setCheck(null)
        .appendField("]")
        .appendField("=");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#25ah7o
Blockly.Blocks['lista'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("LISTA")
        .appendField(new Blockly.FieldTextInput("idLista"), "id");
    this.appendValueInput("expresion")
        .setCheck(null)
        .appendField("[");
    this.appendDummyInput()
        .appendField("]");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//NUM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.Blocks['num'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NUM")
        .appendField(new Blockly.FieldTextInput("numero"), "num");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


//VAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.Blocks['var'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("VAR")
        .appendField(new Blockly.FieldTextInput("idVar"), "id");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//NOT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#azhtpw
Blockly.Blocks['not'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NOT");
    this.appendValueInput("NAME")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//PARENTESIS
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#iu4dcw
Blockly.Blocks['parentesis'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("(");
    this.appendValueInput("NAME")
        .setCheck(null);
    this.appendDummyInput()
        .appendField(")");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//EXPRESION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2rrkzb
Blockly.Blocks['expresion'] = {
  init: function() {
    this.appendValueInput("op1")
        .setCheck(null);
    this.appendValueInput("op2")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["+", "+"], ["-", "-"], ["*", "*"], ["/", "/"], ["and", "and"], ["or", "or"], ["==", "=="], ["!=", "!="], [">", ">"], ["<", "<"], ["=>", "=>"], ["=<", "=<"]]), "operador");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//IF
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#qeu7fd
Blockly.Blocks['if'] = {
  init: function() {
    this.appendValueInput("exp_if")
        .setCheck(null)
        .appendField("IF");
    this.appendStatementInput("bloque_if")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//IF_ELSE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#c5xuw2
Blockly.Blocks['if_else'] = {
  init: function() {
    this.appendValueInput("exp_if")
        .setCheck(null)
        .appendField("IF");
    this.appendStatementInput("bloque_if")
        .setCheck(null);
    this.appendStatementInput("bloque_else")
        .setCheck(null)
        .appendField("else");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//FOR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#ts8vpi
Blockly.Blocks['for'] = {
  init: function() {
    this.appendValueInput("exp_for1")
        .setCheck(null)
        .appendField("FOR");
    this.appendValueInput("exp_for2")
        .setCheck(null);
    this.appendValueInput("exp_for3")
        .setCheck(null);
    this.appendStatementInput("bloque_for")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//WHILE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#3w2m6p
Blockly.Blocks['while'] = {
  init: function() {
    this.appendValueInput("exp_while")
        .setCheck(null)
        .appendField("WHILE");
    this.appendStatementInput("bloque_while")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//PLAY
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#yxpjtd
Blockly.Blocks['play'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("PLAY")
        .appendField(new Blockly.FieldTextInput("nota"), "nota")
        .appendField(new Blockly.FieldDropdown([["1", "1"], ["2", "2"], ["3", "3"], ["4", "4"]]), "duracion");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//PRINT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#cnjojz
Blockly.Blocks['print'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("PRINT");
    this.appendValueInput("text")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//RETURN
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#p8bb66
Blockly.Blocks['return'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("RETURN");
    this.appendValueInput("text")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//CALL
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#zz7a3u
Blockly.Blocks['call'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("CALL")
        .appendField(new Blockly.FieldTextInput("idFunc"), "idFunc");
    this.appendValueInput("text")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
