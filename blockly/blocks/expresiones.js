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
 * @fileoverview Text blocks for Blockly.
 * @author fraser@google.com (Neil Fraser)
 */
'use strict';

goog.provide('Blockly.Blocks.expresiones');

goog.require('Blockly.Blocks');


/**
 * Common HSV hue for all blocks in this category.
 */
Blockly.Blocks.expresiones.HUE = 999;

//LISTA
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#25ah7o
Blockly.Blocks['lista'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("LISTA")
        .appendField(new Blockly.FieldTextInput("idLista"), "id");
    this.appendValueInput("expresion")
        .setCheck(null)
        .appendField("[");
    this.appendDummyInput()
        .appendField("]");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//NUM
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.Blocks['num'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NUM")
        .appendField(new Blockly.FieldTextInput("numero"), "num");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


//VAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#s545wp
Blockly.Blocks['var'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("VAR")
        .appendField(new Blockly.FieldTextInput("idVar"), "id");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//NOT
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#azhtpw
Blockly.Blocks['not'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("NOT");
    this.appendValueInput("NAME")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//PARENTESIS
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#iu4dcw
Blockly.Blocks['parentesis'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("(");
    this.appendValueInput("NAME")
        .setCheck(null);
    this.appendDummyInput()
        .appendField(")");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//EXPRESION
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#2rrkzb
Blockly.Blocks['expresion'] = {
  init: function() {
    this.appendValueInput("op1")
        .setCheck(null);
    this.appendValueInput("op2")
        .setCheck(null)
        .appendField(new Blockly.FieldDropdown([["=", "="], ["+", "+"], ["-", "-"], ["*", "*"], ["/", "/"], ["AND", "AND"], ["OR", "OR"], ["==", "=="], ["!=", "!="], [">", ">"], ["<", "<"], [">=", ">="], ["<=", "<="]]), "operador");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//CHAR
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#anddbd
Blockly.Blocks['char'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("CHAR")
        .appendField(new Blockly.FieldTextInput("texto"), "id");
    this.appendDummyInput();
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


//BOOL
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#i69oay
Blockly.Blocks['bool'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("BOOL")
        .appendField(new Blockly.FieldDropdown([["true", "True"], ["false", "False"]]), "tf");
    this.appendDummyInput();
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

//LENGTH
//https://blockly-demo.appspot.com/static/demos/blockfactory/index.html#sormmf
Blockly.Blocks['length'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("LENGTH");
    this.appendValueInput("NAME")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
