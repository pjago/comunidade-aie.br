---
numero: 29
titulo: Fiscalização de trânsito por vídeo
rotulo: Caso 29 · Fiscalização de trânsito por vídeo
subtitulo: Caso 29 · modelo de documentação da ABNT NBR ISO/IEC 42005:2025 · versão de oficina 1.0, 12/08/2026
resumo: Detecta indícios de infração em imagens de câmeras de via e seleciona cenas para um agente validar antes do auto de infração.
imagem:
alt:
credito:
---
> Documento de simulação para a oficina de Autoavaliação de Impacto Ético (AIE) do Conexão SISP. Caso adaptado da ABNT ISO/IEC TR 24030:2024. O preenchimento é fictício e não descreve um sistema em operação.

## O sistema de IA, conforme a ISO/IEC TR 24030

### 1.1 Descrição
O sistema analisa imagens de câmeras de via para detectar indícios de infração, como falta de cinto, celular ao volante, conversão proibida e uso de faixa exclusiva. Também mede o fluxo de veículos. As cenas suspeitas vão para um agente de trânsito, que valida ou descarta cada uma antes do auto de infração.

### 1.2 Descrição do sistema em quatro respostas
| Pergunta | Resposta |
| O que o sistema faz, em uma frase? | Analisa imagens de câmeras de via para detectar infrações e medir o fluxo. |
| Quem é afetado pela saída dele? | Condutores autuados, pedestres e agentes de trânsito. |
| Que dados usa, e de onde vêm? | Vídeo de via pública, leitura de placas e base de veículos. |
| A saída é sugestão ou decisão? | Sugere a autuação. Um agente valida antes da emissão. |

## Avaliação de impacto, conforme a ISO/IEC 42005:2025

### 2.1 Escopo e critérios da avaliação (cl. 5)
- **Objeto avaliado:** o módulo de visão computacional que pré-seleciona cenas, a fila de validação do agente e o conteúdo da notificação ao autuado.
- **Fora do escopo:** a cobrança de multas e o parque de câmeras contratado.
- **Gatilho da avaliação:** sistema em produção com efeito sancionatório. Reavaliar a cada versão do modelo, a cada infração nova detectada e sempre que a taxa de descarte na validação variar mais de cinco pontos percentuais entre trimestres.
- **Limiar de uso sensível:** dispensar a validação humana antes da autuação exige nova avaliação e decisão formal da autoridade.

### 2.2 Informações sobre o sistema (cl. 6.2)
| Item | Descrição |
| Finalidade pretendida | Ampliar a fiscalização de condutas de risco e reduzir acidentes. |
| Uso pretendido | Triagem: separar as cenas suspeitas do fluxo total para análise humana. |
| Usos não pretendidos | Autuação automática sem validação; rastreamento de pessoa determinada; uso das imagens para outra finalidade de segurança pública. |
| Contexto de implantação | Vias urbanas e rodovias com câmeras fixas de alta resolução. |
| Grau de autonomia | Médio. O sistema não autua, mas define o que o agente vê e o que ele nunca verá. |

### 2.3 Informações sobre os dados (cl. 6.3)
- **Origem:** vídeo contínuo de via pública, leitura automática de placas (ALPR) e base de veículos.
- **Dados pessoais:** imagem de condutor e passageiro, placa e vínculo com o proprietário. São dados pessoais, não sensíveis (LGPD, art. 11). A imagem do rosto não é usada para identificar a pessoa; quem é identificado é o veículo.
- **Qualidade:** o desempenho cai à noite, com chuva, com película nos vidros e com placas sujas ou danificadas.
- **Retenção:** imagens sem indício de infração devem ser descartadas em prazo curto e declarado. As demais seguem o prazo do processo administrativo.
- **Base legal:** competência de fiscalização de trânsito, com os limites da LGPD para órgãos públicos.

### 2.4 Informações sobre o algoritmo e o modelo (cl. 6.4)
Modelos de visão computacional treinados para reconhecer padrões de infração. O ponto crítico é a distribuição do erro, não a acurácia média. O falso positivo gera autuação indevida. O falso negativo não gera reclamação e passa despercebido. Sem medir os dois separadamente, o órgão enxerga só metade do impacto.

