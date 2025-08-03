
function getValues() {
    const volume = parseFloat(document.getElementById('volume').value);
    const density = parseFloat(document.getElementById('density').value);
    const temperature = parseFloat(document.getElementById('temperature').value);

    if (isNaN(volume) || isNaN(density) || isNaN(temperature) || isNaN(vcf)) {
        alert("Please enter valid numbers for all fields.");
        return;
    }

    return { volume, density, temperature};
}


