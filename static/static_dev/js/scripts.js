$(document).ready(function (){
    // GET VALUES FROM PRODUCT.HTML ABOUT PRODUCT=======================================================================
    // START CODE==========================================================================
   var form = $('.form_buying_product');
   console.log(form);

   function basketUpdating(product_id, quantity, is_delete) {
       var data = {};
       // console.log(product_id, quantity, is_delete)
       data.product_id = product_id;
       data.product_quantity = quantity;
       data["csrfmiddlewaretoken"] = $('#csrf_getting_form [name="csrfmiddlewaretoken"]').val(); // csrf from navbar
       // console.log('csrf: '+data["csrfmiddlewaretoken"]);

       if (is_delete) {
           data["is_delete"] = true;
       }

       var url = form.attr("action");

       console.log(data)
       $.ajax({
           url: url,
           type: 'POST',
           data: data,
           cache: true,
           success: function (data){
                // console.log('OK');
                // console.log('products total number: '+data.products_total_number);  // get from order\views.py
               if (data.products_total_number || data.products_total_number == 0) {
                   $('#basket_total_number').text("("+data.products_total_number+")");  // throwing to navbar.html in <a href="">Кошик <span id="basket_total_amount"></span><span id="basket_total_number"></span></a>
                    // console.log(data.products)  // // get from order\views.py ---> return_dict['products'].append(product_dict)
                   $('.basket-items ul').html("");
                   $.each(data.products, function (k, v){
                       $('.basket-items ul').append('<li>'+v.product_name+'| '+v.product_quantity+' шт| '+v.product_total_price+'₴| '+
                           '<a class="delete-item" href="" data-product_id="'+v.product_id+'">X</a>'+'</li>');
                   });
               }

           },
           error: function (){
               // console.log('ERROR');
           }
       })
   }


   form.on('submit',function(e){
       // console.log('form_submit');
        var form = $(this);
        e.preventDefault();
        var form = $(this);
        var quantity = $('#quantity').val();
        var submit_btn = form.find($('.submit_btn'));
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name")
        var product_price = submit_btn.data("product_price")

        basketUpdating(product_id, quantity, is_delete=false)
    });
    // END CODE==================================================================================


    var basket = $('.basket-container');

    function shovingBasket(){
        $('.basket-items').removeClass('hidden');
    }

    // basket.on('click', function (e){
    //     e.preventDefault();
    //     shovingBasket();
    // });

    basket.mouseover(function (){
        shovingBasket();
    });

    // basket.mouseout(function (){
    //     $('.basket-items').addClass('hidden');
    // });

    $(document).on('click', '.delete-item', function (e){
        e.preventDefault();
        product_id = $(this).data("product_id");
        quantity = 0;
        basketUpdating(product_id, quantity, is_delete=true)
    });

    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function (){
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log('total_order_amount: '+total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    }

    $(document).on('change', '.product-in-basket-quantity', function (){
        console.log('product-in-basket-quantity');
        var current_quantity = $(this).val();
        console.log('current_quantity: '+current_quantity);
        var current_price_tr = $(this).closest('tr');
        // console.log('current_price_tr: '+current_price_tr);
        var current_price = parseFloat(current_price_tr.find('.price-per-item').text()).toFixed(2);
        // var current_price = parseFloat($('.price-per-item').text()).toFixed(2);
        console.log('current_price: '+current_price);
        var total_amount = parseFloat(current_quantity * current_price).toFixed(2);
        console.log('total_amount: '+total_amount);
        current_price_tr.find('.total-product-in-basket-amount').text(total_amount);

        calculatingBasketAmount();
    });

    // console.log('визов функції '+calculatingBasketAmount())
    calculatingBasketAmount();
});


// NAVBAR============================================================================================
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
// END CODE============================================================================================


