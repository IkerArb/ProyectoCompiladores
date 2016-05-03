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

goog.provide('Blockly.Din.inicio');

goog.require('Blockly.Din');

//PROGRAMA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s5s3x5
Blockly.Din['programa'] = function(block) {
  var statements_vars = Blockly.Din.statementToCode(block, 'vars');
  var statements_funciones = Blockly.Din.statementToCode(block, 'funciones');
  var text_tempo = block.getFieldValue('tempo');
  var statements_cancion = Blockly.Din.statementToCode(block, 'cancion');
  // TODO: Assemble Din into code variable.
  var code = statements_vars +'\n' +statements_funciones +'\n' +'CANCION (' +text_tempo +') ' +statements_cancion +'\n';
  return code;
};

//BLOQUE_CANCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#6xrwfx
Blockly.Din['bloque_cancion'] = function(block) {
  var statements_vars = Blockly.Din.statementToCode(block, 'vars');
  var statements_funcs = Blockly.Din.statementToCode(block, 'funcs');
  // TODO: Assemble Din into code variable.
  var code = statements_vars +'\n' +'{\n' +statements_funcs +'}\n';
  return code;
};

//BLOQUE_FUNCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2euwrg
Blockly.Din['bloque_funcion'] = function(block) {
  var text_id = block.getFieldValue('id');
  var dropdown_tipo = block.getFieldValue('tipo');
  var value_params = Blockly.Din.valueToCode(block, 'params', Blockly.Din.ORDER_ATOMIC);
  var statements_vars = Blockly.Din.statementToCode(block, 'vars');
  var statements_funcs = Blockly.Din.statementToCode(block, 'funcs');
  // TODO: Assemble Din into code variable.
  var code = 'FUNC ' +dropdown_tipo +' ' +text_id +'(' +value_params +')' +statements_vars +'\n' +'{\n' +statements_funcs  +'}\n';
  return code;
};
