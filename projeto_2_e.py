# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:31:06 2020

@author: gabri
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:01:50 2020

@author: gabri
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

def main():
    
    """
    """
    
    arquivo_dados = "k0_t4750_g2.5_cort.txt"
    arquivo_linhas = "linhas_moore.txt"
    arquivo_ident = "identificacao.txt"
    arquivo_saida = "larguras_" + arquivo_dados
    arqSai = open(arquivo_saida, 'w', encoding = 'utf - 8')
    #espac_igual = input("Os pontos do arquivo têm abscissas igualmente espaçadas? (s/n): ")
    espac_igual = "s"
    arqSai.write("Linha objetivada(Moore) (A):")
    arqSai.write("     ")
    arqSai.write("Identificação:")
    arqSai.write("     ")
    arqSai.write("Ener. exc. (eV):")
    arqSai.write("     ")
    arqSai.write("Problema observado:")
    arqSai.write("     ")
    arqSai.write("Intervalo usado (A):")
    arqSai.write("     ")
    arqSai.write("L. de menor fluxo (A):")
    arqSai.write("     ")
    arqSai.write("Intervalo usado para normalização (A):")
    arqSai.write("     ")
    arqSai.write("Fluxo de normalização:")
    arqSai.write("     ")
    arqSai.write("Integral de trapézios a (A):")
    arqSai.write("     ")
    arqSai.write("Integral de trapézios b (A):")
    arqSai.write("     ")
    arqSai.write("Integral de Simpson (A):")
    arqSai.write("     ")
    arqSai.write("Erro relativo (int. b e Simpson):")
    arqSai.write("     ")
    arqSai.write("Intervalo usado para espelhamento (A):")
    arqSai.write("     ")
    arqSai.write("Integral de trapézios espelhada a (A):")
    arqSai.write("     ")
    arqSai.write("Integral de trapézios espelhada b (A):")
    arqSai.write("     ")
    arqSai.write("Integral de Simpson espelhada:")
    arqSai.write("     ")
    arqSai.write("Erro relativo (int. b e Simpson) espelhado:")
    
    arqSai.write("\n")

    arqEntra = open(arquivo_ident, 'r', encoding = 'utf - 8')
    linha_ident = arqEntra.readline()
    
    lista_pontos = np.loadtxt(arquivo_dados)
    n_pontos = len(lista_pontos)
    wl_spc = []
    fluxo_spc = []
    
    for i in range(n_pontos):
        wl_spc.append(lista_pontos[i][0])
        fluxo_spc.append(lista_pontos[i][1])
        
    wl_spc = np.array(wl_spc)
    intervalo_pontos = wl_spc[1] - wl_spc[0]
    fluxo_spc = np.array(fluxo_spc)

    linhas = np.loadtxt(arquivo_linhas)
    n_lin = len(linhas)

    for j in range(n_lin):
        
        linha_ident = arqEntra.readline()
        lista_ident = linha_ident.split()
        str_ident = lista_ident[0] + " " + lista_ident[1]
        str_ep = lista_ident[2]
        linha_moore = float(linhas[j])
        
        arqSai.write("%-33s" %(str(linha_moore)))
        arqSai.write("%-19s" %(str_ident))
        arqSai.write("%-21s" %(str_ep))
        
        print("\nLinha objetivada do Moore:", linha_moore)
        
        lista_intervalos_norm = []
        ponto_norm = []
        lista_maior_fluxo = []
        int_plot = 5
        wl_cort_1, fluxo_cort_1, maior_fluxo_1, menor_wl = corte_de_dados_lista(wl_spc, fluxo_spc, linha_moore - int_plot, linha_moore + int_plot)
        ponto_norm.append(wl_cort_1[0])
        ponto_norm.append(wl_cort_1[-1])
        lista_intervalos_norm.append(ponto_norm)
        ponto_norm = []
        lista_maior_fluxo.append(maior_fluxo_1)
        lista_1s = []
        for k in range(len(fluxo_cort_1)):
            lista_1s.append(1)
        lista_1s = np.array(lista_1s)
        
        plt.plot(wl_cort_1, fluxo_cort_1/maior_fluxo_1, "r.")
        plt.plot(wl_cort_1, lista_1s)
        plt.show()
        
        int_plot = 2
        wl_cort_2, fluxo_cort_2, maior_fluxo_2, menor_wl = corte_de_dados_lista(wl_cort_1, fluxo_cort_1, linha_moore - int_plot, linha_moore + int_plot)
        ponto_norm.append(wl_cort_2[0])
        ponto_norm.append(wl_cort_2[-1])
        lista_intervalos_norm.append(ponto_norm)
        ponto_norm = []
        lista_maior_fluxo.append(maior_fluxo_2)
        lista_1s = []
        for k in range(len(fluxo_cort_2)):
            lista_1s.append(1)
        lista_1s = np.array(lista_1s)
        
        plt.plot(wl_cort_2, fluxo_cort_2/maior_fluxo_2, "b.")
        plt.plot(wl_cort_2, lista_1s)
        plt.show()
        
        int_plot = 1
        wl_cort_3, fluxo_cort_3, maior_fluxo_3, menor_wl = corte_de_dados_lista(wl_cort_2, fluxo_cort_2, linha_moore - int_plot, linha_moore + int_plot)
        ponto_norm.append(wl_cort_3[0])
        ponto_norm.append(wl_cort_3[-1])
        lista_intervalos_norm.append(ponto_norm)
        ponto_norm = []
        lista_maior_fluxo.append(maior_fluxo_3)
        lista_1s = []
        for k in range(len(fluxo_cort_3)):
            lista_1s.append(1)
        lista_1s = np.array(lista_1s)
        
        plt.plot(wl_cort_3, fluxo_cort_3/maior_fluxo_3, "g.")
        plt.plot(wl_cort_3, lista_1s)
        plt.show()
        
        prob = int(input("\nQual problema é observado na linha?: "))
        arqSai.write("%-24s" %(str(prob)))
        
        if (prob != 4) and (prob != 3):
            
            if (prob == 0) or (prob == 5) or (prob == 6):
        
                limiteInf = float(input("\nDigite o limite inferior para integração: "))
                limiteSup = float(input("\nDigite o limite superior para integração: "))
                arqSai.write("%-7.7s" %(str(limiteInf)))
                arqSai.write(" - ")
                arqSai.write("%-15.7s" %(str(limiteSup)))
                wl_cort_int, fluxo_cort_int, maior_fluxo_4, menor_wl = corte_de_dados_lista(wl_cort_2, fluxo_cort_2, limiteInf, limiteSup)
                arqSai.write("%-27.9s" %(str(menor_wl)))
                lista_maior_fluxo.append(maior_fluxo_4)
                ponto_norm.append(wl_cort_int[0])
                ponto_norm.append(wl_cort_int[-1])
                lista_intervalos_norm.append(ponto_norm)
                ponto_norm = []
                
                variavel = int(input("\nDe qual dos intervalos deve ser tomado o maior fluxo?: "))
                maior_fluxo = lista_maior_fluxo[variavel - 1]
                int_norm = lista_intervalos_norm[variavel - 1]
                
                str_norm = str(int_norm[0]) + " - " + str(int_norm[1])
                arqSai.write("%-43.9s" %(str_norm))
                arqSai.write("%-27.9s" %(str(maior_fluxo)))
                
                
                listaPhi, listaH = calcPhi(wl_cort_int, fluxo_cort_int)
                
                if espac_igual == "s":
                    
                    intervalo_int = wl_cort_int[-1] -  wl_cort_int[0]
                    
                    intervalo_pontos_int = intervalo_pontos
                    int_trap_a_red = (trap_1(intervalo_pontos_int, fluxo_cort_int))/maior_fluxo
                    int_a_corr = intervalo_int - int_trap_a_red
                    arqSai.write("%-33.9s" %(str(int_a_corr)))
                    
                    int_trap_b_red = int_trap_a_red/2
                    ##lista_x_inter = []
                    ##lista_y_inter = []
                    intervalo_pontos_int /= 2
                    
                    for l in range(len(wl_cort_int) - 1):
                    
                        x_inter_l = wl_cort_int[l] + intervalo_pontos_int
                        ##lista_x_inter.append(x_inter_l)
                        posicao_x_inter_l = achaX(x_inter_l, wl_cort_int)
                        y_inter_l = poli(x_inter_l, posicao_x_inter_l, listaPhi, wl_cort_int, fluxo_cort_int, listaH)
                        int_trap_b_red += (intervalo_pontos_int*y_inter_l)/maior_fluxo
                        ##lista_y_inter.append(y_inter_l)
                        
                    ##plt.plot(np.array(wl_cort_int), np.array(fluxo_cort_int)/maior_fluxo, "r.")
                    ##plt.plot(np.array(lista_x_inter), np.array(lista_y_inter)/maior_fluxo, "b.")
                    ##plt.show()
                    
                    int_b_corr = intervalo_int - int_trap_b_red
                    arqSai.write("%-33.9s" %(str(int_b_corr)))
                    
                    int_simpson = (4*int_a_corr - int_b_corr)/3
                    arqSai.write("%-29.9s" %(str(int_simpson)))
                    
                    rel_err = np.fabs((int_simpson - int_b_corr))/int_simpson
                    arqSai.write("%-38s" %(str(rel_err)))
                    
                    
                    
            
            if prob == 1:
                
                limiteInf = float(input("\nDigite o limite inferior para integração: "))
                limiteSup = float(input("\nDigite o limite superior para integração: "))
                arqSai.write("%-7.7s" %(str(limiteInf)))
                arqSai.write(" - ")
                arqSai.write("%-15.7s" %(str(limiteSup)))
                
                wl_cort_int, fluxo_cort_int, maior_fluxo_4, menor_wl = corte_de_dados_lista(wl_cort_2, fluxo_cort_2, limiteInf, limiteSup)
                arqSai.write("%-27.9s" %(str(menor_wl)))
                lista_maior_fluxo.append(maior_fluxo_4)
                ponto_norm.append(wl_cort_int[0])
                ponto_norm.append(wl_cort_int[-1])
                lista_intervalos_norm.append(ponto_norm)
                ponto_norm = []
                
                variavel = int(input("\nDe qual dos intervalos deve ser tomado o maior fluxo?: "))
                maior_fluxo = lista_maior_fluxo[variavel - 1]
                int_norm = lista_intervalos_norm[variavel - 1]
                
                
                arqSai.write("%-.7s" %(str(int_norm[0])))
                arqSai.write(" - ")
                arqSai.write("%-33.7s" %(str(int_norm[1])))
                arqSai.write("%-27.9s" %(str(maior_fluxo)))
                
                plt.plot(wl_cort_int, fluxo_cort_int/maior_fluxo, "r.") ###
                plt.show() ###
                
                listaPhi, listaH = calcPhi(wl_cort_int, fluxo_cort_int)
                
                intervalo_pontos_int = intervalo_pontos
                if espac_igual == "s":
                    
                    intervalo_int = wl_cort_int[-1] -  wl_cort_int[0]
                    
                    int_trap_a_red = (trap_1(intervalo_pontos_int, fluxo_cort_int))/maior_fluxo
                    int_a_corr = intervalo_int - int_trap_a_red
                    arqSai.write("%-33.9s" %(str(int_a_corr)))
                    
                    int_trap_b_red = int_trap_a_red/2
                    ##lista_x_inter = []
                    ##lista_y_inter = []
                    intervalo_pontos_int /= 2
                    
                    for l in range(len(wl_cort_int) - 1):
                    
                        x_inter_l = wl_cort_int[l] + intervalo_pontos_int
                        ##lista_x_inter.append(x_inter_l)
                        posicao_x_inter_l = achaX(x_inter_l, wl_cort_int)
                        y_inter_l = poli(x_inter_l, posicao_x_inter_l, listaPhi, wl_cort_int, fluxo_cort_int, listaH)
                        int_trap_b_red += (intervalo_pontos_int*y_inter_l)/maior_fluxo
                        ##lista_y_inter.append(y_inter_l)
                        
                    ##plt.plot(np.array(wl_cort_int), np.array(fluxo_cort_int)/maior_fluxo, "r.")
                    ##plt.plot(np.array(lista_x_inter), np.array(lista_y_inter)/maior_fluxo, "b.")
                    ##plt.show()
                    
                    int_b_corr = intervalo_int - int_trap_b_red
                    arqSai.write("%-33.9s" %(str(int_b_corr)))
                    
                    int_simpson = (4*int_a_corr - int_b_corr)/3
                    arqSai.write("%-29.9s" %(str(int_simpson)))
                    
                    rel_err = np.fabs((int_simpson - int_b_corr))/int_simpson
                    arqSai.write("%-38s" %(str(rel_err)))
                    
                    #--------------------------------------------------------------------#
                    
                    intervalo_pontos_int = intervalo_pontos
                    limiteInf = menor_wl
                    
                    arqSai.write("%-7.7s" %(str(limiteInf)))
                    arqSai.write(" - ")
                    arqSai.write("%-33.7s" %(str(limiteSup)))
                    
                    wl_cort_int_esp, fluxo_cort_int_esp, maior_fluxo_5, menor_wl = corte_de_dados_lista(wl_cort_2, fluxo_cort_2, limiteInf, limiteSup)
                    
                    plt.plot(wl_cort_int_esp, fluxo_cort_int_esp/maior_fluxo, "g.") ###
                    plt.show() ###
                    
                    primeiro_wl = wl_cort_int_esp[0]
                    lista_prov = []
                    for m in range(1, len(wl_cort_int_esp), 1):
                        
                        primeiro_wl -= intervalo_pontos
                        wl_cort_int_esp = np.append(primeiro_wl, wl_cort_int_esp)
                        lista_prov = [fluxo_cort_int_esp[m]] + lista_prov
                    
                    lista_prov = np.array(lista_prov)
                    fluxo_cort_int_esp = np.append(lista_prov, fluxo_cort_int_esp)
                    
                    listaPhi, listaH = calcPhi(wl_cort_int_esp, fluxo_cort_int_esp)
                    
                    intervalo_int = wl_cort_int_esp[-1] - wl_cort_int_esp[0]
                    
                    plt.plot(wl_cort_int_esp, fluxo_cort_int_esp/maior_fluxo, "b.")
                    plt.show()
                    
                    int_trap_a_red = (trap_1(intervalo_pontos_int, fluxo_cort_int_esp))/maior_fluxo
                    int_a_corr = intervalo_int - int_trap_a_red
                    arqSai.write("%-43.9s" %(str(int_a_corr)))
                    
                    int_trap_b_red = int_trap_a_red/2
                    ##lista_x_inter = []
                    ##lista_y_inter = []
                    intervalo_pontos_int /= 2
                    
                    for l in range(len(wl_cort_int_esp) - 1):
                    
                        x_inter_l = wl_cort_int_esp[l] + intervalo_pontos_int
                        ##lista_x_inter.append(x_inter_l)
                        posicao_x_inter_l = achaX(x_inter_l, wl_cort_int_esp)
                        y_inter_l = poli(x_inter_l, posicao_x_inter_l, listaPhi, wl_cort_int_esp, fluxo_cort_int_esp, listaH)
                        int_trap_b_red += (intervalo_pontos_int*y_inter_l)/maior_fluxo
                        ##lista_y_inter.append(y_inter_l)
                        
                    int_b_corr = intervalo_int - int_trap_b_red
                    arqSai.write("%-43.9s" %(str(int_b_corr)))
                    
                    int_simpson = (4*int_a_corr - int_b_corr)/3
                    arqSai.write("%-35.9s" %(str(int_simpson)))
                    
                    rel_err = np.fabs((int_simpson - int_b_corr))/int_simpson
                    arqSai.write("%-43s" %(str(rel_err)))
            
            if prob == 2:
                
                limiteInf = float(input("\nDigite o limite inferior para integração: "))
                limiteSup = float(input("\nDigite o limite superior para integração: "))
                arqSai.write("%-7.7s" %(str(limiteInf)))
                arqSai.write(" - ")
                arqSai.write("%-15.7s" %(str(limiteSup)))
                
                wl_cort_int, fluxo_cort_int, maior_fluxo_4, menor_wl = corte_de_dados_lista(wl_cort_2, fluxo_cort_2, limiteInf, limiteSup)
                arqSai.write("%-27.9s" %(str(menor_wl)))
                lista_maior_fluxo.append(maior_fluxo_4)
                ponto_norm.append(wl_cort_int[0])
                ponto_norm.append(wl_cort_int[-1])
                lista_intervalos_norm.append(ponto_norm)
                ponto_norm = []
                
                variavel = int(input("\nDe qual dos intervalos deve ser tomado o maior fluxo?: "))
                maior_fluxo = lista_maior_fluxo[variavel - 1]
                int_norm = lista_intervalos_norm[variavel - 1]
                
                arqSai.write("%-.7s" %(str(int_norm[0])))
                arqSai.write(" - ")
                arqSai.write("%-33.7s" %(str(int_norm[1])))
                arqSai.write("%-27.9s" %(str(maior_fluxo)))
                
                ###plt.plot(wl_cort_int, fluxo_cort_int/maior_fluxo, "r.") ###
                ###plt.show() ###
                
                
                listaPhi, listaH = calcPhi(wl_cort_int, fluxo_cort_int)
                
                intervalo_pontos_int = intervalo_pontos
                if espac_igual == "s":
                    
                    intervalo_int = wl_cort_int[-1] -  wl_cort_int[0]
                    
                    int_trap_a_red = (trap_1(intervalo_pontos_int, fluxo_cort_int))/maior_fluxo
                    int_a_corr = intervalo_int - int_trap_a_red
                    arqSai.write("%-33.9s" %(str(int_a_corr)))
                    
                    int_trap_b_red = int_trap_a_red/2
                    ##lista_x_inter = []
                    ##lista_y_inter = []
                    intervalo_pontos_int /= 2
                    
                    for l in range(len(wl_cort_int) - 1):
                    
                        x_inter_l = wl_cort_int[l] + intervalo_pontos_int
                        ##lista_x_inter.append(x_inter_l)
                        posicao_x_inter_l = achaX(x_inter_l, wl_cort_int)
                        y_inter_l = poli(x_inter_l, posicao_x_inter_l, listaPhi, wl_cort_int, fluxo_cort_int, listaH)
                        int_trap_b_red += (intervalo_pontos_int*y_inter_l)/maior_fluxo
                        ##lista_y_inter.append(y_inter_l)
                        
                    ##plt.plot(np.array(wl_cort_int), np.array(fluxo_cort_int)/maior_fluxo, "r.")
                    ##plt.plot(np.array(lista_x_inter), np.array(lista_y_inter)/maior_fluxo, "b.")
                    ##plt.show()
                    
                    int_b_corr = intervalo_int - int_trap_b_red
                    arqSai.write("%-33.9s" %(str(int_b_corr)))
                    
                    int_simpson = (4*int_a_corr - int_b_corr)/3
                    arqSai.write("%-29.9s" %(str(int_simpson)))
                    
                    rel_err = np.fabs((int_simpson - int_b_corr))/int_simpson
                    arqSai.write("%-38s" %(str(rel_err)))
                    
                    #--------------------------------------------------------------------#
                    
                    intervalo_pontos_int = intervalo_pontos
                    limiteSup = menor_wl
                    
                    arqSai.write("%-7.7s" %(str(limiteInf)))
                    arqSai.write(" - ")
                    arqSai.write("%-33.7s" %(str(limiteSup)))
                    
                    wl_cort_int_esp, fluxo_cort_int_esp, maior_fluxo_5, menor_wl = corte_de_dados_lista(wl_cort_2, fluxo_cort_2, limiteInf, limiteSup)
                    
                    ###plt.plot(wl_cort_int_esp, fluxo_cort_int_esp/maior_fluxo, "g.") ###
                    ###plt.show() ###
                    
                    ultimo_wl = wl_cort_int_esp[-1]
                    lista_prov = []
                    for m in range(-2, -len(wl_cort_int_esp) - 1, -1):
                        ultimo_wl += intervalo_pontos
                        wl_cort_int_esp = np.append(wl_cort_int_esp, ultimo_wl)
                        lista_prov.append(fluxo_cort_int_esp[m])
                    
                    lista_prov = np.array(lista_prov)
                    fluxo_cort_int_esp = np.append(fluxo_cort_int_esp, lista_prov)
                    
                    listaPhi, listaH = calcPhi(wl_cort_int_esp, fluxo_cort_int_esp)
                    
                    intervalo_int = wl_cort_int_esp[-1] - wl_cort_int_esp[0]
                    
                    plt.plot(wl_cort_int_esp, fluxo_cort_int_esp/maior_fluxo, "b-")
                    plt.show()
                    
                    int_trap_a_red = (trap_1(intervalo_pontos_int, fluxo_cort_int_esp))/maior_fluxo
                    int_a_corr = intervalo_int - int_trap_a_red
                    arqSai.write("%-43.9s" %(str(int_a_corr)))
                    
                    int_trap_b_red = int_trap_a_red/2
                    ##lista_x_inter = []
                    ##lista_y_inter = []
                    intervalo_pontos_int /= 2
                    
                    for l in range(len(wl_cort_int_esp) - 1):
                    
                        x_inter_l = wl_cort_int_esp[l] + intervalo_pontos_int
                        ##lista_x_inter.append(x_inter_l)
                        posicao_x_inter_l = achaX(x_inter_l, wl_cort_int_esp)
                        y_inter_l = poli(x_inter_l, posicao_x_inter_l, listaPhi, wl_cort_int_esp, fluxo_cort_int_esp, listaH)
                        int_trap_b_red += (intervalo_pontos_int*y_inter_l)/maior_fluxo
                        ##lista_y_inter.append(y_inter_l)
                    
                    int_b_corr = intervalo_int - int_trap_b_red
                    arqSai.write("%-43.9s" %(str(int_b_corr)))
                    
                    int_simpson = (4*int_a_corr - int_b_corr)/3
                    arqSai.write("%-35.9s" %(str(int_simpson)))
                    
                    rel_err = np.fabs((int_simpson - int_b_corr))/int_simpson
                    arqSai.write("%-43s" %(str(rel_err)))
        arqSai.write("\n")
        
    arqSai.close()
    arqEntra.close
    
        
    
