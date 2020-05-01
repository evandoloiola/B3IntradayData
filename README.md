#B3IntradayData

Aplicação Python para obteção de dados intraday de ações e derivativos da B3 de uma API da UOL Finance e gravar em uma base de dados MySql.

##Pré-requisitos:
a) Conhecimento básico em MySql.
b) Conhecimento intermediário de Python.
Instalação:

###1) Instalar MySql na última versão
###2) Executar seguintes scripts SQL para criação da base de dados e tabelas:
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
###4) Adicionar na pasta database o arquivo 'db.json' com o seguinte conteúdo:

```json
{
      "host":"ip ou nome servidor de dados",
      "user":"usuário do banco de dados",
      "password":"senha de acesso ao banco de dados",
      "db":"nome do banco de dados"

  }
```
