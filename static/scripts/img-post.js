document.addEventListener('DOMContentLoaded', () => {
    const postImageButton = document.getElementById('postImageButton');

    postImageButton.addEventListener('click', () => {
        const base64Image = sessionStorage.getItem('uploadedImage');

        if (!base64Image) {
            alert('Por favor selecciona y guarda una imagen antes de enviarla.');
            return;
        }

        fetch('/upload', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: base64Image }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.redirect_url) {
                    window.location.href = data.redirect_url; // Redirigir al cliente
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => console.log('Error:', error));
    });
});
