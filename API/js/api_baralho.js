let idBaralho = 0;

fetch("https://www.deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").then( retorno => retorno.json()).then( dado => idBaralho = dado.deck_id  );



let proximaCarta = () => {
    fetch(`https://www.deckofcardsapi.com/api/deck/${idBaralho}/draw/?count=1`).then( resposta => resposta.json()).then( dado => document.body.innerHTML = `<img src=${dado.cards[0].image}>` );
}
addEventListener('click',proximaCarta)

 