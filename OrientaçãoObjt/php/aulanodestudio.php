<!-- Aula 2 class atributos e metodos-->

<?php
// Definindo estrutura do objeto 
class Pessoa {
    public $nome; //Atributo
    public $idade; //Atributo

    public function Falar (){  //Metodo / Função 
        echo $this->nome. " de " .$this->idade. " acabou de falar";
    }
}

//Instanciando uma class
$rodrigo = new Pessoa ();  //Rodrigo é um objeto que contem dois atributos e um metodo
$rodrigo->nome = "Rodrigo Santos de Oliveira";
$rodrigo->idade = 25;
$rodrigo->Falar();

?>
<!-- Aula 3 -->

<?php

    echo "</br>";
    class Login {
        //public $email;
        //public $senha;

        private $email; //Se estiver privado, não será acessivel fora da class
        private $senha;

        public function getEmail() { //Pega o atributo
            return $this->email;
        }

        public function setEmail($e) { //Atribui o valor para o atributo
            $this->email = $e;
        }

        public function getSenha() { //Pega o atributo
            return $this->senha;
        }

        public function setSenha($s) { //Atribui o valor para o atributo
            $this->senha = $s;
        }



        public function Logar(){
            if($this->email == "teste@teste@gmail.com" and $this->senha == "12345" ):
                echo "Logado com sucesso";
            else:
            echo "Dados invalidos";
            endif;
        }
    }

    $logar = new login();
    $logar->setEmail("teste@teste@gmail.com");
    $logar->setSenha("12345");
    $logar->logar();
    echo "</br>";
    echo $logar->getEmail();
    
?>