// Load data from API
async function loadData() {
    try {
        const response = await fetch('/api');
        const data = await response.json();
        console.log('Data loaded:', data);
        displayData(data);
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

// Display data in the dashboard
function displayData(data) {
    const dataDisplay = document.getElementById('data-display');
    if (dataDisplay) {
        dataDisplay.innerHTML = `<p>${JSON.stringify(data)}</p>`;
    }
}

// Initialize dashboard on page load
document.addEventListener('DOMContentLoaded', () => {
    loadData();
});