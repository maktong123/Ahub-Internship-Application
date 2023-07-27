let currentPage = 0;
const form = document.getElementById('myForm');
const fieldsets = form.getElementsByTagName('fieldset');
const translateAmount=100;
let translate=0;
function showPage(page){
    for (let i = 0; i < fieldsets.length; i++) {
        if (i === page) {
            translate += translateAmount;
            //fieldsets[i].style.transform= `translateX(${translate}%)`;
           fieldsets[i].style.display = 'block';

        }else{
             translate -= translateAmount;
            //fieldsets[i].style.transform= `translateX(${translate}%)`;

            fieldsets[i].style.display= 'none';
        }
    }
}
function nextPage(){
    if (currentPage < fieldsets.length -1 ) {
        currentPage++;
        showPage(currentPage);
    }
}
function previousPage() {
    if (currentPage > 0) {
        currentPage--;
        showPage(currentPage);
    }
}



showPage(currentPage);

function readITLetter(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#it_letter_preview').attr('src', e.target.result);
            $('#it_letter_preview').css('display', 'block');
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$('#upload_it_letter').change(function () {
    readITLetter(this);
});

function readPhoto(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#photo_preview').attr('src', e.target.result);
            $('#photo_preview').css('display', 'block');
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$('#upload_photo').change(function () {
    readPhoto(this);
});
