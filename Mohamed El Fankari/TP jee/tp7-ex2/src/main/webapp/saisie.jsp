<%@ page contentType="text/html" %>
<!DOCTYPE html>
<html>
<head>
    <title>Calculatrice</title>
</head>
<body>
    <form action="Calcul" method="post">
        Entrez le premier op�rande: <input type="text" name="operande1" /><br>
        Entrez le deuxi�me op�rande: <input type="text" name="operande2" /><br>
        Choisissez l'op�ration:
        <select name="operation">
            <option value="+">Addition</option>
            <option value="-">Soustraction</option>
            <option value="*">Multiplication</option>
            <option value="/">Division</option>
        </select><br>
        <input type="submit" value="Calculer" />
    </form>

    <script>
        var message = '<%= request.getAttribute("message") %>';
        if (message !== null && message !== '') {
            alert(message);
        }
    </script>
</body>
</html>
