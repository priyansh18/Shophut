var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener('click', function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log('ProductId:', productId, 'Action:', action);

    console.log('User', user);
    if (user == 'AnonymousUser') {
      addCookieItem(productId, action);
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function addCookieItem(productId, action) {
  console.log('Not Logged In.....');

  if (action == 'add') {
    console.log('erwesrwer', cart);
    if (cart[productId] == undefined) {
      console.log('WFEASR', cart[productId]);
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]['quantity'] += 1;
    }
  }
  if (action == 'remove') {
    cart[productId]['quantity'] -= 1;

    if (cart[productId]['quantity'] <= 0) {
      delete cart[productId];
    }
  }
  document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
  location.reload();
}

function updateUserOrder(productId, action) {
  var url = '/update_item/';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({ productId, action }),
  })
    .then((response) => response.json())
    .then((data) => location.reload());
}
