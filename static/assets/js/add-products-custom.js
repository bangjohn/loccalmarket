(function () {
    "use strict"


    // $(document).ready(function () {
    //     $('#pilihan').on('input', function () {
    //         if ($(this).hasClass("active")) {
    //             // lakukan sesuatu jika elemen memiliki kelas
    //             console.log('true');
    //         } else {
    //             // lakukan sesuatu jika elemen tidak memiliki kelas
    //             console.log('false')
    //             $(this).addClass('active');
    //             // Get the element where the new row will be added.
    //             let div = $("#pilihan-variasi-container");
    //
    //             // Create the new row.
    //             let newRow = $("<div class='row mb-2'></div>");
    //             let inputGroup = $("<div class='input-group pilihan-variasi'></div>");
    //             let input = $("<input type='text' class='form-control form-pilihan-variasi' id='pilihan' style='margin-right: 10px;'></div>");
    //             let button = $("<button class='btn btn-outline-danger delete-button' type='button'> <i class='bx bx-trash'></i> </button>");
    //
    //             // Add the elements to the new row.
    //             newRow.append(inputGroup);
    //             inputGroup.append(input);
    //             inputGroup.append(button);
    //
    //             // Append the new row to the parent element.
    //             div.append(newRow);
    //         }
    //     })
    // });

    $(document).ready(function () {
        // Menangani peristiwa input pada elemen input-field yang ada saat ini
        $('#form-pilihan-variasi-1').on('input', '.form-pilihan-variasi', function () {
            var inputValue = $(this).val();

            if (inputValue !== '') {
                // Membuat elemen input baru
                let inputGroup = $("<div class='input-group pilihan-variasi mb-2'></div>");
                let input = $("<input type='text' class='form-control form-pilihan-variasi' id='pilihan' style='margin-right: 10px;'>");
                let inputGroupAppend = $("<div class='input-group-append'></div>");
                let button = $("<button class='btn btn-outline-danger delete-button disabled' type='button'> <i class='bx bx-trash'></i> </button>");

                // Menambahkan elemen ke dalam inputGroup
                inputGroup.append(input);
                inputGroup.append(inputGroupAppend);
                inputGroupAppend.append(button);

                // Menambahkan elemen input baru ke dalam kontainer
                $('#form-pilihan-variasi-1').append(inputGroup);

            }
        });
    });


    $(document).on('click', '.delete-button', function () {
        $(this).closest('.row.mb-2').remove();
    });

    $(document).ready(function () {
        $('#tambah-produk-submenu').children().addClass('active');

    });

})();