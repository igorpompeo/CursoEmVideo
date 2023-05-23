import java.util.Random;

/**
 * Classe agregada de Lutador
 * @author 069547631
 * @version 1.00
 * @since 09 - maio - 2023
 */
public class Luta {
    // Atributos
    private Lutador desafiado, desafiante;
    private int rounds;
    private boolean aprovada;

    // Métodos públicos
    public void marcarLuta(Lutador l1, Lutador l2){
        if (l1.getCategoria() == l2.getCategoria()
                && l1.getNome() != l2.getNome()){
            this.aprovada = true;
            setDesafiado(l1);
            setDesafiante(l2);
        } else {
            aprovada = false;
            desafiado = null;
            desafiante = null;
        }
    }
    public void lutar(){
        if (aprovada){
            desafiado.apresentar();
            desafiante.apresentar();
            Random aleatorio = new Random();
            int limite = 3;
            int vencedor = aleatorio.nextInt(limite);
            switch (vencedor){
                case 0: //Empate
                    System.out.println("----------------------------");
                    System.out.println("Empatou!");
                    desafiado.empatarLuta();
                    desafiante.empatarLuta();
                    break;
                case 1: //Ganhou Desafiado
                    System.out.println("----------------------------");
                    System.out.println("O vencedor foi: " + desafiado.getNome());
                    desafiado.ganharLuta();
                    desafiante.perderLuta();
                    break;
                case 2: //Ganhou Desafiante
                    System.out.println("----------------------------");
                    System.out.println("O vencedor foi: " + desafiante.getNome());
                    desafiado.perderLuta();
                    desafiante.ganharLuta();
                    break;
            }
        } else {
            System.out.println("Luta não pode acontecer");
        }
    }

    // Métodos Especiais
    public void setDesafiado(Lutador dd){ this.desafiado = dd; }

    public Lutador getDesafiado(){ return desafiado; }

    public void setDesafiante(Lutador dd){ this.desafiante = dd; }

    public Lutador getDesafiante(){ return desafiante; }
}
