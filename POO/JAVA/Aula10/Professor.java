public class Professor extends Pessoa{
    private String especilidade;
    private double salario;

    public void receberAum(float aum){
        this.salario += aum;
    }

    public String getEspecilidade() {
        return especilidade;
    }

    public void setEspecilidade(String especilidade) {
        this.especilidade = especilidade;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}
