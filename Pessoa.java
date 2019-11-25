public class Pessoa{
    protected String nome;
    protected String data_de_nascimento;
    public Pessoa(String nome,String data){
        this.nome=nome;
        data_de_nascimento=data;
    }
    public String getnome(){
        return this.nome;
    }
    public String getdate(){
        return this.data_de_nascimento;
    }
    public String toString(){
        return ("nome: "+ nome+"\n"+ "Data de nascimento: " + data_de_nascimento);
    }
}
