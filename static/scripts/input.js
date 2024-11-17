document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('fileInput');
    const placeholderImage = document.getElementById('placeholder');

    fileInput.addEventListener('change', (event) => {
        const file = event.target.files[0];

        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const base64Image = reader.result;
                sessionStorage.setItem('uploadedImage', base64Image);
                placeholderImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});
