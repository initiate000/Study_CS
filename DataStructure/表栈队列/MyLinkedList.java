package liststackqueue;

public class MyLinkedList<T> implements Iterable<T> {

    private static class Node<T> {
        public T data;
        public Node<T> prev;
        public Node<T> next;

        public Node(T d, Node<T> p, Node<T> n){
            data = d;
            prev = p;
            next = n;
        }
    }

    private void addBefore(Node<T> p, T x){
        Node<T> newNode = new Node(x, p.prev, p);
        newNode.prev.next = newNode;
        p.prev = newNode;
    }

    // public MyLinkedList(){
    //     doClear();
    // }
    public java.util.Iterator<T> iterator(){
        return new LinkedListIterator();
    }
    
    private class LinkedListIterator implements java.util.Iterator<T> {

        public boolean hasNext(){
            return true; //.......
        }

        public T Next(){
            return T a;
        }
    }
}
