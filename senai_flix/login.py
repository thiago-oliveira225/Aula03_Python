class Cadastro_Login:
    def efetua_cadastro_login(self):
        email_cadastro = input("Cadastre o seu email = ")
        senha_cadastro = int(input("Cadastre uma senha de 3 números = "))
        print (f"O email {email_cadastro} e a senha {senha_cadastro} foram cadastrados com sucesso !!! \n")

        while True:
        
            print ("#### Vamos fazer o login #### \n")

            email = input("Digite o seu email = ")
            senha = int(input("Digite a sua senha = "))
            if ((email_cadastro == email) and (senha_cadastro == senha)):
                    print("#### Login efetuado com sucesso #### \n")
                    break
            else:
                print ("Erro nos dados digitados !!!\n")       



