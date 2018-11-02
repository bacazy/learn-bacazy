import { tokenize, Token } from "./lex/Token";

function compile(source:string) {
    const tokens:Token[] = tokenize(source);
    
}


export function jadex(source: string) {
    return compile(source);
}