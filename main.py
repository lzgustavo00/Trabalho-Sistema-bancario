#include <iostream>
#include <string>
#include <limits>

using namespace std;

// ---------------------------------------------------------
// Função para limpar entradas inválidas
// ---------------------------------------------------------
void limparEntrada() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

// ---------------------------------------------------------
// Exibe o menu principal
// ---------------------------------------------------------
void exibirMenu() {
    cout << "\n";
    cout << "=====================================\n";
    cout << "          BANCO INF101\n";
    cout << "    SISTEMA DE CONTAS BANCARIAS\n";
    cout << "=====================================\n";
    cout << " [1] Cadastrar conta\n";
    cout << " [2] Consultar conta\n";
    cout << " [3] Verificar saldo\n";
    cout << " [4] Alterar tipo da conta\n";
    cout << " [5] Ativar/Desativar conta\n";
    cout << " [6] Sair\n";
    cout << "=====================================\n";
}

// ---------------------------------------------------------
// Verifica se existe uma conta cadastrada
// ---------------------------------------------------------
bool existeConta(int numeroConta) {
    return numeroConta != 0;
}

// ---------------------------------------------------------
// Cadastro da conta
// ---------------------------------------------------------
void cadastrarConta(
    int& numeroConta,
    string& nomeCliente,
    string& cpf,
    int& tipoConta,
    double& saldo,
    bool& contaAtiva
) {
    cout << "\n========== NOVO CADASTRO ==========\n";

    // Número da conta
    while (true) {
        cout << "Numero da conta: ";
        cin >> numeroConta;

        if (cin.fail()) {
            limparEntrada();
            cout << "Informe um numero valido.\n";
        }
        else if (numeroConta <= 0) {
            cout << "O numero da conta deve ser maior que zero.\n";
        }
        else {
            break;
        }
    }

    limparEntrada();

    // Nome do cliente
    do {
        cout << "Nome do titular: ";
        getline(cin, nomeCliente);

        if (nomeCliente.empty()) {
            cout << "O nome do titular nao pode ficar vazio.\n";
        }

    } while (nomeCliente.empty());

    // CPF
    do {
        cout << "CPF do titular: ";
        getline(cin, cpf);

        if (cpf.empty()) {
            cout << "O CPF nao pode ficar vazio.\n";
        }

    } while (cpf.empty());

    // Tipo da conta
    do {
        cout << "\nEscolha o tipo da conta:\n";
        cout << "1 - Conta Corrente\n";
        cout << "2 - Conta Poupanca\n";
        cout << "Opcao: ";

        cin >> tipoConta;

        if (cin.fail()) {
            limparEntrada();
            tipoConta = 0;
            cout << "Digite apenas 1 ou 2.\n";
        }
        else if (tipoConta < 1 || tipoConta > 2) {
            cout << "Tipo de conta invalido.\n";
        }

    } while (tipoConta < 1 || tipoConta > 2);

    // Saldo inicial
    do {
        cout << "Saldo inicial: R$ ";
        cin >> saldo;

        if (cin.fail()) {
            limparEntrada();
            saldo = -1;
            cout << "Informe um valor numerico valido.\n";
        }
        else if (saldo < 0) {
            cout << "O saldo inicial nao pode ser negativo.\n";
        }

    } while (saldo < 0);

    // Toda conta inicia ativa
    contaAtiva = true;

    limparEntrada();

    cout << "\nConta cadastrada com sucesso!\n";
}

// ---------------------------------------------------------
// Consulta dos dados cadastrados
// ---------------------------------------------------------
void consultarConta(
    int numeroConta,
    const string& nomeCliente,
    const string& cpf,
    int tipoConta,
    double saldo,
    bool contaAtiva
) {
    cout << "\n=========== CONTA ===========\n";
    cout << "Numero : " << numeroConta << endl;
    cout << "Titular: " << nomeCliente << endl;
    cout << "CPF    : " << cpf << endl;

    cout << "Tipo   : ";

    if (tipoConta == 1) {
        cout << "Corrente";
    }
    else {
        cout << "Poupanca";
    }

    cout << endl;
    cout << "Saldo  : R$ " << saldo << endl;

    cout << "Status : ";

    if (contaAtiva) {
        cout << "Ativa";
    }
    else {
        cout << "Inativa";
    }

    cout << endl;
    cout << "==============================\n";
}

