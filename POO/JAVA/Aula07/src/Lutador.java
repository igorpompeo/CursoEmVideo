/**
 * Classe Lutador da Aula07 com o professor Guanabara - Curso em vídeo
 * @author 069547631
 * @version 1.00
 * @since 09 - maio - 2023
 */
public class Lutador {
    // Atributos
    private String nome, nacionalidade, categoria;
    private int idade, vitorias, derrotas, empates;
    private float peso, altura;

    // Métodos Públicos
    public void apresentar(){
        System.out.println("--------------------------------------------");
        System.out.print("Senhoras e Senhores, lhes apresento o lutador " + this.getNome());
        System.out.println(", com sua nacionalidade " + this.getNacionalidade() + ".");
        System.out.print("Tendo seus " + this.getIdade() + " anos");
        System.out.print(", com " + this.getAltura() + " m de altura");
        System.out.println(", pesando apenas " + this.getPeso() + " Kg.");
        System.out.print("Já ganhou " + this.getVitorias() + " vitórias");
        System.out.print(", tendo perdido apenas " + this.getDerrotas() + " derrotas");
        System.out.println(" e com seus pequenos" + this.getEmpates() + " empates.");
    }
    public void status(){
        System.out.println("--------------------------------------------");
        System.out.print(this.getNome());
        System.out.print(", é um peso " + getCategoria());
        System.out.print(", ganhou " + this.getVitorias() + " vezes");
        System.out.print(", perdeu " + this.getDerrotas() + " vezes");
        System.out.println(", empatou " + this.getEmpates() + " vezes.");
    }
    public void ganharLuta(){
        this.setVitorias(this.getVitorias() + 1);
    }
    public void perderLuta(){
        this.setVitorias(this.getVitorias() - 1);
    }
    public void empatarLuta(){
        this.setEmpates(this.getEmpates() + 1);
    }

    // Métodos Especiais
    public Lutador(String nome, String nacionalidade, int idade, float altura,
                   float peso, int vitorias, int derrotas, int empates) {
        this.nome = nome;
        this.nacionalidade = nacionalidade;
        this.idade = idade;
        this.altura = altura;
        this.setPeso(peso);
        this.vitorias = vitorias;
        this.derrotas = derrotas;
        this.empates = empates;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    public String getCategoria() {
        return categoria;
    }

    private void setCategoria() {
        if (getPeso() < 52.2) {
            this.categoria = "Inválido";
        } else if (getPeso() <= 70.3) {
            this.categoria = "Leve";
        } else if (getPeso() <= 83.9) {
            this.categoria = "Médio";
        } else if (getPeso() <= 120.2) {
            this.categoria = "Pesado";
        } else {
            this.categoria = "Inválido";
        }
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public int getVitorias() {
        return vitorias;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }

    public float getPeso() {
        return peso;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }

    public float getAltura() {
        return altura;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }
}
