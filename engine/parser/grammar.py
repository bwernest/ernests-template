grammar = r"""
%import common.WS             -> WHITESPACE
%import common.SIGNED_NUMBER  -> NUMBER
%import common.FLOAT          -> FLOAT
%import common.INT            -> INT

%ignore WHITESPACE

STRING.1   : /[a-zA-Z0-9\/é,àèêâôδƚƛƜƝƞƟƠơƢƣρƤƥƦƧƨƩƪƫƬƭƮƯưƱƲσγû.+:_*%#-]+/

SUPERSTRING.1 : /[a-zA-Z0-9\/é,àèê''""âôδƚƛƜƝƞƟƠơƢƣρƤƥƦƧƨƩƪƫƬƭƮƯưƱƲσγû.+:_*%#-]+/

APO : /[""]/

VALUE           : APO STRING? (" " STRING+)* APO

PARAMETER.2     : STRING "=" VALUE

BEGIN.3 : "<" | "<?" | "</"
END.3 : ">" | "?>" | "/>"

line    : BEGIN STRING* PARAMETER* END (SUPERSTRING+ BEGIN SUPERSTRING+ END)*

start           : line*
"""
