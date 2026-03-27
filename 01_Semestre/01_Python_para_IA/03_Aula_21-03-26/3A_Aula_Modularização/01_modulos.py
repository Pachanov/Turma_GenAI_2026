#CONDA 
# Siga esses passos para instalar o ambiente Conda em sua máquina.
# Serve, dentre outras coisas, para evitar conflitos e compartimentar diferentes pacotes Python.
# Cuidado!
# Faça em casa. Você não vai conseguir instalar nos laboratórios devido às restrições de instalação.

# Baixe a última versão do miniconda.
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# Execute o instalador:
# bash Miniconda3-latest-Linux-x86_64.sh
# Recarregue o shell, ou execute:
# source ~/.bashrc
# Se tudo deu certo, seu shell vai informar o ambiente Conda atual (base):
# # (base) usuario@computador:~$


# Para criar um novo ambiente:
# conda create --name nome_ambiente
# Para ativar o ambiente:
# conda activate nome_ambiente
# Para instalar um pacote no ambiente atual, use preferencialmente:
# conda install <PACKAGE_NAME>

# Para listar todos ambientes disponíveis:
# conda info --envs
# Para voltar ao ambiente base:
# conda activate