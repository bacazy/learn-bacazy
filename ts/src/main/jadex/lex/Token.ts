

enum TokenType {
    NUMBER,
    KEYWORD,
    STRING,
    BOOLEAN,
}

interface Token {
    type: TokenType,
    value: string
}

/**
 * 
 * @param source 输入原文本
 */
export function tokenize(source: string){
    let tokens: Token[]  = [];
    return tokens;
}

export {TokenType, Token};