def trap_1(intervalo, lista_y):
    """
    Método para abscissas igualmente espaçadas.
    """
    int_trap = 0
    for i in range(len(lista_y) - 1):
        trap_i = (lista_y[i] + lista_y[i + 1])*intervalo/2
        int_trap += trap_i
        
    return int_trap
    
def trap_2(lista_x, lista_y):
    """
    Método para abscissas não igualmente espaçadas.
    """
    int_trap = 0
    for i in range(len(lista_x) - 1):
        intervalo_i = lista_x[i + 1] - lista_x[i]
        trap_i = (lista_y[i] + lista_y[i + 1])*intervalo_i/2
        int_trap += trap_i
        
    return int_trap

def gera_pontos_interpolacao(listaX, div_int):
    
    saida = "ab2.txt"
    arqSai = open(saida, 'w', encoding = 'utf - 8')
    listaXInter = []
    xInf = listaX[0]
    xSup = listaX[-1]
    passo = (listaX[1] - listaX[0])/div_int
    saida = "ab2.txt"
    arqSai = open(saida, 'w', encoding = 'utf - 8')
    x = xInf
    
    while x <= xSup:
        arqSai.write(str(x))
        arqSai.write("\n")
        listaXInter.append(x)
        x += passo
        
    arqSai.close()
    
    return listaXInter

