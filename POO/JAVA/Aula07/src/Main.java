/**
 * Classe princial do exercício do professor Guanabara
 * @author 069547631
 * @version 1.00
 * @since 09 - maio - 2023
 */
public class Main {
    public static void main(String[] args) {
        Lutador l[] = new Lutador[6]; // Vetor para fazer a declaração de vários de uma só vez
        l[0] = new Lutador("Pretty Body", "França", 31,
                1.75f, 68.9f, 11, 2, 1);
        l[1] = new Lutador("Putscript", "Brasil", 29,
                1.68f, 57.8f, 14, 2, 3);
        l[2] = new Lutador("Snapshadow", "EUA", 35,
                1.65f, 80.9f, 12, 2, 1);
        l[3] = new Lutador("Dead Code", "Austrália", 28,
                1.93f, 81.6f, 13, 0, 2);
        l[4] = new Lutador("UFOCobol", "Brasil", 37,
                1.70f, 119.3f, 5, 4, 3);
        l[5] = new Lutador("Nerdaart", "EUA", 30,
                1.81f, 105.7f, 12, 2, 4);

//        for (Lutador lutador:l){ // For para fazer a apresentação dos lutadores
//            lutador.apresentar();
//            lutador.status();
//        }
        
        Luta uec = new Luta();
        uec.marcarLuta(l[0], l[1]);
        uec.lutar();
    }
}
