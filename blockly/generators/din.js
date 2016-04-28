'use strict';

goog.provide('Blockly.din');

goog.require('Blockly.Generator');

/**
 * Din code generator.
 * @type {!Blockly.Generator}
 */
Blockly.din = new Blockly.Generator('din');

Blockly.din.addReservedWords(
 'start,function,void,end,if,else,while,return,print,number,string,bool,list,and,or,not,set,less?,greater?,equals?, different?,color,line,shape,draw,polygon,circle,call,rectangle,point,true,false,elif,var,lambda,delete'
);

/**
* Order of operation ENUMs.
*/

Blockly.din.ORDER_ATOMIC = 0;
Blockly.din.ORDER_FUNCTION_CALL = 1;
Blockly.din.ORDER_LOGICAL_NOT = 2;
Blockly.din.ORDER_MULTIPLICATION = 3; // *
Blockly.din.ORDER_DIVISION = 3;       // /
Blockly.din.ORDER_MODULUS = 3;        // %
Blockly.din.ORDER_ADDITION = 4;       // +
Blockly.din.ORDER_SUBTRACTION = 4;    // -
Blockly.din.ORDER_RELATIONAL = 5;     // < <= > >=
Blockly.din.ORDER_EQUALITY = 6;       // == != === !==
Blockly.din.ORDER_LOGICAL_AND = 7;      // and
Blockly.din.ORDER_LOGICAL_OR = 8;       // or
Blockly.din.ORDER_CONDITIONAL = 9;      // if else
Blockly.din.ORDER_ASSIGNMENT = 10;    // = += -= *= /= %= <<= >>=
Blockly.din.ORDER_COMMA = 12;         // ,
Blockly.din.ORDER_NONE = 99;          // (...)
/**
* Initialise the database of variable names.
* @param {!Blockly.Workspace} workspace Workspace to generate code from.
*/
Blockly.din.init = function(workspace){
  // Create a dictionary of definitions to be printed before the code.
  Blockly.din.definitions_ = Object.create(null);
  // Create a dictionary mapping desired function names in definitions_
  // to actual function names (to avoid collisions with user functions).
  Blockly.din.functionNames_ = Object.create(null);

  if (!Blockly.din.variableDB_) {
    Blockly.din.variableDB_ =
        new Blockly.Names(Blockly.din.RESERVED_WORDS_);
  } else {
    Blockly.din.variableDB_.reset();
  }

  var defvars = [];
  var variables = Blockly.Variables.allVariables(workspace);
  for (var i = 0; i < variables.length; i++) {
    defvars[i] = 'var ' +
        Blockly.din.variableDB_.getName(variables[i],
        Blockly.Variables.NAME_TYPE) + ';';
  }
  Blockly.din.definitions_['variables'] = defvars.join('\n');
};

/**
 * Prepend the generated code with the variable definitions.
 * @param {string} code Generated code.
 * @return {string} Completed code.
 */
 Blockly.din.finish = function(code) {
   // Convert the definitions dictionary into a list.
   var definitions = [];
   for (var name in Blockly.din.definitions_) {
     definitions.push(Blockly.din.definitions_[name]);
   }
   // Clean up temporary data.
   delete Blockly.din.definitions_;
   delete Blockly.din.functionNames_;
   Blockly.din.variableDB_.reset();
   return definitions.join('\n\n') + '\n\n\n' + code;
 };

 /**
  * Naked values are top-level blocks with outputs that aren't plugged into
  * anything.  A trailing semicolon is needed to make this legal.
  * @param {string} line Line of generated code.
  * @return {string} Legal line of code.
  */
 Blockly.din.scrubNakedValue = function(line) {
   return line + ';\n';
 };

 /**
  * Encode a string as a properly escaped din string, complete with
  * quotes.
  * @param {string} string Text to encode.
  * @return {string} din string.
  * @private
  */
 Blockly.din.quote_ = function(string) {
   // TODO: This is a quick hack.  Replace with goog.string.quote
   string = string.replace(/\\/g, '\\\\')
                  .replace(/\n/g, '\\\n')
                  .replace(/'/g, '\\\'');
   return '\'' + string + '\'';
 };

 /**
  * Common tasks for generating din from blocks.
  * Handles comments for the specified block and any connected value blocks.
  * Calls any statements following this block.
  * @param {!Blockly.Block} block The current block.
  * @param {string} code The din code created for this block.
  * @return {string} din code with comments and subsequent blocks added.
  * @private
  */
 Blockly.din.scrub_ = function(block, code) {
   var commentCode = '';
   // Only collect comments for blocks that aren't inline.
   if (!block.outputConnection || !block.outputConnection.targetConnection) {
     // Collect comment for this block.
     var comment = block.getCommentText();
     if (comment) {
       commentCode += Blockly.din.prefixLines(comment, '// ') + '\n';
     }
     // Collect comments for all value arguments.
     // Don't collect comments for nested statements.
     for (var x = 0; x < block.inputList.length; x++) {
       if (block.inputList[x].type == Blockly.INPUT_VALUE) {
         var childBlock = block.inputList[x].connection.targetBlock();
         if (childBlock) {
           var comment = Blockly.din.allNestedComments(childBlock);
           if (comment) {
             commentCode += Blockly.din.prefixLines(comment, '// ');
           }
         }
       }
     }
   }
   var nextBlock = block.nextConnection && block.nextConnection.targetBlock();
   var nextCode = Blockly.din.blockToCode(nextBlock);
   return commentCode + code + nextCode;
 };
