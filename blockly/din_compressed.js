// Do not edit this file; automatically generated by build.py.
'use strict';

Blockly.Din=new Blockly.Generator("Din");Blockly.Din.addReservedWords("start,function,void,end,if,else,while,return,print,number,string,bool,list,and,or,not,set,less?,greater?,equals?, different?,color,line,shape,draw,polygon,circle,call,rectangle,point,true,false,elif,var,lambda,delete");Blockly.Din.ORDER_ATOMIC=0;Blockly.Din.ORDER_FUNCTION_CALL=1;Blockly.Din.ORDER_LOGICAL_NOT=2;Blockly.Din.ORDER_MULTIPLICATION=3;Blockly.Din.ORDER_DIVISION=3;Blockly.Din.ORDER_MODULUS=3;
Blockly.Din.ORDER_ADDITION=4;Blockly.Din.ORDER_SUBTRACTION=4;Blockly.Din.ORDER_RELATIONAL=5;Blockly.Din.ORDER_EQUALITY=6;Blockly.Din.ORDER_LOGICAL_AND=7;Blockly.Din.ORDER_LOGICAL_OR=8;Blockly.Din.ORDER_CONDITIONAL=9;Blockly.Din.ORDER_ASSIGNMENT=10;Blockly.Din.ORDER_COMMA=12;Blockly.Din.ORDER_NONE=99;
Blockly.Din.init=function(a){Blockly.Din.definitions_=Object.create(null);Blockly.Din.functionNames_=Object.create(null);Blockly.Din.variableDB_?Blockly.Din.variableDB_.reset():Blockly.Din.variableDB_=new Blockly.Names(Blockly.Din.RESERVED_WORDS_);var b=[];a=Blockly.Variables.allVariables(a);for(var c=0;c<a.length;c++)b[c]="var "+Blockly.Din.variableDB_.getName(a[c],Blockly.Variables.NAME_TYPE)+";";Blockly.Din.definitions_.variables=b.join("\n")};
Blockly.Din.finish=function(a){var b=[],c;for(c in Blockly.Din.definitions_)b.push(Blockly.Din.definitions_[c]);delete Blockly.Din.definitions_;delete Blockly.Din.functionNames_;Blockly.Din.variableDB_.reset();return b.join("\n\n")+"\n\n\n"+a};Blockly.Din.scrubNakedValue=function(a){return a+";\n"};Blockly.Din.quote_=function(a){a=a.replace(/\\/g,"\\\\").replace(/\n/g,"\\\n").replace(/'/g,"\\'");return"'"+a+"'"};
Blockly.Din.scrub_=function(a,b){var c="";if(!a.outputConnection||!a.outputConnection.targetConnection){var d=a.getCommentText();d&&(c+=Blockly.Din.prefixLines(d,"// ")+"\n");for(var e=0;e<a.inputList.length;e++)a.inputList[e].type==Blockly.INPUT_VALUE&&(d=a.inputList[e].connection.targetBlock())&&(d=Blockly.Din.allNestedComments(d))&&(c+=Blockly.Din.prefixLines(d,"// "))}e=a.nextConnection&&a.nextConnection.targetBlock();e=Blockly.Din.blockToCode(e);return c+b+e};
// Copyright 2012 Google Inc.  Apache License 2.0
Blockly.Din.expresiones={};Blockly.Din.lista=function(a){var b=a.getFieldValue("id");a=Blockly.Din.valueToCode(a,"expresion",Blockly.Din.ORDER_ATOMIC);return b+"["+a+"]"};Blockly.Din.num=function(a){return a.getFieldValue("num")};Blockly.Din["var"]=function(a){return a.getFieldValue("id")};Blockly.Din.text=function(a){return'"'+a.getFieldValue("id")+'"'};Blockly.Din.not=function(a){return"NOT "+Blockly.Din.valueToCode(a,"NAME",Blockly.Din.ORDER_ATOMIC)};
Blockly.Din.parentesis=function(a){return"("+Blockly.Din.valueToCode(a,"NAME",Blockly.Din.ORDER_ATOMIC)+")"};Blockly.Din.expresion=function(a){var b=Blockly.Din.valueToCode(a,"op1",Blockly.Din.ORDER_ATOMIC),c=a.getFieldValue("operador");a=Blockly.Din.valueToCode(a,"op2",Blockly.Din.ORDER_ATOMIC);return b+c+a};Blockly.Din["char"]=function(a){return'"'+a.getFieldValue("id")+'"'};Blockly.Din.bool=function(a){return a.getFieldValue("tf")};
Blockly.Din.length=function(a){return Blockly.Din.valueToCode(a,"NAME",Blockly.Din.ORDER_ATOMIC)+".LENGTH()"};Blockly.Din.inicio={};Blockly.Din.programa=function(a){var b=Blockly.Din.statementToCode(a,"vars"),c=Blockly.Din.statementToCode(a,"funciones"),d=a.getFieldValue("tempo");a=Blockly.Din.statementToCode(a,"cancion");return b+"\n"+c+"\nCANCION ("+d+") "+a+"\n"};Blockly.Din.bloque_cancion=function(a){var b=Blockly.Din.statementToCode(a,"vars");a=Blockly.Din.statementToCode(a,"funcs");return b+"\n{\n"+a+"}\n"};
Blockly.Din.bloque_funcion=function(a){var b=a.getFieldValue("id"),c=a.getFieldValue("tipo"),d=Blockly.Din.valueToCode(a,"params",Blockly.Din.ORDER_ATOMIC),e=Blockly.Din.statementToCode(a,"vars");a=Blockly.Din.statementToCode(a,"funcs");return"FUNC "+c+" "+b+"("+d+")"+e+"\n{\n"+a+"}\n"};Blockly.Din.logic={};Blockly.Din["if"]=function(a){var b=Blockly.Din.valueToCode(a,"exp_if",Blockly.Din.ORDER_ATOMIC);a=Blockly.Din.statementToCode(a,"bloque_if");return"IF ("+b+"){\n"+a+"\n};"};Blockly.Din.if_else=function(a){var b=Blockly.Din.valueToCode(a,"exp_if",Blockly.Din.ORDER_ATOMIC),c=Blockly.Din.statementToCode(a,"bloque_if");a=Blockly.Din.statementToCode(a,"bloque_else");return"IF ("+b+"){\n"+c+"\n}\nELSE {\n"+a+"\n};"};
Blockly.Din["for"]=function(a){var b=Blockly.Din.valueToCode(a,"exp_for1",Blockly.Din.ORDER_ATOMIC),c=Blockly.Din.valueToCode(a,"exp_for2",Blockly.Din.ORDER_ATOMIC),d=Blockly.Din.valueToCode(a,"exp_for3",Blockly.Din.ORDER_ATOMIC);a=Blockly.Din.statementToCode(a,"bloque_for");return"FOR ("+b+";"+c+";"+d+";){\n"+a+"\n};"};Blockly.Din["while"]=function(a){var b=Blockly.Din.valueToCode(a,"exp_while",Blockly.Din.ORDER_ATOMIC);a=Blockly.Din.statementToCode(a,"bloque_while");return"WHILE ("+b+"){\n"+a+"\n};"};Blockly.Din.simples={};Blockly.Din.play=function(a){var b=a.getFieldValue("nota");a=a.getFieldValue("duracion");return"PLAY("+b+","+a+");"};Blockly.Din.print=function(a){return"PRINT "+Blockly.Din.valueToCode(a,"text",Blockly.Din.ORDER_ATOMIC)+";"};Blockly.Din["return"]=function(a){return"RETURN ("+Blockly.Din.valueToCode(a,"text",Blockly.Din.ORDER_ATOMIC)+");"};
Blockly.Din.call=function(a){var b=a.getFieldValue("idFunc");a=Blockly.Din.valueToCode(a,"text",Blockly.Din.ORDER_ATOMIC);return"CALL "+b+"("+a+");"};Blockly.Din.call_void=function(a){var b=a.getFieldValue("idFunc");a=Blockly.Din.valueToCode(a,"text",Blockly.Din.ORDER_ATOMIC);return"CALL "+b+"("+a+");"};Blockly.Din.param=function(a){var b=a.getFieldValue("tipo"),c=a.getFieldValue("id");a=Blockly.Din.valueToCode(a,"NAME",Blockly.Din.ORDER_ATOMIC);b=b+" "+c;""!=a&&(b+=","+a);return b};
Blockly.Din._param=function(a){var b=Blockly.Din.valueToCode(a,"param1",Blockly.Din.ORDER_ATOMIC);a=Blockly.Din.valueToCode(a,"param2",Blockly.Din.ORDER_ATOMIC);""!=a&&(b+=","+a);return b};Blockly.Din.variables={};Blockly.Din.variable=function(a){var b=a.getFieldValue("id");a=a.getFieldValue("tipo");return"VAR "+b+" : "+a+";\n"};Blockly.Din.assig_var=function(a){var b=a.getFieldValue("id");a=Blockly.Din.valueToCode(a,"resultado",Blockly.Din.ORDER_ATOMIC);return b+"="+a+";\n"};Blockly.Din.var_lista=function(a){var b=a.getFieldValue("id"),c=a.getFieldValue("tipo");a=Blockly.Din.valueToCode(a,"longitud",Blockly.Din.ORDER_ATOMIC);return"VAR "+b+" : "+c+" LIST("+a+");\n"};
Blockly.Din.assig_lista=function(a){var b=a.getFieldValue("id"),c=Blockly.Din.valueToCode(a,"expresion",Blockly.Din.ORDER_ATOMIC);a=Blockly.Din.valueToCode(a,"resultado",Blockly.Din.ORDER_ATOMIC);return b+"["+c+"] = "+a+";\n"};