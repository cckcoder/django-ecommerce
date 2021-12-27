let form = document.getElementById('payment-form');

form.addEventListener('submit', (elem) => {
  // Stripe payment record
  elem.preventDefault();
  window.location.replace("http://127.0.0.1:8000/payment/orderplaced/")
})
