digraph G {

 b [shape="rectangle", label="Начало"];
 m1 [shape="rectangle", label="М 1\nV=960 O=4560"];

 m1a0 [shape="rectangle", label="М 1 A 0\nV=960 O=4158", color=red];

 m1a1 [shape="rectangle", label="М 1 A 1\nV=4584 O=4584"];
                                                 
 m1a2 [shape="rectangle", label="М 1 A 2\nV=3360 O=4656"];

 m1a3 [shape="rectangle", label="М 1 A 3\nV=4560 O=4728"];

 m0   [shape="rectangle", label="М 0\nV=0 O=4290", color=red];

 m1a1_ [shape="none", label="..."];
 m1a2_ [shape="none", label="..."];
 m1a3_ [shape="none", label="..."];

 b -> m1;
 b -> m0;
 m1 -> m1a3 -> m1a3_;
 m1 -> m1a2 -> m1a2_; 
 m1 -> m1a1 -> m1a1_;
 m1 -> m1a0;
}