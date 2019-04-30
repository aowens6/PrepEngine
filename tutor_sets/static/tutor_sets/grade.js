function verify(){
    var radios = document.getElementsByTagName('input');
    var explanation = document.getElementById('explanation');

    var value;

    for (var i = 0; i < radios.length; i++) {
        if (radios[i].type === 'radio' && radios[i].checked) {

            value = radios[i].value;

            if (value == "True"){
                swal({
                  title: "Correct!",
                  icon: "success",
                  timer: 1500
                });
            }else{
                swal({
                  title: 'Not quite!',
                  icon: 'error',
                  timer: 1500
                })
            }
        }
        if (explanation !== null){
            explanation.style.display = "block"
        }
    }
}