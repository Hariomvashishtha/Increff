package com.TelescoSpringBoot.SimpleWebApp.repository;

import com.TelescoSpringBoot.SimpleWebApp.model.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProductRepo extends JpaRepository<Product,Integer>
{
   @Query("SELECT p from Product p WHERE " +
   "LOWER(p.name) Like LOWER(CONACT('%',:keyword, '%')) OR " +
   ""
   )
   List<Product> searchProduct(String keyword);

}
