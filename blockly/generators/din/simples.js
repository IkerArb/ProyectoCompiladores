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

goog.provide('Blockly.Din.simples');

goog.require('Blockly.Din');

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
