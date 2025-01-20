package com.TelescoSpringBoot.SimpleWebApp.service;

import com.TelescoSpringBoot.SimpleWebApp.model.Product;
import com.TelescoSpringBoot.SimpleWebApp.repository.ProductRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.ArrayList;
import java.util.Arrays;
import  java.util.List;
@Service
public class ProductService
{
    @Autowired
    ProductRepo repo;
//     List<Product> products = new ArrayList<>(Arrays.asList(
//                              new Product(101,"Iphone",50000),
//                              new Product(102,"Samsung",30000),
//                              new Product(103,"Vivo",10000)));

    public  List<Product> getProduct()
    {
//      return products;
        return repo.findAll();
    }

    public Product getProductById(int prodId)
    {
//        return products.stream()
//                .filter(p -> p.getProdId() == prodId)
//                .findFirst()
//                .orElse(new Product(-1,"No Item",0));
        return repo.findById(prodId).orElse(new Product(-1,"no item found",-1));


    }
    public  void addProduct(Product newProd)
    {
//        products.add(newProd);
        repo.save(newProd);

    }

    public void updateProduct(Product prod)
    {
//        int index=0;
//        for(int i=0;i<products.size();i++)
//        {
//             if(products.get(i).getProdId()==prod.getProdId())
//             {
//                 index =i;
//                 break;
//             }
//        }
//        products.set(index,prod);
        repo.save(prod);
        // it will check if it is already there then update this otherwise we will save this.

    }

    public void deleteProduct(int prodId)
    {
//        int index=0;
//        for(int i=0;i<products.size();i++)
//        {
//            if(products.get(i).getProdId()==prodId)
//            {
//                index =i;
//                break;
//            }
//        }
//        products.remove(index);
        repo.deleteById(prodId);

    }
}
