---
numero: 181
titulo: Detecção de furtos em estação metroferroviária de grande circulação
rotulo: Caso 181 · Detecção de furtos em espaço público
subtitulo: Caso 181 · modelo de documentação da ABNT NBR ISO/IEC 42005:2025 · versão de oficina 1.0, 12/08/2026
resumo: Reconhece, nas câmeras de uma estação, ações com alta probabilidade de furto em curso e alerta a equipe de segurança. O modelo é treinado com vídeo de milhares de pessoas que só passaram pelas câmeras.
imagem:
alt:
credito:
---
> Documento de simulação para a oficina de Autoavaliação de Impacto Ético (AIE) do Conexão SISP. Caso adaptado da ABNT ISO/IEC TR 24030:2024. O preenchimento é fictício e não descreve um sistema em operação.

## Parte I — O caso de uso, conforme a ISO/IEC TR 24030

### 1.1 Descrição
O sistema analisa as imagens das centenas de câmeras de CCTV de uma estação de grande circulação. Ele reconhece ações com alta probabilidade de furto em curso e alerta a equipe de segurança, que confere a cena na câmera antes de decidir se aborda alguém. Como cada câmera tem ângulo, iluminação e fundo próprios, o modelo é treinado com milhares de horas de vídeo real de cada uma. Esse acervo inclui a imagem de milhares de pessoas que só passaram pelo local.

### 1.2 Retrato do sistema em seis respostas
| Pergunta | Resposta |
| O que o sistema faz, em uma frase? | Reconhece, em imagens de CCTV, ações com alta probabilidade de serem furto em curso. |
| Quem é afetado pela saída dele? | Quem circula na estação, a equipe de segurança, as pessoas abordadas e todas as pessoas cuja imagem está no acervo de treinamento. |
| Que dados usa, e de onde vêm? | Vídeo das câmeras da estação e um acervo de treino de milhares de horas, com cenas de furto encenadas ou reais. |
| A saída é sugestão ou decisão? | Emite alerta para a equipe, que decide abordar. |
| Em que fase está? | Desenvolvimento. |
| Quem responde por ele no órgão? | Gerência de segurança da operadora da estação. |

### 1.3 Por que este caso importa no Brasil
Furto é um problema cotidiano nas grandes redes de transporte público. As estações já operam com centenas de câmeras, instaladas para acompanhar o fluxo, apurar acidentes e instruir ocorrências. O acervo de vídeo já existe e cresce todos os dias. A pergunta do caso é se vale reaproveitar esse acervo para treinar um sistema, e por quanto tempo guardar o material.

!!! **Atenção:** o sistema detecta um ato em curso. Não faz identificação biométrica e não estima a propensão de ninguém a cometer crime. Dado biométrico é sensível (LGPD, art. 11). Identificação biométrica à distância em espaço público e previsão de infrações pelo comportamento anterior estão entre as hipóteses de risco excessivo discutidas no PL 2338/2023. Acoplar o alerta a reconhecimento facial ou a base de mandados muda o patamar da avaliação.

## Parte II — Avaliação de impacto preenchida

### 2.1 Escopo e critérios da avaliação (cl. 5)
- **Objeto avaliado:** o módulo de detecção de anomalia, a regra de emissão de alerta, o protocolo de verificação pela equipe e o acervo de vídeo do treinamento.
- **Fora do escopo:** o parque de câmeras e o sistema de registro de ocorrência.
- **Gatilho da avaliação:** sistema em desenvolvimento que trata a imagem de muitas pessoas sem suspeita e cujo alerta pode levar a abordagem. Reavaliar a cada retreinamento, a cada mudança no protocolo de abordagem ou a cada 12 meses.
- **Limiar de uso sensível:** integrar base biométrica ou de mandados, ou usar o acervo fora do treinamento, exige nova avaliação e decisão formal da autoridade.