def calcPhi(listaAb, listaOr):
    """ (str) -> list, list, list, list
    Toma o nome de um arquivo contendo um conjunto de pontos [xi, yi] já
    ordenados de forma crescente para as abscissas e calcula os phi's
    correspondentes de uma interpolação por spline cúbica. Esses phi's são
    devolvidos em uma lista. Também devolve listas para as abscissas, as
    ordenadas, e para as quantidades h, necessárias para calcular o polinômio
    interpolante entre pontos.
    """
    
    listaH = []
    listaE = []
    listaU = [0]
    listaL = [0, 0]
    listaPhi = []
    listaY = [0]
    
    # Algumas das listas são inicializadas já com elementos para uma
    # melhor correspondência com a apostila de onde o método foi tirado. No
    # entanto, esses números não chegam de fato a interferir nas contas.
    
    n = len(listaAb)
    for i in range(n):
        
        listaPhi.append(0)
        
    if n > 2:
        
        # Essa condição é imposta porque, para o caso de menos de 2 pontos, a
        # interpolação não é válida.
        
        n = n - 1
        
        # Essa translação em n foi feita para traduzir os n's que seriam usados
        # aqui com os n's da apostila de onde o método foi tirado.
        
        for i in range(0, n, 1):
            hi = float(listaAb[i + 1]) - float(listaAb[i])
            listaH.append(hi)
            ei = 6*(float(listaOr[i + 1]) - float(listaOr[i]))/hi
            listaE.append(ei)
            
        u1 = 2*(float(listaH[0]) + float(listaH[1]))
        listaU.append(u1)
        for j in range(2, n, 1):
            uj = 2*(listaH[j - 1] + listaH[j]) - ((listaH[j - 1])**2)/listaU[j - 1]
            listaU.append(uj)
            lj = float(listaH[j - 1])/float(listaU[j - 1])
            listaL.append(lj)
        
        y1 = listaE[1] - listaE[0]
        listaY.append(y1)
        for k in range(2, n, 1):
            yk = listaE[k] - listaE[k - 1] - listaL[k]*listaY[k - 1]
            listaY.append(yk)
        
        phiUlt = listaY[-1]/listaU[-1]
        listaPhi[n - 1] = phiUlt
        for z in range(n - 2, 0, -1):
            phiz = (listaY[z] - listaH[z]*listaPhi[z + 1])/listaU[z]
            listaPhi[z] = phiz
    
    return listaPhi, listaH

