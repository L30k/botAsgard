<h1 align="center">Bot Asgard</h1>


<strong>
Este projeto é um bot para Discord que oferece ferramentas para gerenciamento de um servidor focado no jogo Throne and Liberty.
</strong>

<hr>

## Documentação

- [Configuração e Uso](#configuração-e-uso)
- [Funcionalidades](#funcionalidades)
- [Licença](LICENSE.md)

<hr>

## Configuração e Uso

Antes de começar, você precisará configurar o arquivo de ambiente `.env` com as informações necessárias. Siga os passos
abaixo:

1. Faça uma cópia do arquivo [`.env.example`](src%2F.env.example) e renomeie para `.env`.

2. Preencha os campos no arquivo `.env` com suas informações:

> BOT_TOKEN = (coloque aqui o token do seu bot)
>
> MODERATOR_ID = (coloque aqui o ID do moderador responsável)

Para ativar o bot pela primeira vez:

1. Verifique se o arquivo `.env` está configurado corretamente.
2. Inicie o bot.
3. No chat do Discord, execute o comando `!sincronizar` para sincronizar os comandos. Este passo só precisa ser feito
   uma vez durante a primeira ativação do bot.

<hr>

## Funcionalidades

<h4>Comandos</h4>

> **/limpar [#canal]** - Limpa todas as mensagens de um canal específico.
>
> **/enviar [@cargo] [Mensagem]** - Envia uma mensagem para todos os membros de um cargo específico.

<h4>Eventos</h4>

> Atualização do status do bot

<hr>

## Links

<p align="center">
    <a href="https://discord.gg/RKAm2ySAce">
        <img src="https://skillicons.dev/icons?i=discord" alt="Discord">
    </a>
    <a href="https://github.com/L30k/botAsgard">
        <img src="https://skillicons.dev/icons?i=github" alt="GitHub">
    </a>
</p>
