<?php 
    require 'funcionario.class.php';

    $funcionario = new funcionario();
    $funcionario->setNome('Fulano');
    $funcionario->setSalarioBase(1000);
    $funcionario->setHorasExtras(10);
    $funcionario->setValorDaHora(20);

    echo $funcionario->getSalarioEfetivo();

    //TAREFA DE CASA
    //Sempre que um funcionario tiver horas extras, ele também terá um aumento de 10% no salario base
?>