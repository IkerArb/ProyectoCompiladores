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
 * @fileoverview Generating JavaScript for colour blocks.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Din.logic');

goog.require('Blockly.Din');

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
