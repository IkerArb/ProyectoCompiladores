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

goog.provide('Blockly.Din.simples');

goog.require('Blockly.Din');

//PLAY
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#yxpjtd
Blockly.Din['play'] = function(block) {
  var text_nota = block.getFieldValue('nota');
  var dropdown_duracion = block.getFieldValue('duracion');
  // TODO: Assemble Din into code variable.
  var code = 'PLAY(' +text_nota +',' +dropdown_duracion +');';
  return code;
};

//PRINT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#cnjojz
Blockly.Din['print'] = function(block) {
  var value_text = Blockly.Din.valueToCode(block, 'text', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = 'PRINT ' +value_text +';';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//RETURN
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#p8bb66
Blockly.Din['return'] = function(block) {
  var value_text = Blockly.Din.valueToCode(block, 'text', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = 'RETURN (' +value_text +');';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//CALL
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#zz7a3u
Blockly.Din['call'] = function(block) {
  var text_idfunc = block.getFieldValue('idFunc');
  var value_text = Blockly.Din.valueToCode(block, 'text', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble Din into code variable.
  var code = 'CALL ' +text_idfunc +'(' +value_text +');';
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//CALL_VOID
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#zz7a3u
Blockly.Din['call_void'] = function(block) {
  var text_idfunc = block.getFieldValue('idFunc');
  var value_text = Blockly.Din.valueToCode(block, 'text', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = 'CALL ' +text_idfunc +'(' +value_text +');';
  return code;
};

//PARAM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#4qzmzd
Blockly.Din['param'] = function(block) {
  var dropdown_tipo = block.getFieldValue('tipo');
  var text_id = block.getFieldValue('id');
  var value_name = Blockly.Din.valueToCode(block, 'NAME', Blockly.Din.ORDER_ATOMIC);
  // TODO: Assemble JavaScript into code variable.
  var code = dropdown_tipo +' ' +text_id;
  if (value_name != ""){
    code += "," +value_name;
  }
  // TODO: Change ORDER_NONE to the correct strength.
  return code;
};

//+PARAM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#te5oba
Blockly.Din['_param'] = function(block) {
  var value_param1 = Blockly.Din.valueToCode(block, 'param1', Blockly.Din.ORDER_ATOMIC);
  var value_param2 = Blockly.Din.valueToCode(block, 'param2', Blockly.Din.ORDER_ATOMIC);
  var code = value_param1;
  if(value_param2 != ""){
    code += "," +value_param2;
  }
  return code;
};
