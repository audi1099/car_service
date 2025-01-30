document.addEventListener('DOMContentLoaded', function() {
    let servicesList = document.getElementById('services-list');
    const services = ["Замена масла", "Ремонт двигателя", "Диагностика"];

    services.forEach(service => {
        let item = document.createElement('p');
        item.textContent = service;
        servicesList.appendChild(item);
    });
});