---
numero: 186
titulo: Previsão do nível de rios em enchentes
rotulo: Caso 186 · Previsão do nível de rios em enchentes
subtitulo: Caso 186 · modelo de documentação da ABNT NBR ISO/IEC 42005:2025 · versão de oficina 1.0, 12/08/2026
resumo: Prevê o nível dos rios nas próximas horas a partir de chuva, vazão e série histórica, para ampliar o tempo de reação da defesa civil.
imagem:
alt:
credito:
---
> Documento de simulação para a oficina de Autoavaliação de Impacto Ético (AIE) do Conexão SISP. Caso adaptado da ABNT ISO/IEC TR 24030:2024. O preenchimento é fictício e não descreve um sistema em operação.

## O sistema de IA, conforme a ISO/IEC TR 24030

### 1.1 Descrição
O sistema prevê o nível dos rios para as próximas horas a partir da chuva observada, da vazão e da série histórica. A previsão embasa o alerta enviado às prefeituras e à defesa civil. A decisão de evacuar uma área é sempre humana.

### 1.2 Descrição do sistema em quatro respostas
| Pergunta | Resposta |
| O que o sistema faz, em uma frase? | A cada 10 minutos, prevê o nível do rio para até 6 horas à frente e publica um mapa de perigo por estação. |
| Quem é afetado pela saída dele? | Moradores de área de risco, defesa civil e prefeituras. |
| Que dados usa, e de onde vêm? | Estações telemétricas, radar meteorológico e série histórica. |
| A saída é sugestão ou decisão? | Produz o mapa de perigo que embasa o aviso. A decisão de evacuar é humana. |

## Avaliação de impacto, conforme a ISO/IEC 42005:2025

### 2.1 Escopo e critérios da avaliação (cl. 5)
- **Objeto avaliado:** o modelo de previsão de nível, a regra de disparo do alerta e a forma do mapa de perigo entregue a quem decide.
- **Fora do escopo:** a rede de estações telemétricas e os canais de comunicação com a população.
- **Gatilho da avaliação:** sistema em produção cuja saída embasa decisão sobre vida e integridade física. Reavaliar a cada retreinamento, a cada bacia nova, após todo evento extremo em que a previsão errou, ou a cada 12 meses.
- **Limiar de uso sensível:** mudar o limiar de disparo do alerta exige nova avaliação e registro da decisão.

### 2.2 Informações sobre o sistema (cl. 6.2)
| Item | Descrição |
| Finalidade pretendida | Ampliar o tempo de reação da defesa civil e da população antes da cheia. |
| Uso pretendido | Previsão a cada 10 minutos, com horizonte de 6 horas e faixa de incerteza, apresentada como mapa de perigo para apoiar a decisão de alerta. |
| Usos não pretendidos | Usar a previsão para licenciamento ou para cobertura de seguro; usar fora das bacias em que o modelo foi validado. |
| Contexto de implantação | Bacias com estação telemétrica ativa e cobertura de radar. |
| Grau de autonomia | Alta automação no cálculo: previsão e mapa saem sem intervenção, a cada 10 minutos. A decisão de evacuar é humana, mas na urgência a previsão costuma ser aceita sem contestação. |

### 2.3 Informações sobre os dados (cl. 6.3)
- **Origem:** estações telemétricas de nível e chuva, radar meteorológico e séries históricas de vazão.
- **Dados pessoais:** não há. O impacto recai sobre territórios e populações, não sobre indivíduos identificados.
- **Dependência externa:** a chuva prevista vem de outro órgão. Erro ou atraso na origem entra na previsão sem controle do centro de monitoramento.
- **Qualidade:** estação com falha, assoreamento ou corrosão degrada a entrada sem aviso. Bacias sem estação ficam sem previsão.
- **Cobertura desigual:** as bacias mais instrumentadas tendem a ser as de maior interesse econômico, não as de maior vulnerabilidade social.
- **Retenção:** séries mantidas de forma permanente, por valor científico e operacional.

### 2.4 Informações sobre o algoritmo e o modelo (cl. 6.4)
Modelos de aprendizado de máquina treinados com séries hidrometeorológicas, combinados a modelos hidrológicos tradicionais. Dois pontos importam. Eventos extremos são raros na série histórica, então o modelo é menos confiável na situação em que mais importa. E uma previsão determinística informa um único resultado: declarar a incerteza junto com o número permite ao gestor decidir sabendo do erro possível.

