'use strict';

goog.provide('Blockly.Din');

goog.require('Blockly.Generator');

/**
 * Din code generator.
 * @type {!Blockly.Generator}
 */
Blockly.Din = new Blockly.Generator('Din');

Blockly.Din.addReservedWords(
 'start,function,void,end,if,else,while,return,print,number,string,bool,list,and,or,not,set,less?,greater?,equals?, different?,color,line,shape,draw,polygon,circle,call,rectangle,point,true,false,elif,var,lambda,delete'
);

/**
* Order of operation ENUMs.
*/

Blockly.Din.ORDER_ATOMIC = 0;
Blockly.Din.ORDER_FUNCTION_CALL = 1;
Blockly.Din.ORDER_LOGICAL_NOT = 2;
Blockly.Din.ORDER_MULTIPLICATION = 3; // *
Blockly.Din.ORDER_DIVISION = 3;       // /
Blockly.Din.ORDER_MODULUS = 3;        // %
Blockly.Din.ORDER_ADDITION = 4;       // +
Blockly.Din.ORDER_SUBTRACTION = 4;    // -
Blockly.Din.ORDER_RELATIONAL = 5;     // < <= > >=
Blockly.Din.ORDER_EQUALITY = 6;       // == != === !==
Blockly.Din.ORDER_LOGICAL_AND = 7;      // and
Blockly.Din.ORDER_LOGICAL_OR = 8;       // or
Blockly.Din.ORDER_CONDITIONAL = 9;      // if else
Blockly.Din.ORDER_ASSIGNMENT = 10;    // = += -= *= /= %= <<= >>=
Blockly.Din.ORDER_COMMA = 12;         // ,
Blockly.Din.ORDER_NONE = 99;          // (...)
/**
* Initialise the database of variable names.
* @param {!Blockly.Workspace} workspace Workspace to generate code from.
*/
Blockly.Din.init = function(workspace){
  // Create a dictionary of definitions to be printed before the code.
  Blockly.Din.definitions_ = Object.create(null);
  // Create a dictionary mapping desired function names in definitions_
  // to actual function names (to avoid collisions with user functions).
  Blockly.Din.functionNames_ = Object.create(null);

  if (!Blockly.Din.variableDB_) {
    Blockly.Din.variableDB_ =
        new Blockly.Names(Blockly.Din.RESERVED_WORDS_);
  } else {
    Blockly.Din.variableDB_.reset();
  }

  var defvars = [];
  var variables = Blockly.Variables.allVariables(workspace);
  for (var i = 0; i < variables.length; i++) {
    defvars[i] = 'var ' +
        Blockly.Din.variableDB_.getName(variables[i],
        Blockly.Variables.NAME_TYPE) + ';';
  }
  Blockly.Din.definitions_['variables'] = defvars.join('\n');
};

/**
 * Prepend the generated code with the variable definitions.
 * @param {string} code Generated code.
 * @return {string} Completed code.
 */
 Blockly.Din.finish = function(code) {
   // Convert the definitions dictionary into a list.
   var definitions = [];
   for (var name in Blockly.Din.definitions_) {
     definitions.push(Blockly.Din.definitions_[name]);
   }
   // Clean up temporary data.
   delete Blockly.Din.definitions_;
   delete Blockly.Din.functionNames_;
   Blockly.Din.variableDB_.reset();
   return definitions.join('\n\n') + '\n\n\n' + code;
 };

 /**
  * Naked values are top-level blocks with outputs that aren't plugged into
  * anything.  A trailing semicolon is needed to make this legal.
  * @param {string} line Line of generated code.
  * @return {string} Legal line of code.
  */
 Blockly.Din.scrubNakedValue = function(line) {
   return line + ';\n';
 };

 /**
  * Encode a string as a properly escaped Din string, complete with
  * quotes.
  * @param {string} string Text to encode.
  * @return {string} Din string.
  * @private
  */
 Blockly.Din.quote_ = function(string) {
   // TODO: This is a quick hack.  Replace with goog.string.quote
   string = string.replace(/\\/g, '\\\\')
                  .replace(/\n/g, '\\\n')
                  .replace(/'/g, '\\\'');
   return '\'' + string + '\'';
 };

 /**
  * Common tasks for generating Din from blocks.
  * Handles comments for the specified block and any connected value blocks.
  * Calls any statements following this block.
  * @param {!Blockly.Block} block The current block.
  * @param {string} code The Din code created for this block.
  * @return {string} Din code with comments and subsequent blocks added.
  * @private
  */
 Blockly.Din.scrub_ = function(block, code) {
   var commentCode = '';
   // Only collect comments for blocks that aren't inline.
   if (!block.outputConnection || !block.outputConnection.targetConnection) {
     // Collect comment for this block.
     var comment = block.getCommentText();
     if (comment) {
       commentCode += Blockly.Din.prefixLines(comment, '// ') + '\n';
     }
     // Collect comments for all value arguments.
     // Don't collect comments for nested statements.
     for (var x = 0; x < block.inputList.length; x++) {
       if (block.inputList[x].type == Blockly.INPUT_VALUE) {
         var childBlock = block.inputList[x].connection.targetBlock();
         if (childBlock) {
           var comment = Blockly.Din.allNestedComments(childBlock);
           if (comment) {
             commentCode += Blockly.Din.prefixLines(comment, '// ');
           }
         }
       }
     }
   }
   var nextBlock = block.nextConnection && block.nextConnection.targetBlock();
   var nextCode = Blockly.Din.blockToCode(nextBlock);
   return commentCode + code + nextCode;
 };
