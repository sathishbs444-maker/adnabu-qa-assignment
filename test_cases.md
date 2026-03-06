# Test Cases – AdNabuTestStore

## a) Product Search

TC1 – Search with valid product name (Positive)
- Step: Enter a valid product name in the search bar.
- Expected Result: Relevant products should be displayed.

TC2 – Search with non-existing product (Negative)
- Step: Enter a product name that does not exist.
- Expected Result: System should show "No products found".

TC3 – Search with special characters (Edge Case)
- Step: Enter special characters like @#$%.
- Expected Result: System should handle input properly without crashing.


## b) Add to Cart

TC4 – Add product to cart successfully (Positive)
- Step: Select a product and click "Add to Cart".
- Expected Result: Product should be added to cart and cart count increases.

TC5 – Add out-of-stock product (Negative)
- Step: Try to add an out-of-stock product.
- Expected Result: System should show an "Out of Stock" message.

TC6 – Add same product multiple times (Edge Case)
- Step: Click "Add to Cart" multiple times.
- Expected Result: Cart should update quantity correctly.
