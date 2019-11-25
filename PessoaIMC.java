public abstract class PessoaIMC extends Pessoa{
    protected double peso;
    protected double altura;
    public PessoaIMC(String nome,String data, double peso,double altura){
        super(nome,data);
        this.peso=peso;
        this.altura=altura;
        }
    public double getpeso(){
        return peso;
    }
    public double getaltura(){
        return altura;
    }
    public void setpeso(double peso){
        this.peso=peso;
    }
    public void setaltura(double altura){
        this.altura=altura;
    }
    protected double calculaIMC(double altura, double peso){
        return (peso/(altura*altura));
    }
    public abstract String  resultIMC();

    public String toString(){
        return (super.toString()+"\npeso: "+ peso+"\nAltura: "+altura+"\n");
    }
}
