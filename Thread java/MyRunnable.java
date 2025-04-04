class MyRunnable implements Runnable 
{
    public void run() {
        System.out.println(Thread.currentThread().getName() + " is running.");
    }

    public static void main(String[] args) {
        MyRunnable task = new MyRunnable();

        Thread t1 = new Thread(task, "Thread A");
        Thread t2 = new Thread(task, "Thread B");

        t1.start();
        t2.start();
    }
}
