public class Aluno extends Pessoa{
    // A classe que estiver à esquerda da palavra extends é a classe filha
    // que recebe herança da classe à direita de extends
    private int mat;
    private String curso;

    public void cancelarMatr(){
        System.out.println("Matrícula será cancelada!");
    }

    public int getMat() {
        return mat;
    }

    public void setMat(int mat) {
        this.mat = mat;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }
}
