# Assistente de Apresentações

Kit com três skills que trabalham juntas para transformar qualquer conteúdo (um roteiro simples, tópicos de uma aula, uma palestra, um relatório) em **apresentação pronta + roteiro de fala**, sobre qualquer assunto, no design que você mandar.

| Arquivo | O que faz |
|---|---|
| `assistente-apresentacoes.zip` | O atendimento. Recebe o material e as referências de design, faz as perguntas, monta o plano de slides para você aprovar e distribui o trabalho. |
| `roteiro-apresentacao.zip` | Escreve o que falar em cada slide: tópicos, fala sugerida, tempo, transição e, quando houver dados, a fonte de cada um. |
| `construtor-apresentacoes.zip` | Monta os slides em HTML (para apresentar no navegador) e/ou PowerPoint (para editar no Canva), com as notas do apresentador. |

**Instale as três.** O assistente chama as outras duas pelo nome; sem elas, ele não consegue entregar.

## Como instalar
Cada pessoa instala as três skills na própria conta (skills enviadas ficam privadas para quem enviou):

1. No Claude, abra **Configurações → Capacidades** (*Settings → Capabilities*, se a interface estiver em inglês).
2. Confirme que **Execução de código e criação de arquivos** está ativada.
3. Na seção **Skills**, clique em **Upload skill** e envie um dos arquivos `.zip` da pasta [`kit/`](kit/). Repita para os três.
4. Confira que as três aparecem ativadas na lista de Skills.

Skills estão disponíveis nos planos Pro, Max, Team e Enterprise. Em planos Team e Enterprise, o administrador pode instalar as skills para toda a equipe de uma vez, pelas configurações de administração.

## Como usar
1. Abra uma conversa nova.
2. Anexe o **conteúdo** (roteiro, tópicos, texto ou relatório; também pode só descrever o tema na mensagem) e a **referência de design** (PowerPoint, PDF de slides ou imagens da marca). A referência é opcional; sem ela, o assistente usa um estilo escuro moderno.
3. Peça, por exemplo: *"Use o assistente-apresentacoes para montar uma apresentação a partir deste roteiro, no design deste PowerPoint."* Citar o nome da skill garante que ela seja usada; em algumas versões do Claude também dá para digitar `/assistente-apresentacoes`.
4. Responda as duas perguntas: **duração** da apresentação e **formato** (HTML, PowerPoint ou os dois).
5. Leia o **plano de slides** e aprove ou peça mudanças (ordem, slides a incluir ou tirar, tempo).
6. Receba o deck e o roteiro em documento (e, se ele encontrar, a lista de divergências no material).

## Bom saber
- Os **fatos e números vêm sempre do conteúdo** que você mandou. Textos do PowerPoint de referência servem só como estilo.
- Se você já escreveu a sua fala, ela é mantida: o assistente divide por slide e ajusta só o necessário.
- O assistente avisa quando encontra **divergências** (por exemplo, um número rotulado errado na referência). Corrija na fonte antes de apresentar.
- No deck HTML, a tecla **N** abre as notas do apresentador; no PowerPoint, elas ficam nas anotações de cada slide.
- Para mudar algo depois, peça pelo plano: *"troque a ordem dos slides 4 e 5"*, *"inclua um slide sobre pagamentos"*. Roteiro e deck são atualizados juntos.

## Estrutura do repositório
```
skills/
  assistente-apresentacoes/   # coordena tudo: triagem, perguntas, plano de slides
  roteiro-apresentacao/       # roteiro de fala e notas do apresentador
  construtor-apresentacoes/   # deck em HTML e PowerPoint (Canva)
kit/                          # as três skills empacotadas em .zip, prontas para instalar
```
Para gerar os `.zip` de novo depois de editar uma skill: `cd skills && zip -r ../kit/NOME.zip NOME`.
