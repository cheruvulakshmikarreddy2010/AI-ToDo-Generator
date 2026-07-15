console.log("Script Loaded");

document.getElementById("generateBtn").addEventListener("click", async function () {

    alert("Button clicked!");

    const goal = document.getElementById("goal").value;
    const deadline = document.getElementById("deadline").value;
    const priority = document.getElementById("priority").value;

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                goal,
                deadline,
                priority
            })
        });

        const data = await response.json();
        document.getElementById("taskList").innerHTML = `<pre>${data.tasks}</pre>`;

    } catch (err) {
        console.error(err);
        alert(err);
    }
});