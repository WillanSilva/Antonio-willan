public class mulher extends PessoaIMC {
    private  double classi;
    public mulher(String nome,String data,double  peso,double altura ){
        super(nome,data,peso,altura);
        classi=super.calculaIMC(peso,altura);
    }
    public String resultIMC(){
        if (classi<19){
            return ("abaixo do peso ideal");
        }
        else if(classi<=25.8){
            return("Peso ideal");
        }
        else return("acima do peso");
    }
    public String toString(){
        return super.toString()+"resultado: "+resultIMC()+"\n";
    }
}