### 2.5 Partes interessadas (cl. 6.6)
| Parte interessada | Interesse no sistema |
| Moradores de área de risco | Receber o alerta com antecedência útil e em linguagem compreensível. |
| Defesa civil municipal | Saber o grau de confiança da previsão antes de acionar a evacuação. |
| Prefeituras | Planejar abrigo, rota e transporte. |
| Órgão de monitoramento | Manter a credibilidade do sistema de alerta ao longo do tempo. |
| Agência meteorológica, como fornecedora de dados | Entregar a previsão de chuva em tempo e formato utilizáveis. |
| Desenvolvedor do modelo | Manter e retreinar o modelo conforme as bacias mudam. |
| Comunidade científica | Reproduzir e criticar o modelo. |

### 2.6 Benefícios reais e potenciais (cl. 6.7)
- **Para as pessoas:** horas de antecedência para sair de casa com documentos e com os idosos da família.
- **Para a organização:** equipes de campo priorizadas onde o risco é maior.
- **Para a sociedade:** menos perdas materiais e menos mortes evitáveis em eventos extremos.

### 2.7 Danos reais e potenciais (cl. 6.8)
| Dano | Quem sofre | Como se manifesta |
| Alerta que não vem | Moradores de área de risco | Evento extremo fora do padrão histórico não é previsto. |
| Alerta em excesso | Moradores e defesa civil | Evacuações desnecessárias reduzem a adesão ao próximo alerta. |
| Desigualdade de cobertura | Comunidades em bacias sem estação | Quem não é monitorado não é alertado. |
| Excesso de confiança no número | Gestor da defesa civil | Previsão sem faixa de incerteza é lida como certeza. |
| Falha em cascata | Toda a área monitorada | Queda da rede telemétrica durante a chuva, quando o dado é mais necessário. |

### 2.8 Falhas do sistema e uso indevido previsível (cl. 6.8.3)
- Degradação silenciosa por sensor descalibrado ou submerso.
- Chuva acima do histórico, com erro maior no evento extremo.
- Interrupção ou atraso na previsão de chuva da agência meteorológica.
- Uso indevido previsível: divulgar a previsão bruta ao público sem tradução e sem faixa de incerteza.
- Uso indevido previsível: usar o histórico de alertas para negar a responsabilidade do poder público em ação judicial.

### 2.9 Verificação por tema de documentação (cl. 6)
| Tema | Situação hoje | O que falta |
| Responsabilização | A decisão de alerta é do órgão, registrada em ata. | Registrar qual previsão embasou cada alerta. |
| Transparência | Metodologia publicada em artigo científico. | Resumo público em linguagem simples, para prefeituras e comunidades. |
| Equidade | Não avaliado por território. | Mapear as áreas de risco sem estação e priorizar a instalação. |
| Privacidade | Sem dado pessoal. | Sem ação. |
| Confiabilidade | Desempenho medido em bacias selecionadas. | Publicar o acerto por bacia e por antecedência, separando eventos extremos. |
| Segurança | Infraestrutura crítica com redundância parcial. | Plano de contingência para queda da telemetria ou da previsão externa durante o evento. |
| Explicabilidade | Mapa de perigo por estação, com o nível previsto. | Entregar a previsão sempre com a faixa de incerteza. |
| Impacto ambiental | Servidor de porte modesto, local ou em nuvem. | Estimar o consumo do treinamento e da operação. |

### 2.10 Medidas de tratamento
| Medida | Responsável | Prazo |
| Entregar toda previsão com faixa de incerteza explícita | Equipe de modelagem | 90 dias |
| Publicar o desempenho por bacia, com recorte de eventos extremos | Divisão de produtos | 180 dias |
| Mapa público das áreas de risco sem cobertura telemétrica | Monitoramento e parceiros municipais | 120 dias |
| Protocolo de contingência para queda de estações durante evento | Operação | 60 dias |
| Material em linguagem simples para a defesa civil municipal | Comunicação | 90 dias |

### 2.11 Risco residual
O que permanece depois das medidas previstas:
- **Alerta que não vem:** o desempenho é medido em bacias selecionadas. Nenhuma medida cria medição própria para eventos extremos, raros por definição.
- **Alerta em excesso:** a faixa de incerteza ajuda quem decide, mas nenhuma medida acompanha a adesão da população ao alerta.
- **Excesso de confiança no número:** a faixa de incerteza passa a ser entregue, mas nada garante que ela seja usada na decisão.
- **Falha em cascata:** o protocolo de contingência diz o que fazer quando a previsão externa cai, mas não repõe o dado. Sem uma segunda fonte, a previsão degrada durante o evento.