### 2.2 Informações sobre o sistema (cl. 6.2)
| Item | Descrição |
| Finalidade pretendida | Ampliar a capacidade da equipe de detectar incidentes em centenas de câmeras ao mesmo tempo. |
| Uso pretendido | Alerta para a equipe presente na estação, que confere a cena na câmera antes de agir. |
| Usos não pretendidos | Abordagem automática por alerta; identificação biométrica; consulta ao histórico de passagem de uma pessoa; reuso do acervo para outra finalidade. |
| Contexto de implantação | Estação de grande circulação, com centenas de câmeras de ângulo, fundo e iluminação variáveis. |
| Grau de autonomia | Médio. A equipe tem a última palavra, mas o alerta define o que ela olha entre centenas de telas. |

### 2.3 Informações sobre os dados (cl. 6.3)
- **Origem:** vídeo contínuo das câmeras e um acervo de milhares de horas gravadas em condições reais, câmera por câmera, reutilizado a cada retreinamento.
- **Dados pessoais:** imagem do rosto e do corpo de milhares de pessoas que só passaram pelas câmeras, sem suspeita. O acervo inclui também cenas encenadas por atores e furtos reais.
- **Consentimento:** não há e não é aplicável.
- **Base legal:** o operador é pessoa jurídica de direito público. O tratamento depende de finalidade pública no exercício de competência legal, com publicidade das hipóteses (LGPD, art. 23), limitado ao mínimo necessário (art. 6º, III).
- **Qualidade e viés:**
  - A qualidade não é uniforme: o desempenho medido em uma câmera não vale para as outras. Furtos que ninguém notificou seguem no acervo como situação normal.
  - O acervo tem três fontes de desigualdade. Os exemplos encenados dependem de quem foi escolhido para representar o furtador. Os exemplos reais vêm do que a equipe percebeu e registrou. E quem permanece no local sem embarcar foge do padrão e tende a ser sinalizado. Nenhuma das três é medida hoje.
- **Retenção:** a operação exige guardar só os trechos com alerta; o treinamento exige o acervo longo. Os dados devem ser eliminados ao fim do tratamento, salvo hipóteses restritas (LGPD, art. 16). Anonimização reversível continua sendo dado pessoal (art. 12).

### 2.4 Informações sobre o algoritmo e o modelo (cl. 6.4)
Modelo de visão computacional treinado com aprendizado profundo sobre vídeo. Ele aprende o padrão de movimento normal e sinaliza o desvio. A saída é um trecho de vídeo com uma pontuação na tela do operador, sem o motivo do alerta. Um limiar de disparo define quanto o sistema sinaliza: baixo demais multiplica os falsos positivos; alto demais deixa passar furtos. Hoje o fornecedor configura o limiar, câmera por câmera.

### 2.5 Partes interessadas (cl. 6.6)
| Parte interessada | Interesse no sistema |
| Pessoas que circulam na estação | Não serem abordadas por engano nem terem a imagem guardada além do necessário. |
| Pessoas em situação de vulnerabilidade | Não virarem alvo preferencial por aparência ou permanência no local. |
| Equipes de segurança da estação | Alerta confiável, com protocolo claro de verificação. |
| Operadora da estação | Sustentar tecnicamente e juridicamente cada abordagem. |
| Sociedade civil e Ministério Público | Fiscalizar proporcionalidade e transparência. |

### 2.6 Benefícios reais e potenciais (cl. 6.7)
- **Para as pessoas:** resposta mais rápida a furtos em local de grande circulação.
- **Para a organização:** direcionamento das equipes em áreas extensas.
- **Para a sociedade:** possível redução de furtos, a ser medida pela taxa de detecção real.

