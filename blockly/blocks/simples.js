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
 * @fileoverview Loop blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Blocks.simples');

goog.require('Blockly.Blocks');


/**
 * Common HSV hue for all blocks in this category.
 */
Blockly.Blocks.simples.HUE = 120;

//PLAY
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#yxpjtd
Blockly.Blocks['play'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("PLAY")
        .appendField(new Blockly.FieldTextInput("nota"), "nota")
        .appendField(new Blockly.FieldDropdown([["1", "4"], [".5","8"], ["2", "3"], ["3", "2"], ["4", "1"]]), "duracion");
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
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
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
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
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

//CALL_VOID
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#zz7a3u
Blockly.Blocks['call_void'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("CALL_VOID")
        .appendField(new Blockly.FieldTextInput("idFunc"), "idFunc");
    this.appendValueInput("text")
        .setCheck(null);
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//PARAM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#4qzmzd
Blockly.Blocks['param'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("PARAM")
        .appendField(new Blockly.FieldDropdown([["int", "INT"], ["float", "FLOAT"], ["char", "char"], ["bool", "OPTIONNAME"]]), "tipo")
        .appendField(new Blockly.FieldTextInput("idVar"), "id");
    this.setInputsInline(false);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//+PARAM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#te5oba
Blockly.Blocks['_param'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("+PARAM");
    this.appendValueInput("param1")
        .setCheck(null);
    this.appendValueInput("param2")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
