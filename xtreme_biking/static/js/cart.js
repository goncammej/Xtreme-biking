var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function () {
		var productId = this.dataset.product
		var action = this.dataset.action
		var redirect = this.dataset.redirect
		var quantity = parseInt(this.dataset.quantity)
		var availability = parseInt(this.dataset.availability)
		console.log(availability)
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser') {
			addCookieItem(productId, action, redirect, quantity, availability)
		} else {
			updateUserOrder(productId, action, redirect, quantity, availability)
		}
	})
}

function updateUserOrder(productId, action, redirect, quantity, availability) {
	console.log('User is authenticated, sending data...')

	var url = '/update_item/'

	fetch(url, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': csrftoken,
		},
		body: JSON.stringify({ 'productId': productId, 'action': action, 'quantity': quantity})
	})
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			location.href = redirect
		});
}

function addCookieItem(productId, action, redirect, quantity, availability) {
	console.log('User is not authenticated')

	if (action == 'add') {
		if (cart[productId] == undefined) {
			cart[productId] = { 'quantity': 1 }

		} else {
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove') {
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0) {
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}

	if (action == 'delete') {
		delete cart[productId];
	}

	if (action == 'add-quantity') {
		if (cart[productId] == undefined) {
			cart[productId] = { 'quantity': quantity }

		} else {
			if (quantity + cart[productId].quantity <= availability) {
				cart[productId]['quantity'] += quantity
			} else {
				cart[productId]['quantity'] = availability
			}
		}
	}

	console.log('CART:', cart)
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

	location.href = redirect
}

function increaseCount(a, b, pid, availability) {
	var input = b.previousElementSibling;
	var value = parseInt(input.value, 10);
	
	value = isNaN(value) ? 0 : value;
	value++;
	if (value > availability) {
		value = availability;
	}
	input.value = value;
	updateAddToCartButtonQuantity(pid, value);
}
function decreaseCount(a, b, pid, availability) {
	var input = b.nextElementSibling;
	var value = parseInt(input.value, 10);
	if (value > 1) {
		value = isNaN(value) ? 0 : value;
		value--;
		input.value = value;
		updateAddToCartButtonQuantity(pid, value)
	}
}
function updateAddToCartButtonQuantity(button, quantity) {
	const addToCartButton = document.getElementById('add-cart-' + button);
	addToCartButton.setAttribute('data-quantity', quantity);
}