(function () {
    "use strict"

    // for product features
    var toolbarOptions = [
        [{'header': [1, 2, 3, 4, 5, 6, false]}],
        [{'font': []}],
        ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
        ['blockquote', 'code-block'],

        [{'header': 1}, {'header': 2}],               // custom button values
        [{'list': 'ordered'}, {'list': 'bullet'}],

        [{'color': []}, {'background': []}],          // dropdown with defaults from theme
        [{'align': []}],
        ['clean']                                         // remove formatting button
    ];
    var quill = new Quill('#product-features', {
        modules: {
            toolbar: toolbarOptions
        },
        theme: 'snow'
    });

    FilePond.registerPlugin(
        FilePondPluginImagePreview,
        FilePondPluginFileValidateSize,
        FilePondPluginFileValidateType,
        FilePondPluginImageCrop,
    )
    FilePond.setOptions({
        acceptedFileTypes: ['image/png', 'image/jpg', 'image/jpeg', 'image.webp'],
        imageCropAspectRatio: '1:1',
        imagePreviewHeight: 170,
        imageResizeTargetWidth: 200,
        imageResizeTargetHeight: 200,
        styleProgressIndicatorPosition: 'center',

        server: {
            process: {
                url: '/temp-image-upload/',
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken(),
                },
            },
            revert: {
                url: '/temp-image-delete/',
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCSRFToken()
                }
            },
        },
    });
    // for product images upload

    const Gambar1 = document.querySelector('.gambar1');
    const Gambar2 = document.querySelector('.gambar2');
    const Gambar3 = document.querySelector('.gambar3');
    FilePond.create(Gambar1,);
    FilePond.create(Gambar2,);
    FilePond.create(Gambar3,);

    const input = document.getElementById('myInput');
    const counter = document.getElementById('characterCount');
    input.addEventListener('input', updateCharacterCount);
    updateCharacterCount(); // Menjalankan fungsi saat halaman dimuat
    function updateCharacterCount() {
        const count = input.value.length;
        const maxLength = parseInt(input.getAttribute('maxlength'));
        counter.textContent = (count || 0) + '/' + maxLength;
    }

    function updateCharacterCount() {
        const count = input.value.length;
        const maxLength = parseInt(input.getAttribute('maxlength'));
        counter.textContent = count + '/' + maxLength;
    }


    function getCSRFToken() {
        const cookieValue = document.cookie.match(/(^|;) ?csrftoken=([^;]*)(;|$)/);
        return cookieValue ? cookieValue[2] : '';
    }

    document.getElementById('berat').addEventListener('keydown', function (event) {
        if (event.which === 38 || event.which === 40 || event.key === '.' || event.key === ',') {
            event.preventDefault();
        }
    });


})();