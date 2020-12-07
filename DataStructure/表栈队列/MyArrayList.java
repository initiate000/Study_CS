package liststackqueue;

public class MyArrayList<T> implements Iterable<T> {
    private static final int DEFAULT_CAPACITY = 10;

    private int theSize;
    private T [] theItems;

    public MyArrayList() {
        doClear();
    }

    public void clear() {
        doClear();
    }

    private void doClear() {
        theSize = 0;
        ensureCapacity(DEFAULT_CAPACITY);
    }

    public int size() {
        return theSize;
    }

    public boolean isEmoty() {
        return size() == 0;
    }

    public void trimToSize() {
        ensureCapacity(size());
    }

    public T get(int idx){
        if(idx < 0 || idx > size()) {
            throw new ArrayIndexOutOfBoundsException();
        }
        return theItems[idx];
    }

    public T set(int idx, T newVal) {
        if(idx < 0 || idx > size()) {
            throw new ArrayIndexOutOfBoundsException();
        }
        T old = theItems[idx];
        theItems[idx] = newVal;
        return old;
    }

    public void ensureCapacity(int newCapacity) {
        if(newCapacity < theSize){
            return;
        }
        T [] old = theItems;
        theItems = (T []) new Object[newCapacity];
        for (int i = 0; i < size(); i++){
            theItems[i] = old[i];
        }
    }

    public boolean add(T x){
        add(size(), x);
        return true;
    }

    public void add(int idx, T x){
        if(theItems.length == size()){
            ensureCapacity(size()*2+1);
        }
        // 整体平移
        for(int i = theSize; i > idx; i--){
            theItems[i] = theItems[i-1];
        }
        theItems[idx] = x;
        
        theSize++;
    }

    public T remove(int idx){
        T removeItem = theItems[idx];
        for(int i = idx; i < size(); i++){
            theItems[i] = theItems[i+1];
        }

        theSize--;
        return removeItem;
    }
    
    public java.util.Iterator<T> iterator(){
        return new ArrayListIterator();
    }

    /**
     * 内部类实现ArrayListIterator接口，size()是MyArrayList.this.size()的简记符，theItems同理。remove()是用MyArrayList.this.remove()是为了避免冲突。
     */
    public class ArrayListIterator implements java.util.Iterator<T>{
        private int current = 0;

        public boolean hasNext(){
            return current < size();
        }

        public T next(){
            if(!hasNext()){
                throw new java.util.NoSuchElementException();
            }
            return theItems[current++];
        }
        
        @Override
        public void remove(){
            MyArrayList.this.remove(--current);
        }
    }

    /**
     * 使用嵌套类来实现ArrayListIterator接口。
     */
    // private static class ArrayListIterator<T> implements java.util.Iterator<T> {
    //     private int current = 0;
    //     private MyArrayList<T> theList;

    //     public ArrayListIterator(MyArrayList<T> list){
    //         theList = list;
    //     }

    //     public boolean hasNext(){
    //         return current < theList.size();
    //     }
    //     public T next(){
    //         if(!hashasNext()){
    //             throw new java.util.NoSuchElementException();
    //         }
    //         return theList.theItems[current++];
    //     }

    // }
}