// ---------------------------------------------------------
// Mostra somente o saldo
// ---------------------------------------------------------
void mostrarSaldo(int numeroConta, double saldo) {
    cout << "\n========== SALDO ==========\n";
    cout << "Conta: " << numeroConta << endl;
    cout << "Saldo disponivel: R$ " << saldo << endl;
    cout << "===========================\n";
}

// ---------------------------------------------------------
// Alteração do tipo de conta
// ---------------------------------------------------------
void alterarTipo(int& tipoConta) {

    cout << "\n====== ALTERACAO DE CONTA ======\n";

    cout << "Tipo atual: ";

    if (tipoConta == 1) {
        cout << "Corrente\n";
    }
    else {
        cout << "Poupanca\n";
    }

    do {
        cout << "\nNovo tipo:\n";
        cout << "1 - Conta Corrente\n";
        cout << "2 - Conta Poupanca\n";
        cout << "Opcao: ";

        cin >> tipoConta;

        if (cin.fail()) {
            limparEntrada();
            tipoConta = 0;
            cout << "Opcao invalida.\n";
        }
        else if (tipoConta != 1 && tipoConta != 2) {
            cout << "Escolha 1 ou 2.\n";
        }

    } while (tipoConta != 1 && tipoConta != 2);

    limparEntrada();

    cout << "\nTipo da conta alterado com sucesso!\n";
}

// ---------------------------------------------------------
// Ativação ou desativação da conta
// ---------------------------------------------------------
void alterarStatus(bool& contaAtiva) {

    contaAtiva = !contaAtiva;

    cout << "\nA conta agora esta ";

    if (contaAtiva) {
        cout << "ATIVA.";
    }
    else {
        cout << "INATIVA.";
    }

    cout << endl;
}

// ---------------------------------------------------------
// Programa principal
// ---------------------------------------------------------
int main() {

    // Variáveis individuais exigidas pelo trabalho
    int numeroConta = 0;
    string nomeCliente;
    string cpf;
    int tipoConta = 0;
    double saldo = 0.0;
    bool contaAtiva = false;

    int escolha;

    do {

        exibirMenu();

        cout << "Digite sua escolha: ";
        cin >> escolha;

        if (cin.fail()) {
            limparEntrada();
            cout << "\nDigite somente numeros de 1 a 6.\n";
            continue;
        }

        limparEntrada();

        switch (escolha) {

            case 1:

                cadastrarConta(
                    numeroConta,
                    nomeCliente,
                    cpf,
                    tipoConta,
                    saldo,
                    contaAtiva
                );

                break;

            case 2:

                if (!existeConta(numeroConta)) {
                    cout << "\nNenhuma conta cadastrada.\n";
                }
                else {
                    consultarConta(
                        numeroConta,
                        nomeCliente,
                        cpf,
                        tipoConta,
                        saldo,
                        contaAtiva
                    );
                }

                break;

            case 3:

                if (!existeConta(numeroConta)) {
                    cout << "\nCadastre uma conta antes de consultar o saldo.\n";
                }
                else {
                    mostrarSaldo(numeroConta, saldo);
                }

                break;

            case 4:

                if (!existeConta(numeroConta)) {
                    cout << "\nNenhuma conta cadastrada.\n";
                }
                else {
                    alterarTipo(tipoConta);
                }

                break;

            case 5:

                if (!existeConta(numeroConta)) {
                    cout << "\nNenhuma conta cadastrada.\n";
                }
                else {
                    alterarStatus(contaAtiva);
                }

                break;

            case 6:

                cout << "\n=====================================\n";
                cout << "       ENCERRANDO O BANCO INF101\n";
                cout << "     Obrigado por utilizar o sistema\n";
                cout << "=====================================\n";

                break;

            default:

                cout << "\nOpcao inexistente. Escolha de 1 a 6.\n";

                break;
        }

    } while (escolha != 6);

    return 0;
}
