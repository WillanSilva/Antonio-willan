public class homem extends PessoaIMC{
    private double classi;
    public homem(String nome,String data,double  peso,double altura ){
        super(nome,data,peso,altura);
        classi=super.calculaIMC(altura,peso);
    }
    public String resultIMC(){;
        String peso;
        if (classi<20.7){
            peso="abaixo do peso ideal";
        }
        else if(classi<=26.4){
            peso="Peso ideal";
        }
        else{
            peso="acima do peso";
        }
    return peso;
    }
    public String toString(){
        return super.toString()+"resultado: "+resultIMC()+"\n";
    }
}
