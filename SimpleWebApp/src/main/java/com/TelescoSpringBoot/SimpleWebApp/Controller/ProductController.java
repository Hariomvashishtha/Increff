package com.TelescoSpringBoot.SimpleWebApp.Controller;
import com.TelescoSpringBoot.SimpleWebApp.model.Product;
import com.TelescoSpringBoot.SimpleWebApp.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@RestController
@CrossOrigin // to handle the cors error
public class ProductController
{
    @Autowired
    ProductService productService;
   // @GetMapping("/products")
//    public List<Product> getAllProducts()
//    {
//        return  this.productService.getProduct();
//    }
    // use of the responseEntity because you want to send the status code to the api also
    @GetMapping("/products")
    public ResponseEntity<List<Product>> getAllProducts()
    {
        return  new ResponseEntity<List<Product>>(this.productService.getProduct(), HttpStatus.OK);
    }

    @GetMapping("/products/{prodId}")
    public  Product getProductById( @PathVariable  int prodId)
    {
        return this.productService.getProductById(prodId);
    }
//    @GetMapping("/products/{prodId}")
//    public ResponseEntity<Product> getAllProducts(@PathVariable int prodId)
//    {
//        Product product = this.productService.getProductById(prodId);
//        if(product!=null) return new ResponseEntity<>(product,HttpStatus.OK);
//        else              return new ResponseEntity<>(product,HttpStatus.OK);
//
//    }
    @PostMapping("/products")
    public void  addProduct( @RequestBody  Product newProd)
    {
         productService.addProduct(newProd);
    }
    @PutMapping("/products")
    public void updateProduct(@RequestBody Product prod)
    {
         productService.updateProduct(prod);
    }
    @DeleteMapping("/products/{prodId}")
    public void deleteProduct(@PathVariable int prodId)
    {
         productService.deleteProduct(prodId);
    }
}
