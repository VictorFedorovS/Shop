/* Добавить блок, если есть конкуренты сайты */
function Nado_Pokazivat(a) {
    var label = a;

    if (label=="Yes") {
        document.getElementById("Block_First_Concurent").style.display='block';
        document.getElementById("Block_Advantages").style.display='block';
        document.getElementById("Block_examples_of_advantages").style.display='block';
        document.getElementById("examples").checked = false;
        Vvod_First_Concurent.setAttribute('required', '');
        Vvod_Advantages.setAttribute('required','');
    } 
    
    if (label=="No") {
        document.getElementById("Block_First_Concurent").style.display='none';
        document.getElementById("Block_Advantages").style.display='none';
        document.getElementById("Block_examples_of_advantages").style.display='none';
        document.getElementById("examples").checked = false;
        document.getElementById("Vvod_First_Concurent").required = false;
        document.getElementById("Vvod_Advantages").required = false;
    } 
}

