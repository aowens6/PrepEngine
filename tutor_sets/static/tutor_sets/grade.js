function verify(){
    var radios = document.getElementsByTagName('input');
    var explanation = document.getElementById('explanation');

    var value;

    for (var i = 0; i < radios.length; i++) {
        if (radios[i].type === 'radio' && radios[i].checked) {

            value = radios[i].value;

            if (value == "True"){
                alert('Correct!');
            }else{
                alert('Not quite');
            }
        }
        explanation.style.display = "block"
    }

}