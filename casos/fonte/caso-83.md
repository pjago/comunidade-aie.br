---
numero: 83
titulo: Correção automatizada de redação em exame público de larga escala
rotulo: Caso 83 · Correção automatizada de redação
subtitulo: Caso 83 · modelo de documentação da ABNT NBR ISO/IEC 42005:2025 · versão de oficina 1.0, 18/09/2026
resumo: Atribui a nota da redação a partir da folha manuscrita digitalizada. A maioria dos textos não tem segunda correção humana; uma amostra é comparada com corretores.
imagem:
alt:
credito:
---
> Documento de simulação para a oficina de Autoavaliação de Impacto Ético (AIE) do Conexão SISP. Caso adaptado da ABNT ISO/IEC TR 24030:2024. O preenchimento é fictício e não descreve um sistema em operação.

## Parte I — O caso de uso, conforme a ISO/IEC TR 24030

### 1.1 Descrição
O sistema corrige a redação de um exame público de larga escala a partir da folha manuscrita digitalizada. Ele dá uma nota a cada critério e uma nota final, com um padrão único para todos os candidatos. Uma amostra das correções é comparada com a correção humana, para controle de qualidade. O texto também é verificado quanto a cópia. A nota entra diretamente na classificação do exame; a maioria dos textos não tem segunda correção humana.

### 1.2 Retrato do sistema em seis respostas
| Pergunta | Resposta |
| O que o sistema faz, em uma frase? | Atribui nota à redação de um exame público, a partir do texto digitalizado da folha manuscrita. |
| Quem é afetado pela saída dele? | Candidatos, avaliadores humanos e a instituição responsável pela classificação. |
| Que dados usa, e de onde vêm? | Imagem digitalizada da folha manuscrita e o texto reconhecido a partir dela. |
| A saída é sugestão ou decisão? | Atribui a nota que compõe a classificação. Não há segunda correção humana da maioria dos textos. |
| Em que fase está? | Produção. |
| Quem responde por ele no órgão? | Instituição responsável pela organização do exame. |

### 1.3 Por que este caso importa no Brasil
Exame de larga escala significa alto volume em prazo curto: o Enem teve mais de três milhões de inscritos em anos recentes. Hoje cada redação passa por dois corretores humanos, com um terceiro em caso de divergência. A correção automatizada promete padronização e velocidade. Mas a nota de redação decide vaga em universidade pública, financiamento estudantil e, em concursos, o acesso ao cargo. Quem discorda da nota precisa saber por qual critério ela foi dada.

## Parte II — Avaliação de impacto preenchida

### 2.1 Escopo e critérios da avaliação (cl. 5)
- **Objeto avaliado:** o modelo de correção, o padrão de pontuação por critério e a amostragem de controle de qualidade.
- **Fora do escopo:** a digitalização das folhas e o sistema de inscrição e convocação.
- **Gatilho da avaliação:** sistema em produção cuja saída entra diretamente na classificação. Reavaliar a cada retreinamento, a cada mudança no padrão de pontuação ou a cada edição do exame.
- **Limiar de uso sensível:** reduzir o percentual de textos com segunda correção humana exige nova avaliação e decisão formal da autoridade do exame.

### 2.2 Informações sobre o sistema (cl. 6.2)
| Item | Descrição |
| Finalidade pretendida | Aplicar os critérios de avaliação da redação de forma padronizada e em grande volume, com menos tempo e custo de correção humana. |
| Uso pretendido | Correção principal de todos os textos, com verificação por amostragem contra a correção humana. |
| Usos não pretendidos | Usar a nota para outra finalidade; mudar o padrão de pontuação sem nova avaliação; dispensar a correção humana por amostragem. |
| Contexto de implantação | Exame público de larga escala, com redação manuscrita digitalizada. |
| Grau de autonomia | Alto. O sistema dá a nota que entra na classificação. A correção humana alcança só uma amostra. |

### 2.3 Informações sobre os dados (cl. 6.3)
- **Origem:** imagem digitalizada da folha de redação, produzida na aplicação do exame.
- **Dados pessoais:** o texto não é identificado ao candidato durante a correção, por desenho do processo. A caligrafia pode permitir identificação indireta se a imagem vazar.
- **Qualidade:** letra pouco legível, rasura e mudança de tinta ou de caligrafia degradam o reconhecimento e podem afetar a nota.
- **Retenção:** imagens e notas guardadas pelo prazo do recurso e da auditoria do exame.
- **Base legal:** execução de política pública de avaliação e seleção em exame público, com tratamento limitado à correção e à classificação.

### 2.4 Informações sobre o algoritmo e o modelo (cl. 6.4)
Modelo de processamento de linguagem natural e aprendizado profundo. Ele reconhece o texto manuscrito e avalia critérios como coerência, coesão, norma culta e atendimento ao tema. Também sinaliza trechos muito parecidos com conteúdo já publicado. A nota final combina as notas por critério, com pesos definidos antes. Quando a nota diverge da que um avaliador daria, a causa pode estar no reconhecimento do texto, na avaliação de um critério ou nos pesos, e essas três fontes não aparecem separadas na nota final.