def achaX(x, listaX):
    """ (float, list) -> int
    Esse programa toma uma tabela de abscissas ordenada de forma crescente e um
    número x e retorna um número entre 1 e n - 1 caso x1 <= x <= xn, 0 caso
    x < x1 e n caso x > xn.
    """
    
    n = len(listaX)
    if x < float(listaX[0]):
        posicao = 0
    elif x > float(listaX[n - 1]):
        posicao = n
    else:
        iInf = 0
        iSup = n - 1
        while (iSup - iInf) > 1:
            iComp = (iSup + iInf) // 2
            xi = float(listaX[iComp])
            if x < xi:
                iSup = iComp
            else:
                iInf = iComp
                
            # Aqui, o método da bisseção é utilizado, de forma a reduzir a
            # quantidade de passos necessários para encontrar o intervalo ao
            # qual x pertence. Nele, x é comparado com o valor do meio de um
            # intervalo, x0. Se x >= x0, o novo intervalo tem como limite
            # inferior x0. Se x < x0, o novo intervalo tem como limite superior
            # x0. Então, um novo x0 é tomado desse novo intervalo, e o processo
            # se repete.
            
        posicao = iInf + 1
    
    return posicao

def poli(x, posicaoX, listaPhi, listaX, listaY, listaH):
    """ (int, int, list, list, list) -> float
    Esse programa calcula o valor de y(x) baseado em uma interpolação por spline
    cúbica.
    """
    
    phiInf = listaPhi[posicaoX - 1]
    phiSup = listaPhi[posicaoX]
    xInf = float(listaX[posicaoX - 1])
    xSup = float(listaX[posicaoX])
    yInf = float(listaY[posicaoX - 1])
    ySup = float(listaY[posicaoX])
    hInf = float(listaH[posicaoX - 1])
    
    t1 = (phiInf*(xSup - x)**3)/(6*hInf)
    t2 = (phiSup*(x - xInf)**3)/(6*hInf)
    t3 = ((yInf/hInf) - (hInf*phiInf/6))*(xSup - x)
    t4 = ((ySup/hInf) - (hInf*phiSup/6))*(x - xInf)
    
    y = t1 + t2 + t3 + t4
    
    return y

