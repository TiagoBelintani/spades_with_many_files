import os

arquivos_R1 = [f for f in os.listdir() if f.endswith('R1.fastq.gz')]
arquivos_R2 = [f for f in os.listdir() if f.endswith('R2.fastq.gz')]

for arquivo_R1, arquivo_R2 in zip(arquivos_R1, arquivos_R2):
    nome_saida = arquivo_R1.replace('_R1.fastq.gz', '')
    comando = f'spades.py -1 {arquivo_R1} -2 {arquivo_R2} --careful --cov-cutoff auto -o {nome_saida}'
    os.system(comando)