### 2.5 Partes interessadas (cl. 6.6)
| Parte interessada | Interesse no sistema |
| Candidatos ao exame | Receber uma nota que reflita o texto e poder contestar com base em critério claro. |
| Avaliadores humanos | Clareza sobre o novo papel: corrigir a amostra de controle, não a maioria dos textos. |
| Instituição responsável pelo exame | Sustentar a nota em recurso administrativo e em contestação judicial. |
| Universidades e órgãos que usam a nota | Confiar que a nota reflete o desempenho do candidato. |
| Órgãos de controle e Defensoria | Verificar a igualdade de tratamento entre candidatos. |

### 2.6 Benefícios reais e potenciais (cl. 6.7)
- **Para as pessoas:** padrão único de pontuação, sem a variação entre avaliadores humanos.
- **Para a organização:** menos custo e tempo de correção, e resultado divulgado mais cedo.
- **Para a sociedade:** exame em maior escala, com menor custo por candidato.

### 2.7 Danos reais e potenciais (cl. 6.8)
| Dano | Quem sofre | Como se manifesta |
| Nota que não reflete o texto | Candidato | O reconhecimento da caligrafia falha, ou a avaliação de um critério discorda do que um leitor humano concluiria. |
| Recurso sem informação para sustentá-lo | Candidato | O candidato não sabe qual critério pesou na nota. |
| Padronização que penaliza estilo legítimo | Candidato com escrita fora do padrão mais comum | Oralidade, forma de argumentar ou repertório pouco frequente no treinamento são lidos como desvio. |
| Falso indício de cópia | Candidato | Sinalização de plágio por repertório ou expressão comum ao tema, não por cópia. |
| Perda de capacidade de correção humana | Instituição do exame | Com a correção humana reduzida a uma amostra, a instituição perde a capacidade de corrigir em escala sem o sistema. |

### 2.8 Falhas do sistema e uso indevido previsível (cl. 6.8.3)
- Queda de desempenho não detectada em digitalização ruim, letra difícil de ler ou caneta fora do padrão.
- Divergência entre nota automatizada e humana na amostra, sem apurar a causa em cada texto.
- Uso indevido previsível: reduzir a correção humana para acelerar o resultado, sem nova avaliação.
- Uso indevido previsível: usar o sinalizador de cópia como prova de fraude, sem revisão humana.

### 2.9 Verificação por tema de documentação (cl. 6)
| Tema | Situação hoje | O que falta |
| Responsabilização | A instituição do exame responde pela nota. | Registrar, para cada nota contestada, se ela veio da correção automatizada ou da amostra humana. |
| Transparência | Critérios publicados no edital. | Publicar para o candidato a nota por critério, não só a final. |
| Equidade | A amostra humana mede a acurácia geral. | Medir a divergência entre nota automatizada e humana por perfil de escrita, região e tipo de escola. |
| Privacidade | Correção sem identificação nominal do candidato. | Avaliar o risco de identificação pela caligrafia em caso de acesso indevido à imagem. |
| Confiabilidade | A amostra humana mede a acurácia geral. | Publicar a divergência entre nota automatizada e humana, sem agregar tudo em uma média única. |
| Segurança | Acesso restrito às imagens. | Trilha de auditoria do acesso à imagem e à nota de cada candidato. |
| Explicabilidade | Só a nota final é divulgada. | Entregar a nota por critério com a nota final, no boletim. |
| Impacto ambiental | Processamento em lote, concentrado no período de correção. | Estimar o consumo do processamento de milhões de textos em pouco tempo. |

### 2.10 Medidas de tratamento
| Medida | Responsável | Prazo |
| Publicar a nota por critério junto com a nota final | Coordenação do exame | 90 dias |
| Medir e publicar a divergência entre nota automatizada e humana por perfil de escrita e por região | Equipe de avaliação e estatística | 180 dias |
| Canal de recurso com acesso à nota por critério antes do prazo de contestação | Ouvidoria do exame | 90 dias |
| Revisão humana obrigatória de todo caso sinalizado como possível cópia, antes de qualquer consequência | Coordenação de integridade do exame | Imediato |
| Definir e publicar o percentual mínimo de correção humana por amostragem, sem redução sem nova avaliação | Instituição responsável pelo exame | 60 dias |

### 2.11 Risco residual
O que permanece depois das medidas previstas:
- **Nota que não reflete o texto:** a nota por critério explica a nota, mas não corrige o erro de reconhecimento ou de avaliação.
- **Recurso sem informação para sustentá-lo:** o recurso ganha a nota por critério, mas o candidato ainda não vê o texto com as marcações do avaliador.
- **Padronização que penaliza estilo legítimo:** medir a divergência por perfil identifica o problema, mas não muda o padrão de pontuação nem os dados de treinamento.
- **Falso indício de cópia:** a revisão humana reduz a consequência indevida, mas o texto continua sinalizado até a revisão.
- **Perda de capacidade de correção humana:** nenhuma medida mantém a capacidade de corrigir em escala além da amostra.

Fonte: adaptado da ABNT ISO/IEC TR 24030:2024, caso de uso 83, “Um sistema de correção inteligente”.
