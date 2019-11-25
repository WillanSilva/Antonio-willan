import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
public class EXE2{
    public  static ArrayList lista= new ArrayList();
    public static int tamanho;
    public static int tam() {
       	String aux;
	    try{
            System.out.print("\nDigite o numero de pessoas: ");
            BufferedReader nr0 = new BufferedReader(new InputStreamReader(System.in));
            tamanho = Integer.parseInt(aux = nr0.readLine());
        }
        catch(IOException E){
            System.out.println("\nerro digite novamente!");
        }
        catch(NumberFormatException E){
            System.out.println("\nerro digite um valor numerico!");
            tam();
        }
        return tamanho;
    }
    public ArrayList get(){
        return lista;
    }
    public static void EXE21() {
        String nome;
        String data;
        String aux;
        int numero;
        double peso,altura;
        BufferedReader nr = new BufferedReader(new InputStreamReader(System.in));
        try {
            boolean h=false, m = false;
            System.out.print("inserir homem(h) ou mulher(m)?");
            aux = nr.readLine();

            if (aux.equalsIgnoreCase("h")) {
                h=true;
            }
            else if(aux.equalsIgnoreCase("m")){
                m=true;
            }
            else{
                System.out.println("\naqui-->"+aux);
                System.out.println("\nERRO NA ESCOLHA ! ");
                System.out.println("\ntente novamente!\n ");
                EXE21();
            }
            System.out.print("Digite o nome: ");
            nome = nr.readLine();
            System.out.print("Digite a data: ");
            data = nr.readLine();
            System.out.print("Digite o peso: ");
            aux = nr.readLine();
            peso = Double.parseDouble(aux);
            System.out.print("Digite a altura: ");
            aux = nr.readLine();
            altura = Double.parseDouble(aux);
            if (h){
                homem instacia=new homem(nome,data,peso,altura);
                lista.add(instacia);
            }
            else if(m){
                mulher instancia = new mulher(nome,data,peso,altura);
                lista.add(instancia);
            }

        } catch (Exception e) {
            System.out.println("ERRO" + e);
            System.out.println("TENTE MAIS UMA VEZ!\n");
            EXE21();
        }
    }
    public static void main(String[] args) {
        int n=tam();
        for(int i=0;i<tamanho;i++){
            EXE21();
        }
        for(int s=0;s<tamanho;s++){
            System.out.println("\n"+lista.get(s));
        }
    }
}
