<!-- Aula 2 -->

<?php
class Pessoa {
    public $nome;
    public $idade;

    public function Falar (){
        echo $this->nome. " de " .$this->idade. " acabou de falar";
    }
}

$rodrigo = new Pessoa ();
$rodrigo->nome = "Rodrigo Santos de Oliveira";
$rodrigo->idade = 25;
$rodrigo->Falar();

?>


<!-- Aula 3 -->
