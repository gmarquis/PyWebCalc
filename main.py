import html, json
import numpy as np
from math import sqrt
from js import document

pyscript.write('display2', 0)       ## determines calculator, nearly loaded/ready.

def string_to_function(expression):
    def function(x):
        return eval(expression)
    return np.frompyfunc(function, 1, 1)

def cancel(*args, **kwargs):
    result = '0'
    pyscript.write('display1', '')
    pyscript.write('display2', result)
    pyscript.write('memory1', result)

def delete(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result = result[:-1]
    if len(result) == 0:
        result = '0'
    pyscript.write('display2', result)

def equ(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    my_function = string_to_function(result)
    pyscript.write('display2', my_function(result))

def one(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '1'
    else:
        result += '1'
    pyscript.write('display2', result)

def two(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '2'
    else:
        result += '2'
    pyscript.write('display2', result)

def three(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '3'
    else:
        result += '3'
    pyscript.write('display2', result)

def zero(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        pass
    else:
        result += '0'
    pyscript.write('display2', result)

def plus(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += '+'
    pyscript.write('display2', result)

def mns(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += '-'
    pyscript.write('display2', result)

def over(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += '/'
    pyscript.write('display2', result)

def pwr(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += '**'
    pyscript.write('display2', result)

def mlt(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += '*'
    pyscript.write('display2', result)

def four(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '4'
    else:
        result += '4'
    pyscript.write('display2', result)
    
def five(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '5'
    else:
        result += '5'
    pyscript.write('display2', result)
    
def six(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '6'
    else:
        result += '6'
    pyscript.write('display2', result)
    
def svn(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '7'
    else:
        result += '7'
    pyscript.write('display2', result)
    
def eight(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '8'
    else:
        result += '8'
    pyscript.write('display2', result)

def nine(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '9'
    else:
        result += '9'
    pyscript.write('display2', result)
    
def sqr(*args, **kwargs):
    result = int(Element('display2').element.innerText)
    result = float(sqrt(result)) 
    result = str(float("%0.4f" % (result)))
    pyscript.write('display2', result)

def dp(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if '.' not in result:
        result += '.'
        pyscript.write('display2', result)

def bin(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result = int(result)
    result = np.binary_repr(result)                         ## dec to bin
    result += 'b'
    pyscript.write('display2', "")
    pyscript.write('display1', str(result))

def hex(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result = int(result)
    result = np.base_repr(result, base=16)                  ## dec to hex
    result += 'h'
    pyscript.write('display2', "")
    pyscript.write('display1', str(result))

def dec(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result > '':
        result = int(result, 16)                            ## hex to dec
        pyscript.write('display2', str(result))
        pyscript.write('display1', '')
    result = str(Element('display1').element.innerText)
    if result[-1] == 'h':
            result = result[:-1]
            result = int(result, 16)                        ## hex to dec
            pyscript.write('display1', str(result))
    else:
        if result[-1] == 'b':
            result = result[:-1]
            result = int(result, 2)                         ## bin to dec
            pyscript.write('display1', str(result))

def x2(*args, **kwargs):
    result = int(Element('display2').element.innerText)
    result = result**2
    pyscript.write('display2', '')
    pyscript.write('display2', result)

def x3(*args, **kwargs):
    result = int(Element('display2').element.innerText)
    result = result**3
    pyscript.write('display2', '')
    pyscript.write('display2', result)

def pi(*args, **kwargs):
    result = int(Element('display2').element.innerText)
    result = 3.14*result
    if result == 0.0:
        result = 3.14
    pyscript.write('display2', result)

def bo(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += '('
    pyscript.write('display2', result)

def bc(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    result += ')'
    pyscript.write('display2', result)

def mr(*args, **kwargs):
    memory = int(Element('memory1').element.innerText)
    pyscript.write('display1', str(memory))

def mp(*args, **kwargs):
    result = int(Element('display2').element.innerText)
    memory = int(Element('memory1').element.innerText)
    memory += result
    pyscript.write('memory1', str(memory))
    pyscript.write('display2', '0')

def ms(*args, **kwargs):
    result = int(Element('display2').element.innerText)
    memory = int(Element('memory1').element.innerText)
    memory -= result
    pyscript.write('memory1', str(memory))
    pyscript.write('display2', '0')

def hexa(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '' ; result += 'A'
    else:
        result += 'A'
    pyscript.write('display2', result)

def hexb(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '' ; result += 'B'
    else:
        result += 'B'
    pyscript.write('display2', result)

def hexc(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '' ; result += 'C'
    else:
        result += 'C'
    pyscript.write('display2', result)

def hexd(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '' ; result += 'D'
    else:
        result += 'D'
    pyscript.write('display2', result)

def hexe(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '' ; result += 'E'
    else:
        result += 'E'
    pyscript.write('display2', result)

def hexf(*args, **kwargs):
    result = str(Element('display2').element.innerText)
    if result == '0':
        result = '' ; result += 'F'
    else:
        result += 'F'
    pyscript.write('display2', result)
