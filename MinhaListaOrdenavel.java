import java.util.*;
import java.io.*;
import java.lang.reflect.Executable;
public class MinhaListaOrdenavel implements Comparator{
    public static ArrayList<PessoaIMC> colecao = new ArrayList<PessoaIMC>();
    public void add1(PessoaIMC pessoa) {
        colecao.add(pessoa);
    }
   public PessoaIMC get(int i) {
        return colecao.get(i);
    }
    @Override
    public int compare (PessoaIMC p1, PessoaIMC p2){
        double pf1, pf2;
        pf2 = ( PessoaIMC ) p2.getPeso();
        pf1 = ( PessoaIMC ) p1.getPeso();
        return (int)Math.round (pf2 - pf1);   
    }
    /*
     * 1.Alfabetica (A-Z) 2.Alfabetica (Z-A) 3.Menor Peso 4.Maior Altura 5.Menor IMC
     */
    public static void ordena(ArrayList lista,int numero) {
        colec = lista;
        switch (numero) {
        case 1: //Alfabetica
           Collections.sort(colec,compare());

            break;
        case 2:   //Alfabetica Invertida
            Collections.sort(colec,compare());

            break;
        case 3: //Peso
            Collections.sort(colec,compare());
            
            break;
    }
    public static void main(String[] args) {
        // System.out.println("Digite adicionar: ");
        BufferedReader nr = new BufferedReader(new InputStreamReader(System.in));
        EXE2 eai = new EXE2();
        MinhaListaOrdenavel falai = new MinhaListaOrdenavel();
        eai.tam();
        int tamanho=eai.tamanho;
        for(int i=0;i<tamanho;i++){
            eai.EXE21();
        }
        colecao=eai.lista;
        System.out.println("Digite 1 ou 2");
        try{
            int i;
            i=Integer.parseInt(nr.readLine());
            falai.ordena(eai.lista,i);
        }
        catch(Exception E){
            System.out.println("Erro"+E);
        }
        System.out.print("DPS DE ORDENAR --------\n"+colecao);
    }
}