public class Main {
    public static void main( String[] args ) {
        var myList = new LinkedList();
        myList.addLast( 10 );
        myList.addLast( 20 );
        myList.addLast( 30 );
        myList.removeLast();
        System.out.println(myList);
        System.out.println( myList.contains( 10 ) );
    }
}