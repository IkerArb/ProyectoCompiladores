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
 * @fileoverview Logic blocks for Blockly.
 * @author q.neutron@gmail.com (Quynh Neutron)
 */
'use strict';

goog.provide('Blockly.Blocks.logic');

goog.require('Blockly.Blocks');


/**
 * Common HSV hue for all blocks in this category.
 */
Blockly.Blocks.logic.HUE = 210;

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
