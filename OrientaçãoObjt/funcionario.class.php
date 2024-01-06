<?php 

class funcionario {
    private $nome;
    private $salarioBase;
    private $horasExtras;
    private $valorDaHora;


    public function setNome($nome) {
        $this->nome = $nome;
    } 

    public function setSalarioBase($base) {
        
        $this->salarioBase = $base + ($base * 0.10);  //Resultado exercicio 
    } 

    public function sethorasExtras($extras) {
        $this->horasExtras = $extras;
    } 
    
    public function setValorDaHora($valor) {
        $this->valorDaHora = $valor;
        
    } 

    public function getSalarioEfetivo() {
        return $this->salarioBase + ($this->horasExtras * $this->valorDaHora );
    } 

}

?>