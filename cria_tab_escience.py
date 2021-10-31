# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 19:07:15 2021

@author: gabri
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 17:21:45 2021

@author: gabri
"""
"""
Dado um arquivo copiado do NED com vários objetos, cria um arquivo .txt em
formatação CSV que pode ser lido em TOPCAT com os valores de nome, ascencao
reta e declinacao em graus decimais, redshift. Uma coluna de magnitude é
criada, mas o NED não retorna esse valor.

"""

def main():
    
    arq_dados = "dados_q1_e.txt"
    arq = open(arq_dados, 'r', encoding = 'utf - 8')
    linha_dados = arq.readline()
    arq_out = open('tab_escience.txt', 'w', encoding = 'utf - 8')
    
    arq_out.write('Nome,RA (J2000),DEC (J2000),redshift,mag')
    
    while linha_dados:
        arq_out.write('\n')
        dado_i = linha_dados.split('|')
        
        lista_nome = dado_i[2].split()
        nome = lista_nome[0] + ' ' + lista_nome[1]
        arq_out.write(nome)
        arq_out.write(',')
        
        # convertendo as medidas de angulo
        # RA de horas para graus 
        dados_ra = dado_i[5][:-1]
        dados_ra_h = float(dados_ra[0:1])
        dados_ra_m = float(dados_ra[3:4])
        dados_ra_s = float(dados_ra[6:])
        
        ra = ra_em_graus(dados_ra_h, dados_ra_m, dados_ra_s)
        arq_out.write(str(ra))
        arq_out.write(',')
        
        dados_dec = dado_i[6][1:-1]
        sinal = True
        
        if dado_i[6][0] == '-':
            sinal = False
            
        dados_dec_g = float(dados_dec[0:2])
        dados_dec_m = float(dados_dec[3:5])
        dados_dec_s = float(dados_dec[6:])
        
        dec = dec_em_deci(dados_dec_g, dados_dec_m, dados_dec_s, sinal)
        arq_out.write(str(dec))
        arq_out.write(',')
        
        z = dado_i[8].split()
        
        if len(z) > 0:
            arq_out.write(str(z[0]))
            arq_out.write(',')
            
        elif len(z) == 0:
            arq_out.write(' ,')
        
        linha_dados = arq.readline()
        
    arq.close()
    arq_out.close()
    
    



    '''
    ngc_1 = dado_1[7]
    arq_out.write('NGC 000')
    arq_out.write(ngc_1)
    arq_out.write('\n')
    
    ngc_i = ngc_1
    
    
    while linha_dados:
        
        dado_i = linha_dados.split()
        ngc_j = dado_i[7]
        
        if ngc_j != ngc_i:
            arq_out.write('NGC ')
            
            for i in range(4 - len(ngc_j)):
                arq_out.write('0')
                
                arq_out.write(ngc_j)
                arq_out.write('\n')
                
        linha_dados = arq.readline()
        ngc_i = ngc_j
        '''
def ra_em_graus(h, m, s):
    
    h_t = h + m/60 + s/360
    
    return(15*h_t)

def dec_em_deci(g, m, s, sinal):
    if sinal:
        return(g + m/60 + s/360)
    else:
        return(-g - m/60 - s/360)
main()
