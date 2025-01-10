you  can pass the argument to the main function when you are compiling the file javac hello hariom
.add() method is used to add at the end of the arrayList 
.add(1,"hariom") add at the end  of the arrayList
.set(1,"Hariom") set  the value of the index 
.remove(1) -> remove the index element 
.remove("hello") will remove the first hello of the list 
.indexOf()-> to ge the index of the any element 
.length is used in the for loop for the  termination condition 
.size() can also be used   , .get() , .set(1,"Hariom") these are also other useful methods 


// how to apply the for each loop in the 
for(double number : numbers) {}

.concat() method is used for the addition in the strings
.equals() whether two variable are having equal value or not 
.compareTo() return the integer value diff between the two strings 
.charAt() is used for indexing in the string in the java 
.substring() method is used to find the substring in the index 
.toUpperCase() .toLowerCase() method is used 
every method in the math class  is the static method , so we can call them without creating the object 

static method can only interact with the static variable and static method
public static void myFirstStaticMethod(){
    // Some code here
  }

extends is used in inheritence for the classes 
super(30.0, 0.64, "flat", "rice flour"); this is basically used in the inheritence 



private  -> only class can modify the fields
nothing mention -< only class and package can modify 
public -< all
protected -< class, child , package , 

final methods are not overridden by the subclasses , its implementation should be remain throughout the inheritence 


// how to override the method in the oops
@override
public void cook()
{

}

// how to use try and catch block in the java 
try
{
    int ratio = length / width;
} 
catch (ArithmeticException e) 
{
    System.err.println("ArithmeticException: " + e.getMessage());
}

// decleration of the 2-d array 
int [][] v;  v = new int[row][col];  v = new int [][] {{},{}}
double [][] doubleValues  = {{},{}};

// accessing the  dimension for the 2-d array 
int rows = intMatrix.length;
int columns = intMatrix[0].length;

// apply for each loop in the 2-d array 
for (int[] row : binary) {
    for (int i: row) {
      onesCount += i;
    }
}


