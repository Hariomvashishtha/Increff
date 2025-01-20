package com.TelescoSpringBoot.SimpleWebApp.model;
import com.fasterxml.jackson.annotation.JsonFormat;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Component;

@Component
@Entity //  if you want to work orm or hibernate then add this class also to it , for creating the table
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Product
{
   @Id // this is pk, you have to mention pk for every primary key
   @GeneratedValue(strategy = GenerationType.IDENTITY) // auto generated primary key
    private int prodId;
    private  String prodName ;
    private int price ;

//    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "dd-MM-yyyy")
//    private String createdDate; FOR CONVERSION OF DATE IN STRING AND DESIRED FORMAT
//    @Lob
//    private  byte[] imageDate;
    public  Product(){}

    public int getProdId() {
        return prodId;
    }

    public void setProdId(int prodId) {
        this.prodId = prodId;
    }

    public String getProdName() {
        return prodName;
    }

    public void setProdName(String prodName) {
        this.prodName = prodName;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public Product(int prodId, String prodName, int price)
    {
        this.prodId = prodId;
        this.prodName = prodName;
        this.price = price;
    }

    @Override
    public String toString() {
        return "Product{" +
                "prodId=" + prodId +
                ", prodName='" + prodName + '\'' +
                ", price=" + price +
                '}';
    }
    // if you want to pass  this object  in the api body , then write the tostring method for this
    // if you are not using the lombok methods

    
}