### 2.5 Partes interessadas (cl. 6.6)
| Parte interessada | Interesse no sistema |
| Condutores | Não ser autuado por erro e poder se defender com a prova em mãos. |
| Pedestres e ciclistas | Redução real das condutas de risco na via. |
| Agentes de trânsito | Fila de validação em volume que permita analisar cada cena. |
| Órgão de trânsito | Sustentar a autuação em processo administrativo e judicial. |
| Fornecedor | Manutenção e evolução do modelo. |

### 2.6 Benefícios reais e potenciais (cl. 6.7)
- **Para as pessoas:** fiscalização de condutas antes flagradas só por acaso, como celular ao volante.
- **Para a organização:** a câmera opera sem parar e separa, entre milhares de veículos, só as cenas suspeitas.
- **Para a sociedade:** dados de fluxo para a engenharia de tráfego.

### 2.7 Danos reais e potenciais (cl. 6.8)
| Dano | Quem sofre | Como se manifesta |
| Autuação indevida | Condutor | Falso positivo validado por agente sobrecarregado. |
| Custo de defesa desigual | Condutor de baixa renda | Recorrer exige tempo, acesso digital e, às vezes, advogado. |
| Vigilância excessiva | Qualquer pessoa na via | Captura contínua de imagem do interior do veículo. |
| Desvio de finalidade | População monitorada | Uso das imagens e das placas para rastreamento não previsto. |
| Validação de fachada | Condutor e órgão | O volume alto transforma a análise humana em confirmação automática. |

### 2.8 Falhas do sistema e uso indevido previsível (cl. 6.8.3)
- Queda de desempenho não detectada após troca de lente ou mudança de ângulo ou de iluminação.
- Erro de leitura de placa que atribui a infração a veículo de terceiro.
- Uso indevido previsível: consulta ao histórico de passagens de um veículo sem autorização.
- Uso indevido previsível: ligar a detecção automática sem validação para reduzir a fila.

### 2.9 Verificação por tema de documentação (cl. 6)
| Tema | Situação hoje | O que falta |
| Responsabilização | A autuação é ato do agente, previsto em resolução. | Registrar no auto que houve pré-seleção automática. |
| Transparência | A sinalização da via informa o videomonitoramento. | Informar ao autuado que a cena foi pré-selecionada por sistema automatizado. |
| Equidade | Não medido. | Verificar se a taxa de falso positivo varia por tipo de veículo, região ou horário. |
| Privacidade | Prazo de retenção contratado. | Descarte automático e auditável das imagens sem indício de infração. |
| Confiabilidade | Acurácia informada pelo fornecedor. | Medição independente, separando falso positivo de falso negativo. |
| Segurança | Acesso restrito ao sistema. | Trilha de auditoria para consulta por placa. |
| Explicabilidade | Imagem anexada ao auto. | Enviar a imagem que fundamenta a autuação junto com a notificação. |
| Impacto ambiental | Processamento contínuo. | Estimar o consumo e avaliar processamento na borda. |

### 2.10 Medidas de tratamento
| Medida | Responsável | Prazo |
| Publicar relatório trimestral com a taxa de descarte na validação | Diretoria de fiscalização | 90 dias |
| Anexar à notificação a imagem que fundamenta a autuação | Área de processamento de autos | 60 dias |
| Auditoria independente do modelo, com corte por região e horário | Órgão de trânsito e universidade parceira | 180 dias |
| Descarte automático de imagens sem indício de infração | TI e fornecedor | 120 dias |
| Limite de cenas por agente e por turno na fila de validação | Gestão operacional | Imediato |

### 2.11 Risco residual
O que permanece depois das medidas previstas:
- **Autuação indevida:** a taxa de descarte mede o erro antes da validação, não as autuações erradas que passaram por ela. Isso só apareceria nas defesas, que ninguém mede.
- **Custo de defesa desigual:** a imagem na notificação facilita contestar, mas não muda quem tem tempo, acesso digital e advogado.
- **Vigilância excessiva:** o descarte reduz o acervo, mas a captura contínua da imagem de quem não cometeu infração continua.
- **Desvio de finalidade:** nenhuma medida cria a trilha de auditoria para consulta por placa apontada em 2.9.
- **Validação de fachada:** o limite de cenas por turno reduz o volume, mas nada verifica a qualidade da validação.
- **Queda de desempenho não detectada:** a auditoria é pontual. Nenhuma medida prevê novo teste após troca de lente ou mudança de ângulo ou de iluminação.
