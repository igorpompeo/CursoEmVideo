public class Aula11 {
    public static void main(String[] args) {
        // Pessoa p1 = new Pessoa(); Não funciona pois a classe Pessoa é abstract (abstrata) e
        // classe abstrata não se instância
        /*Visitante v1 = new Visitante();
        v1.setNome("Igor");
        v1.setIdade(33);
        v1.setSexo("M");
        System.out.println(v1.toString());*/
        // Testando classe aluno
        Aluno a1 = new Aluno();
        a1.setNome("Igor");
        a1.setMatricula(1234);
        a1.setCurso("Informática");
        a1.setIdade(32);
        a1.setSexo("M");
        a1.pagarMensalidade();

        // Testando classe bolsista
        Bolsista b1 = new Bolsista();
        b1.setNome("Igor");
        b1.setMatricula(12345);
        b1.setBolsa(12.5f);
        b1.setSexo("M");
        b1.pagarMensalidade();

        // Testando classe professor
        Professor p1 = new Professor();
        p1.setNome("Igor");
        p1.setSexo("M");
        p1.setIdade(33);
        p1.setSalario(6000.00f);
        p1.aumento(0.3f);
        p1.setEspecialidade("Analista de sistemas");
        System.out.println(p1.toString());

        // Testando classe técnico
        Tecnico t1 = new Tecnico();
        t1.setNome("Igor");
        t1.setSexo("M");
        t1.setIdade(33);
        t1.setCurso("Analise de Sistemas");
        t1.setMatricula(11111);
        t1.setRegistroProfissional(123456789);
        t1.praticar();
    }
}
