package idiomadosistema;

import java.util.Locale;

public class IdiomaDoSistema {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Locale currentLocale = Locale.getDefault();
		String language = currentLocale.getLanguage();
		System.out.println("O idioma atual do sistema operacional é: " + language);
	}

}