### 2.7 Danos reais e potenciais (cl. 6.8)
| Dano | Quem sofre | Como se manifesta |
| Abordagem indevida | Pessoa inocente | Alerta falso positivo tratado como confirmação de suspeita. |
| Discriminação racial e de grupos marginalizados | Pessoas negras, pessoas em situação de rua e trabalhadores informais | O alerta se concentra em quem o acervo ensinou a estranhar e em quem a equipe já observava mais. |
| Constrangimento público | Pessoa abordada | Abordagem diante de outras pessoas, com exposição e dano à imagem. |
| Retenção de imagem de quem não é suspeito | Milhares de pessoas que usam a estação | O acervo de treinamento guarda a imagem de quem só passou pela estação. |
| Perda de confiança institucional | Órgão e sociedade | Erros noticiados sem dados públicos para contraditório. |

### 2.8 Falhas do sistema e uso indevido previsível (cl. 6.8.3)
- Falso positivo em situação comum: pessoa esperando alguém, ambulante arrumando mercadoria, criança correndo.
- Degradação por mudança de iluminação, ângulo ou densidade da multidão.
- Uso indevido previsível: acoplar o alerta a uma base biométrica para identificar quem foi apontado.
- Uso indevido previsível: divulgar imagens de abordagem antes de qualquer confirmação.
- Uso indevido previsível: monitorar manifestação ou aglomeração política.

### 2.9 Verificação por tema de documentação (cl. 6)
| Tema | Situação hoje | O que falta |
| Responsabilização | A decisão de abordar é da equipe. | Registrar em cada abordagem se houve alerta, o desfecho e o perfil de quem foi abordado. |
| Transparência | A sinalização informa o videomonitoramento. | Informar que há análise automatizada e que as imagens alimentam o treinamento. Relatório público periódico com alertas, abordagens, desfechos e perfil agregado. |
| Equidade | Não medida. | Medir a taxa de falso positivo por raça, gênero e faixa etária, com auditoria externa. |
| Privacidade | Base legal definida (2.3). Retenção do acervo em aberto. | Relatório de impacto à proteção de dados (RIPD) antes da implantação e prazo de retenção do acervo. |
| Confiabilidade | Métrica de laboratório. | Teste em campo, no local real, antes de operar. |
| Segurança | Acesso ao vídeo pouco restrito. | Trilha de auditoria de acesso e vedação de exportar imagem sem autorização. |
| Explicabilidade | Alerta sem justificativa. | Mostrar ao operador a cena e o motivo do alerta, com registro da decisão. |
| Impacto ambiental | Cada câmera analisa o próprio vídeo no local; só o trecho com alerta vai ao servidor central. | Estimar o consumo de energia do retreinamento, que reprocessa o acervo inteiro. |

### 2.10 Medidas de tratamento
| Medida | Responsável | Prazo |
| Relatório de impacto à proteção de dados antes da implantação | Encarregado de dados | Antes do piloto |
| Auditoria externa de viés, com recorte racial e etário | Operadora e instituição independente | Antes do piloto |
| Protocolo de abordagem que proíbe ação apenas com base no alerta | Comando operacional | Antes do piloto |
| Relatório público trimestral de alertas, abordagens e desfechos | Operadora | A cada trimestre |
| Vedação formal de integração com base biométrica sem nova avaliação | Autoridade máxima do órgão | Imediato |
| Canal de reparação para quem for abordado por erro | Ouvidoria | Antes do piloto |

### 2.11 Risco residual
O que permanece depois das medidas previstas:
- **Abordagem indevida:** o registro do alerta e do desfecho de cada abordagem segue como lacuna. Não há como saber quantas abordagens vieram de erro.
- **Discriminação:** a auditoria de viés depende do registro de quem foi abordado, que ainda não existe, e não altera as origens do viés descritas em 2.3.
- **Retenção de imagem de quem não é suspeito:** o prazo de retenção ainda não existe. Quando existir, não alcança quem já foi gravado.
- **Constrangimento público:** a reparação vem depois da exposição.
- **Perda de confiança institucional:** o relatório público depende do registro de alertas e desfechos, que ainda não existe.
- **Degradação do modelo:** o teste em campo vem antes da operação. Nenhuma medida prevê novo teste quando iluminação, ângulo ou fluxo mudarem.
