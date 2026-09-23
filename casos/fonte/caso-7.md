---
numero: 7
titulo: Alocação de crianças em creches
rotulo: Caso 7 · Alocação de crianças em creches
subtitulo: Caso 7 · modelo de documentação da ABNT NBR ISO/IEC 42005:2025 · versão de oficina 1.1, revisada em 16/09/2026
resumo: Ordena e distribui as vagas de creche pelos critérios de prioridade da norma municipal. Um servidor homologa a lista.
imagem:
alt:
credito:
---
> Documento de simulação para a oficina de Autoavaliação de Impacto Ético (AIE) do Conexão SISP. Caso adaptado da ABNT ISO/IEC TR 24030:2024. O preenchimento é fictício e não descreve um sistema em operação.

## Parte I — O caso de uso, conforme a ISO/IEC TR 24030

### 1.1 Descrição
O sistema ordena e distribui as vagas de creche entre as crianças inscritas. Ele cruza os critérios de prioridade da norma municipal, o endereço da família, a capacidade de cada unidade e as preferências da inscrição. O resultado é uma lista de encaminhamento, no lugar da fila montada à mão em cada unidade.

### 1.2 Retrato do sistema em seis respostas
| Pergunta | Resposta |
| O que o sistema faz, em uma frase? | Ordena e distribui as vagas de creche entre as crianças inscritas. |
| Quem é afetado pela saída dele? | Famílias inscritas, crianças, unidades de ensino e servidores da secretaria. |
| Que dados usa, e de onde vêm? | Cadastro das famílias, marcador de vulnerabilidade do CadÚnico, endereço e capacidade das unidades. |
| A saída é sugestão ou decisão? | Gera a lista de alocação. Um servidor homologa antes da publicação. |
| Em que fase está? | Produção, em uma capital. |
| Quem responde por ele no órgão? | Secretaria municipal de educação. |

### 1.3 Por que este caso importa no Brasil
Mais da metade das redes municipais mantém lista de espera por creche sem critério de prioridade publicado (Gaepe-Brasil, 2024). Sem critério, a fila avança por ordem de inscrição ou por decisão judicial, o que favorece quem tem acesso a advogado. O sistema aplica o que o Gaepe-Brasil recomenda: fila única, transparente e com prioridade para as crianças mais vulneráveis.

## Parte II — Avaliação de impacto preenchida

### 2.1 Escopo e critérios da avaliação (cl. 5)
- **Objeto avaliado:** o componente que ordena e encaminha as vagas, com as regras de prioridade e a interface da secretaria.
- **Fora do escopo:** o cadastro de inscrição das famílias e o sistema de matrícula.
- **Gatilho da avaliação:** sistema em produção que afeta o acesso a um serviço essencial. Refazer quando os critérios mudarem, quando entrarem novas fontes de dados ou a cada 12 meses.
- **Limiar de uso sensível:** mudança que altere a posição relativa dos grupos prioritários exige nova avaliação antes de entrar em produção.

### 2.2 Informações sobre o sistema (cl. 6.2)
| Item | Descrição |
| Finalidade pretendida | Aplicar de forma previsível e rastreável os critérios de prioridade da norma municipal (CF, art. 208, IV; Lei nº 13.257/2016) e reduzir a desigualdade de acesso entre famílias e regiões. |
| Uso pretendido | Apoio à decisão. O sistema produz a lista; um servidor homologa e publica. |
| Usos não pretendidos | Priorizar unidades por conveniência administrativa; abrir exceções fora dos critérios; usar os dados em outra política. |
| Contexto de implantação | Rede municipal de uma capital, com demanda maior que a oferta em parte dos distritos. Cerca de 8.000 candidaturas. |
| Grau de autonomia | Médio. Não há decisão automatizada, mas o servidor não consegue refazer o cálculo. A homologação valida a lista, não o cálculo. |

### 2.3 Informações sobre os dados (cl. 6.3)
- **Origem:** inscrição preenchida pela família, CadÚnico, base de endereços do município e cadastro de capacidade das unidades.
- **Dados pessoais:** nome e data de nascimento da criança, endereço, composição familiar e marcador de vulnerabilidade do CadÚnico. Dados de crianças têm proteção reforçada.
- **Qualidade:** o marcador de vulnerabilidade depende da atualização do CadÚnico, e o endereço declarado pode estar desatualizado. Os dois mudam a posição na fila.
- **Retenção:** dados ativos enquanto a criança estiver na fila e por cinco anos depois, para auditoria.
- **Base legal:** execução de política pública de educação (CF, art. 208, IV; LDB, art. 11, V; Lei nº 13.257/2016; norma municipal de matrícula), com dados de crianças tratados no seu melhor interesse (LGPD, art. 14).

