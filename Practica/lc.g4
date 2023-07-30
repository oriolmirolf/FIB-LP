grammar lc;

root 
    : terme 
    | definicioMacro 
    ;

terme 
    : LLETRA                            # Lletra
    | '(' terme ')'                     # termeParentitsat
    | terme terme                       # aplicacio    
    | ('λ' | '\\') capselera '.' terme  # abstraccio
    | MACRO_TERME                       # macroTerme
    | terme MACRO_INFIXE terme          # macroInfixe
    ;

definicioMacro : macro ('≡' | '=') terme ;

capselera : LLETRA+ ;


macro : MACRO_TERME | MACRO_INFIXE ;

MACRO_TERME: [A-Z][A-Z0-9]* ; // Han de començar amb una majuscula i poder seguir per majuscules i xifres

MACRO_INFIXE : [\p{P}\p{S}] ; // Permetem com a macro infixe tots els caràcters de puntuació i símbols.     

LLETRA: [a-z] ;

WS : [ \t\n\r]+ -> skip ;