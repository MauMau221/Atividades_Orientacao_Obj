<?php 
    require 'funcionario.class.php';

    //Objeto 1
    $funcionario = new funcionario();
    $funcionario->setNome('Fulano');
    $funcionario->setSalarioBase(1000);
    $funcionario->setHorasExtras(10);
    $funcionario->setValorDaHora(20);

    echo $funcionario->getSalarioEfetivo();
    var_dump($funcionario);


    //Objeto 2
    $funcionario1 = new funcionario();
    $funcionario1->setNome('Fulano1');
    $funcionario1->setSalarioBase(3000);
    $funcionario1->setHorasExtras(10);
    $funcionario1->setValorDaHora(20);

    echo $funcionario1->getSalarioEfetivo();
    var_dump($funcionario1);
    //TAREFA DE CASA
    //Sempre que um funcionario tiver horas extras, ele também terá um aumento de 10% no salario base
?>