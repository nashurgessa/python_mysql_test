document.getElementById("btnClick").addEventListener("click", addTodo);

function addTodo() {

	var textValue = document.getElementById("inputId").value;

	fetch("http://127.0.0.1:5001/todos", {
		method: "POST",
		headers: {"Content-Type": "application/json"},
		body: JSON.stringify(
			{
				'text': textValue
			}
		)
	})
	.then(response => response.json())
	.then(todo => {
		listDisplay(todo);
		document.getElementById("inputId").value = "";
	});
}


function listDisplay(todo) {
	var unOrderList = document.getElementById("unlist");
	var li = document.createElement('li');

	li.textContent = todo.text;
	unOrderList.appendChild(li);
}


function fetchTodos(){
	fetch("http://127.0.0.1:5001/todos")
	.then(response  => {
		if (response.ok){
			return response.json();
		} else {
			throw new Error("Connection wrong");
		}
	}).then(todos => {
		todos.forEach(todo => listDisplay(todo));
	}).catch(error => {
        console.error('Fetch error:', error);
    });
}

// retrieve
fetchTodos();

