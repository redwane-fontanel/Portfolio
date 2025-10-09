document.addEventListener("DOMContentLoaded", function () {
    const scheduleList = document.getElementById("schedule-list");
    
    // Generate hourly slots
    for (let hour = 8; hour <= 22; hour++) {
        const timeSlot = `${hour}:00 - ${hour + 1}:00`;
        const listItem = document.createElement("li");
        listItem.classList.add("list-group-item");
        
        const timeLabel = document.createElement("span");
        timeLabel.textContent = timeSlot;
        
        const inputField = document.createElement("input");
        inputField.setAttribute("type", "text");
        inputField.classList.add("form-control");
        inputField.setAttribute("placeholder", "Enter task...");
        inputField.addEventListener("change", function () {
            localStorage.setItem(timeSlot, inputField.value);
        });
        
        // Load saved data
        if (localStorage.getItem(timeSlot)) {
            inputField.value = localStorage.getItem(timeSlot);
        }
        
        listItem.appendChild(timeLabel);
        listItem.appendChild(inputField);
        scheduleList.appendChild(listItem);
    }
});
