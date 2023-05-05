package aula02;
public class Aula02 {
    public static void main(String[] args) {
        Caneta c1 = new Caneta(); // criando o objeto - instância
        c1.cor = "Azul";
        c1.ponta = 0.5f;
        c1.tampar(); // metodo da caneta tampada
        c1.status(); // metodo que mostra o status da caneta
        c1.rabiscar(); // metodo que faz rabiscar
    }
}
