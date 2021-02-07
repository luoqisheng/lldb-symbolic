#!/usr/bin/python

import lldb
import fbchisellldbbase as fb

def lldbcommands():
  return [ SymbolicAddresses() ]
  
class SymbolicAddresses(fb.FBCommand):
  def name(self):
    return 'symbolic'
    
  def description(self):
    return 'symbolic addresses'
    
  def run(self, arguments, options):
    # It's a good habit to explicitly cast the type of all return
    # values and arguments. LLDB can't always find them on its own.
    interpreter = lldb.debugger.GetCommandInterpreter()
    line = -1
    for arg in arguments[1:]:
      line = line + 1
      object = lldb.SBCommandReturnObject()
      arg = arg.strip()
      interpreter.HandleCommand('image lookup -a {}'.format(arg), self.context, object)
      if object.GetOutput():
        print(object.GetOutput().strip().splitlines()[1].replace('Summary:', 'frame #{}: {}'.format(line, arg)), file=self.result)
