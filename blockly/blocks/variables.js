/**
 * @license
 * Visual Blocks Editor
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
 * @fileoverview List blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Blocks.variables');

goog.require('Blockly.Blocks');


/**
 * Common HSV hue for all blocks in this category.
 */
Blockly.Blocks.lists.HUE = 260;

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

//ASSIG VAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#9dmjag
Blockly.Blocks['assig_var'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("ASSIG VAR")
        .appendField(new Blockly.FieldTextInput("idVar"), "id");
    this.appendValueInput("resultado")
        .setCheck(null)
        .appendField("=");
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
