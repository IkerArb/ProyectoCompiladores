/**
 * @license
 * Visual Blocks Language
 *
 * Copyright 2012 Google Inc.
 * https://developers.google.com/blockly/
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * @fileoverview Generating Din for colour blocks.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Din.expresiones');

goog.require('Blockly.Din');

//LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#25ah7o
Blockly.Din['lista'] = function(block) {
  var text_id = block.getFieldValue('id');
  var value_expresion = Blockly.Din.valueToCode(block, 'expresion', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = text_id +'[' +value_expresion +']';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//NUM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.Din['num'] = function(block) {
  var text_num = block.getFieldValue('num');
  // TODO: Assemble Din into code variable.
  var code = text_num;
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//VAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.Din['var'] = function(block) {
  var text_id = block.getFieldValue('id');
  // TODO: Assemble Din into code variable.
  var code = text_id;
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//TEXT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#if2eus
Blockly.Din['text'] = function(block) {
  var text_id = block.getFieldValue('id');
  // TODO: Assemble JavaScript into code variable.
  var code = '"' +text_id +'"';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//NOT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#azhtpw
Blockly.Din['not'] = function(block) {
  var value_name = Blockly.Din.valueToCode(block, 'NAME', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = 'NOT ' +value_name;
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//PARENTESIS
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#iu4dcw
Blockly.Din['parentesis'] = function(block) {
  var value_name = Blockly.Din.valueToCode(block, 'NAME', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = '(' +value_name +')';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//EXPRESION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2rrkzb
Blockly.Din['expresion'] = function(block) {
  var value_op1 = Blockly.Din.valueToCode(block, 'op1', Blockly.Din.ORDER_ATOMIC);
  var dropdown_operador = block.getFieldValue('operador');
  var value_op2 = Blockly.Din.valueToCode(block, 'op2', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = value_op1 +dropdown_operador +value_op2;
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//CHAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#anddbd
Blockly.Din['char'] = function(block) {
  var text_id = block.getFieldValue('id');
  // TODO: Assemble JavaScript into code variable.
  var code = "\""+text_id+"\"";
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//BOOL
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#i69oay
Blockly.Din['bool'] = function(block) {
  var dropdown_tf = block.getFieldValue('tf');
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_tf;
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//LENGTH
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#sormmf
Blockly.Din['length'] = function(block) {
  var value_name = Blockly.Din.valueToCode(block, 'NAME', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = value_name +'.LENGTH()';
  return code;
};
