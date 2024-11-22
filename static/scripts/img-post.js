document.addEventListener('DOMContentLoaded', () => {
    const postImageButton = document.getElementById('postImageButton');

    postImageButton.addEventListener('click', () => {
        const base64Image = sessionStorage.getItem('uploadedImage');
        console.log(base64Image);
        if (!base64Image) {
            alert('Por favor selecciona y guarda una imagen antes de enviarla.');
            return;
        }

        fetch('/api/generate/output', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: base64Image }),
        })
        .then(response => {
            if (response.redirected) {
                // Si el backend redirige, cambia la ventana actual
                window.location.href = response.url;
            }
        })
        .catch(error => console.log('Error:', error));
    });
});
