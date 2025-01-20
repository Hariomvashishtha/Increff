// spring framework provide template for the jpa, jdbc , hibernate 
// jpa is used for the object relational mapping  ( java persistence api)
// jdbc is used for the database connection 
// hibernate is used for the object relational mapping ( simplfies the interaction betwen the java application and the database)
// / like for jdbc you do not have to write code for the connection and exception handling , closing connection ( you have to write code for query execution)
// / 
// / 
// / spring came to lightweight the java 

// client      ( controller ) ( to handle the request and response  of the client )
// service     ( service ) ( to handle the business logic )
// repository  ( dao ) ( to handle the data access )
// entity      ( model ) ( to represent the data )   


// controoler    service     repository    
// if controller wants to interact with the service(service methods) then it will need to craete the object for the serviec class
// similarly it goes for the service , if it wants to interact with the repository(repository methods) then it will need to craete the object for the repository class
// now if i tell you that hey devloper if you  focous only the business logic , let me handle this object creation 
// if you manage it , you have to manage the complete cycle for this (like creation and  destroying of the object )
// sometimes we have to craetion new object for every request , somethimes even we did not need multiple object for the same class
// that is some other is handling the object creation that is called inversion of control (ioc) principle .
// ioc is just the principle or philosophy , but how to implement it is the spring framework. then we need some technique to implement it.
// that is called dependency injection (di)
// dependency injection is the process of injecting the dependencies into the class (object creation)
// there are two types of dependency injection 1. constructor injection 2. setter injection
// constructor injection is the process of injecting the dependencies into the class using the constructor of the class
// setter injection is the process of injecting the dependencies into the class using the setter methods of the class
// field injection is the process of injecting the dependencies into the class using the field of the class
// example for constructor injection is  
// example for setter injection is 
// example for field injection is  , autowired annotation is used to inject the dependencies into the class using the field of the class
// public class MyService {
//     @Autowired
//     private MyRepository myRepository;
//     public void performService() {
//         // Use myRepository to perform some operations
//         myRepository.doSomething();
//     }
// }


// now suppose we  have 100 files of or 100 of classes , but we do not need object of all the classes , we do need only object for the 
// few classes so that we have to specify in  the config , may be some xml file 

// to run  your server , you need tomcat server for this (configure tomcat server)
// spring boot where  problem of configuartion is solved , run the project in just few minutes 

// deploy your code to the cloud we have to create the war file and deploy it to the cloud. this war file is called web archive file.
// then you have to give this war file to the tomcat server, to run it .
// what spring boot says if you want to devlop the web project you will get the embedded tomcat server in the spring boot