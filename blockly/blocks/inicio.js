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
 * @fileoverview Colour blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Blocks.inicio');

goog.require('Blockly.Blocks');


/**
 * Common HSV hue for all blocks in this category.
 */
Blockly.Blocks.colour.HUE = 20;

//CAT BLOQUES

//PROGRAMA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s5s3x5
Blockly.Blocks['programa'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("PROGRAMA");
    this.appendDummyInput()
        .appendField("VARS");
    this.appendStatementInput("vars")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("FUNCIONES");
    this.appendStatementInput("funciones")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("CANCION")
        .appendField(new Blockly.FieldTextInput("90"), "tempo");
    this.appendStatementInput("cancion")
        .setCheck(null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//BLOQUE_CANCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#6xrwfx
Blockly.Blocks['bloque_cancion'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("VARS CANCION");
    this.appendStatementInput("vars")
        .setCheck(null);
    this.appendDummyInput()
        .appendField("FUNCS CANCION");
    this.appendStatementInput("funcs")
        .setCheck(null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//BLOQUE_FUNCION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2euwrg
Blockly.Blocks['bloque_funcion'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("FUNCION")
        .appendField(new Blockly.FieldTextInput("nombreFunc"), "id")
        .appendField(new Blockly.FieldDropdown([["int", "INT"], ["float", "FLOAT"], ["char", "CHAR"], ["bool", "BOOL"]]), "tipo")
        .appendField("PARAMS");
    this.appendValueInput("params")
        .setCheck(null);
    this.appendStatementInput("vars")
        .setCheck(null)
        .appendField("VARS CANCION");
    this.appendStatementInput("funcs")
        .setCheck(null)
        .appendField("FUNCS CANCION");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
