# B3IntradayData

[![Build Status](https://travis-ci.org/marretti/stock-market-b3.svg?branch=master)](https://travis-ci.org/marretti/stock-market-b3)
[![License MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/marretti/stock-market-b3/blob/master/LICENSE)

Aplicação Python para obteção gratuíta (Free) de dados intraday de ações e derivativos da B3 sem necessidade de cadastro ou usuário através da API do site UOL Finance e gravar em uma base de dados MySql (MariaDB).

## Pré-requisitos:
#### a) Conhecimento básico em MySql.
#### b) Conhecimento intermediário de Python.

## Instalação:

### 1) Instalar MySql na última versão.
### 2) Executar seguintes scripts SQL para criação da base de dados e tabelas:
```sql
    SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
    SET AUTOCOMMIT = 0;
    START TRANSACTION;
    SET time_zone = "+00:00";

    --
    -- Banco de dados: `B3Intraday`
    --

    -- --------------------------------------------------------

    --
    -- Estrutura da tabela `quotes`
    --

    CREATE TABLE `quotes` (
      `index` bigint(20) DEFAULT NULL,
      `date` bigint(20) DEFAULT NULL,
      `price` double DEFAULT NULL,
      `low` double DEFAULT NULL,
      `high` double DEFAULT NULL,
      `var` double DEFAULT NULL,
      `varpct` double DEFAULT NULL,
      `vol` double DEFAULT NULL,
      `tricker` text DEFAULT NULL
    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;

    -- --------------------------------------------------------

    --
    -- Estrutura da tabela `trickers`
    --

    CREATE TABLE `trickers` (
      `id` int(11) NOT NULL,
      `trickerBov` varchar(55) NOT NULL,
      `tricker` varchar(55) NOT NULL
    ) ENGINE=MyISAM DEFAULT CHARSET=latin1;

    --
    -- Índices para tabelas despejadas
    --

    --
    -- Índices para tabela `quotes`
    --
    ALTER TABLE `quotes`
      ADD KEY `ix_quotes_index` (`index`);

    --
    -- Índices para tabela `trickers`
    --
    ALTER TABLE `trickers`
      ADD PRIMARY KEY (`id`);
    COMMIT;
```
### 4) Adicionar na pasta database o arquivo 'db.json' com o seguinte conteúdo:

```json
{
      "host":"ip ou nome servidor de dados",
      "user":"usuário do banco de dados",
      "password":"senha de acesso ao banco de dados",
      "db":"nome do banco de dados"

  }
```
### 5) Inserir na tabela `trickers` os papeis que serão monitorados ao seu critério. 
Obs.: Os dados id e tricker dos papéis podemos ser obtidos através da função "get_assets" do modulo "uol-api" na pasta "uol".

```sql
INSERT INTO `trickers` (`id`, `trickerBov`, `tricker`) VALUES
(1545, 'ABEV3', 'ABEV3.SA'),
(39, 'ALPA4', 'ALPA4.SA'),
(1881, 'AZUL4', 'AZUL4.SA'),
(1027, 'BOVA11', 'BOVA11.SA'),
(192, 'CMIG4', 'CMIG4.SA'),
(222, 'CSNA3', 'CSNA3.SA'),
(283, 'EMBR3', 'EMBR3.SA'),
(683, 'USIM5', 'USIM5.SA'),
(775, 'VALE3', 'VALE3.SA'),
(704, 'WEGE3', 'WEGE3.SA'),
(2324, 'YDUQ3', 'YDUQ3.SA');
```