### 2.4 Informações sobre o algoritmo e o modelo (cl. 6.4)
O sistema usa otimização baseada em teoria dos jogos, não uma regra fixa de fila. Ele busca o conjunto de alocações com a melhor pontuação total, considerando prioridade, tempo de espera, distância, preferência declarada e irmãos na mesma unidade. Como a vaga de uma criança depende das preferências das outras, não há posição explicável linha a linha. É IA no sentido da ISO/IEC 22989, que inclui otimização e busca. Os pesos entre os critérios são uma decisão de política pública.

### 2.5 Partes interessadas (cl. 6.6)
| Parte interessada | Interesse no sistema |
| Famílias inscritas | Entender por que a criança foi ou não chamada e poder contestar. |
| Crianças | Acesso à vaga no tempo certo do desenvolvimento. |
| Unidades de ensino | Receber encaminhamentos compatíveis com a capacidade real. |
| Secretaria | Distribuir vaga escassa com critério defensável. |
| Ministério Público e Defensoria | Verificar o cumprimento do direito à educação infantil. |

### 2.6 Benefícios reais e potenciais (cl. 6.7)
- **Para as pessoas:** fila única e consultável, no lugar de listas separadas por unidade.
- **Para a organização:** menos tempo para montar a lista e rastreabilidade de cada encaminhamento.
- **Para a sociedade:** critérios e tamanho da fila publicados por região, o que apoia o planejamento de novas unidades.

### 2.7 Danos reais e potenciais (cl. 6.8)
| Dano | Quem sofre | Como se manifesta |
| Perda de vaga por dado errado | Criança e família | Endereço ou cadastro social desatualizado rebaixa a posição na fila. |
| Desigualdade territorial | Famílias de bairros com menos unidades | O critério de distância favorece quem mora perto de creche. |
| Opacidade da decisão | Família | A negativa chega sem explicar qual critério pesou. |
| Judicialização seletiva | Famílias sem acesso a advogado | Quem aciona a Justiça avança na fila; quem não consegue, não. |
| Dependência acrítica | Servidor | A homologação vira formalidade, e o erro do sistema sai na lista publicada. |

### 2.8 Falhas do sistema e uso indevido previsível (cl. 6.8.3)
- Capacidade das unidades desatualizada, com encaminhamento para vaga inexistente.
- Empate entre crianças com o mesmo critério decidido pela ordem de registro no banco.
- Uso indevido previsível: informar endereço de conveniência para melhorar a posição no critério de distância.
- Uso indevido previsível: reaproveitar os dados de vulnerabilidade das famílias para outra finalidade, sem nova base legal.

### 2.9 Verificação por tema de documentação (cl. 6)
| Tema | Situação hoje | O que falta |
| Responsabilização | Há responsável formal na secretaria. | Registrar quem aprova mudanças de critério e em que ato. |
| Transparência | Critérios publicados em norma. | Publicar, com a chamada, o critério que determinou a posição. |
| Equidade | Critérios de vulnerabilidade aplicados na ordenação. A secretaria acompanha o tempo de espera por critério. | Publicar o tempo médio de espera por região e por perfil. |
| Privacidade | Base legal definida. | Revisar a retenção e restringir o acesso ao marcador do CadÚnico. |
| Confiabilidade | O resultado depende dos pesos e da configuração da otimização. Não é reproduzível à mão. | Publicar a função de pontuação e os pesos, com casos de referência para teste a cada mudança. |
| Segurança | Acesso por perfil. | Registro de auditoria das alterações manuais de posição na fila. |
| Explicabilidade | Critérios conhecidos, mas o resultado não é rastreável caso a caso. | Explicação em linguagem simples no comprovante da família. |
| Impacto ambiental | Não significativo. | Sem ação. |

### 2.10 Medidas de tratamento de riscos
| Medida | Responsável | Prazo |
| Publicar a explicação do critério aplicado em cada encaminhamento | Coordenação de educação infantil | 90 dias |
| Painel público de tempo de espera por distrito e faixa etária | Equipe de dados da secretaria | 120 dias |
| Canal de contestação com prazo de resposta declarado | Ouvidoria | 60 dias |
| Teste de regressão obrigatório antes de mudar peso de critério | Fornecedor e equipe de TI | A cada versão |
| Revisão anual dos critérios com participação de conselhos | Secretaria | Anual |

### 2.11 Risco residual
O que permanece depois das medidas previstas:
- **Perda de vaga por dado errado:** nenhuma medida trata da atualização do CadÚnico nem da conferência do endereço.
- **Desigualdade territorial:** o painel mede a desigualdade, mas não muda o peso da distância, que a produz.
- **Opacidade da decisão:** publicar o critério não reconstrói a posição de cada criança, que depende das preferências das demais.
- **Judicialização seletiva:** o canal de contestação depende de a família saber que pode contestar.
- **Dependência acrítica:** o servidor homologa sem poder refazer o cálculo, e nenhuma medida cria um meio de discordar da lista.
- **Encaminhamento para vaga inexistente:** nenhuma medida prevê alerta quando a capacidade cadastrada divergir da real.
