using System;

class StackContexts {

    protected static void TimeIt(string note, Func<int, int> f){
        const long frequency = 10000000;  // 10 000 000 / sec, https://docs.microsoft.com/en-us/dotnet/api/system.datetime.ticks#remarks
        const long iterations = 100000000;
        int foo = 0;

        var t1 = DateTime.Now;
        for(int i = 0; i < iterations; ++i)
            foo += f(i);
        var t2 = DateTime.Now;

        Console.WriteLine(
            "{0} took {1} μs", note,
            1.0e6 /* 1/μ */ * (t2 - t1).Ticks / frequency / iterations,
            foo
        );
    }

    public static Func<int, int> UpArg = null;

    public static int Fast(int v){
        var z = v + 1;
        Func<int, int> f = (int x) => {
            return x + z;  // z is not modified
        };
        return f(v);
    }
    public static int Slower(int v){
        var z = v + 1;
        Func<int, int> f = (int x) => {
            return x + z;  // z is not modified
        };
        UpArg = f;
        return f(v);
    }

    public static int Slow(int v){
        var z = v + 1;
        Func<int, int> f = (int x) => {
            z += x;  // z is modified
            return z;
        };
        UpArg = f;
        return f(v);
    }

    public static void Main(){
        // heat up
        Fast(0);
        Slower(0);
        Slow(0);

        // benchmark
        Console.WriteLine("Press any key to benchmark");
        Console.ReadKey();
        TimeIt("Fast", Fast);
        TimeIt("Slower", Slower);
        TimeIt("Slow", Slow);
    }
}
