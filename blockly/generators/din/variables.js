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

goog.provide('Blockly.Din.variables');

goog.require('Blockly.Din');

//VARIABLE
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#bzj9yt
Blockly.JavaScript['variable'] = function(block) {
  var text_id = block.getFieldValue('id');
  var dropdown_tipo = block.getFieldValue('tipo');
  // TODO: Assemble JavaScript into code variable.
  var code = 'VAR ' +text_id +' : ' +dropdown_tipo ';\n';
  return code;
};

//ASSIG VAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#9dmjag
Blockly.JavaScript['assig_var'] = function(block) {
  var text_id = block.getFieldValue('id');
  var value_resultado = Blockly.JavaScript.valueToCode(block, 'resultado', Blockly.JavaScript.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = text_id +'=' +value_resultado ';\n';
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
