//Site base: https://rickandmortyapi.com/ //

let chamada = () =>{
    let epsodio = prompt('De qual epsodio você gostaria de exibir informações? ');

    fetch(`https://rickandmortyapi.com/api/character/${epsodio}`).then( retorno => retorno.json()).then( returnJson => document.body.innerHTML = 
    `<h1>${returnJson.name}</h1> <img src=${returnJson.image}>
    <p>Tipo: ${returnJson.type}</p>
    <p>Genero: ${returnJson.gender}</p>
    <p>Status: ${returnJson.status}</p>`,);




}
addEventListener('click',chamada)



//let proximaCarta = () => {
   // fetch(`https://www.deckofcardsapi.com/api/deck/${idBaralho}/draw/?count=1`).then( resposta => resposta.json()).then( dado => document.body.innerHTML = `<img src=${dado.cards[0].image}>` );
//}
//addEventListener('click',proximaCarta)

 