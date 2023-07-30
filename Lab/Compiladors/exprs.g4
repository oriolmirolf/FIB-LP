// Gramatica per expressions senzilles
grammar exprs;

root : instruccions EOF ;

instruccions : instruccio* ;

instruccio 
     : assignacio 
     | write 
     | condicial
     | bucle
     ;

condicial: 'if' condicio 'then' instruccions 'end';

bucle: 'while' condicio 'do' instruccions 'end' ;


condicio
     : expr '=' expr     # igualtat
     | expr '<>' expr    # desigualtat
     ;

assignacio : ID ':=' expr ;

write: 'write' expr;

expr : <assoc=right> expr '^' expr    # expressioBinaria
     | expr '/' expr    # expressioBinaria
     | expr '*' expr    # expressioBinaria
     | expr '-' expr    # expressioBinaria
     | expr '+' expr    # expressioBinaria
     | NUM              # numero
     | ID               # identificador
     ;

NUM : [0-9]+ ;

ID: [a-zA-Z]+ ;

WS  : [ \t\n\r]+ -> skip ;