def corte_de_dados_lista(lista_x_dados, lista_y_dados, limiteInf, limiteSup):
    """
    """
    
    n = len(lista_x_dados)
    maior_y = 0
    menor_y = sys.float_info.max
    menor_x = 0
        
    atingiuLimiteInf = False
    atingiuLimiteSup = False
    lista_x_cort = []
    lista_y_cort = []
        
    k = 0
    x_k = lista_x_dados[0]

    if x_k > limiteSup:
            
        atingiuLimiteSup = True
            
    while k < n and not atingiuLimiteSup:
                
        while k < n and not atingiuLimiteInf:
                    
            x_k = lista_x_dados[k]
                    
            if (x_k - limiteInf) >= 0:
                        
                atingiuLimiteInf = True
                        
            else:
                        
                k += 1
                        
        while k < n and atingiuLimiteInf and not atingiuLimiteSup:
             
            x_k = lista_x_dados[k]
             
            if x_k > limiteSup:
                 
                atingiuLimiteSup = True
                 
            else:
                 
                lista_x_cort.append(lista_x_dados[k])
                lista_y_cort.append(lista_y_dados[k])
                    
                if lista_y_dados[k] > maior_y:
                    
                    maior_y = lista_y_dados[k]
                
                if lista_y_dados[k] < menor_y:
                    
                    menor_x = lista_x_dados[k]
                    menor_y = lista_y_dados[k]
                
                k += 1
        
    lista_x_cort = np.array(lista_x_cort)
    lista_y_cort = np.array(lista_y_cort)
        
    return lista_x_cort, lista_y_cort, maior_y, menor_x


main()