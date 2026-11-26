# Comparação: Python x Java

As duas versões fazem exatamente a mesma coisa e chegaram aos mesmos resultados (inclusive o valor total do estoque, 1705.0). A diferença está na forma de escrever cada uma.

**Tamanho do código:** o Python ficou mais curto e direto. No Java é preciso escrever mais, porque cada valor enviado ao banco é informado um por um, junto com o seu tipo (texto, número inteiro, número decimal).

**Como as plantas voltam do banco:** no Python cada planta vem como uma sequência simples de valores (id, nome, espécie, preço, estoque). No Java cada planta vira um objeto `Planta`, o que deixa o código mais organizado, mas dá mais trabalho para montar.

**Salvar as alterações:** no Python é preciso confirmar (`commit`) toda vez que se insere, altera ou remove algo; se esquecer, a mudança se perde. No Java isso é feito automaticamente.

**Resultado da inserção:** o Python devolve o número (id) da planta nova. O Java só informa se deu certo ou não.

**Preparação do ambiente:** no Python é preciso criar o ambiente virtual e instalar o conector manualmente. No Java o Maven baixa o conector sozinho a partir do `pom.xml`, mas é necessário ter o JDK e, de preferência, uma IDE como o IntelliJ.

**Exibição dos preços:** o Python mostra os preços com ponto (12.50), e o Java mostra com vírgula (12,50), porque segue o idioma configurado no computador.

**Segurança:** nas duas versões os valores são passados como parâmetros (`%s` no Python e `?` no Java), sem montar o comando juntando texto. Isso evita que alguém consiga alterar o comando enviado ao banco.

**Conclusão:** o Python é mais rápido de escrever e bom para tarefas pequenas. O Java exige mais código, mas é mais rígido e organizado, o que ajuda em projetos maiores, já que muitos erros aparecem antes mesmo de o programa rodar.
