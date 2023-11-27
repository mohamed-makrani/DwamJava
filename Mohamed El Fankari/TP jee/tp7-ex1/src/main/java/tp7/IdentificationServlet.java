package tp7;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class IdentificationServlet
 */
@WebServlet("/Calcul")
public class IdentificationServlet extends HttpServlet {
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String login = request.getParameter("login");
        request.setAttribute("utilisateur_connecte", login);
        RequestDispatcher rd = request.getRequestDispatcher("accueil.jsp");
        rd.forward(request, response);
    }
}


