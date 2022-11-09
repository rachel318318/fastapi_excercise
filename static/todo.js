function removeItem(todo) {
	var elem = document.getElementById(todo);
	
	elem.remove();
}

var instanceCount = 0;
function createRemoveBtn(itemId) {
	var delBtn = document.createElement("Button");
	instanceCount++;
	delBtn.id = "btn_" + instanceCount;
	delBtn.className = "done-btn";
	delBtn.onclick = function() {removeItem(itemId);removeItem(delBtn.id);};
	delBtn.innerText = "DONE";
	var todoListElement = document.getElementById("todo-list");
	todoListElement.appendChild(delBtn);
}


function addTodotoList() {
	var todoElement=document.getElementById("todo");
	var itemsList = document.getElementsByClassName("item");
	var valid = true;

	if (todoElement.value === '') {
		alert('Please add to do item');

		return;
	}

	for (var i = 0; i < itemsList.length; i++) {
		if (itemsList[i].innerHTML.toLowerCase() === todoElement.value.toLowerCase()) {
			alert(todoElement.value + " already exists!");
			valid = false;
		}
	}

	if (valid) {
		var newElement = document.createElement("li");
		instanceCount++;
		
		newElement.id = "todo_" + instanceCount;
		newElement.className = "item";
		newElement.innerText = todoElement.value;
		
		var todoListElement = document.getElementById("todo-list");
		todoListElement.appendChild(newElement);
		
		createRemoveBtn(newElement.id);
	}

	todoElement.value = '';
}