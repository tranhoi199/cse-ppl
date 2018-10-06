# Các quy tắc cơ bản cho thuật toán C3 Lineariztion 


A(O)        ->      [AO]



X(A,B,C)    ->      [XABC]



A(O)
B(O)
D(A,B)      ->      [DABO]



# Ví dụ thuật toán
A(O)
B(O)
C(O)
D(A,B)
E(B,C)
F(D,E,C)

-> [F] + merge(L(D), L(E), L(C), [DEC]) # merge từ các ông nội theo thứ tự rồi tới mảng các cha
-> [F] + merge([DABO], [EBCO], [CO], [DEC]) # nhẩm mấy ông nội giống quy tắc trên, nếu phức tạp thì làm bên ngoài. Nhẩm xong bắt đầu merge. Cách merge: chọn thằng đầu tiên từ trái sáng phải, sao cho nó chỉ đứng đầu trong các danh sách, ở đây thấy D ở mảng đầu tiên (trái nhất) và nó chỉ đứng đầu hoặc ko xuất hiện trong 4 mảng.
-> [FD] + merge([ABO], [EBCO], [CO], [EC]) # Ở đây, thấy A ở mảng đầu tiên mà nó chỉ đứng đầu 4 mảng 
-> [FDA] + merge([BO], [EBCO], [CO], [EC]) # Ở đây, xét theo thứ tự sẽ là B -> E -> C -> E (4 thằng đầu tiên của 4 mảng, xét từ trái sang phải), mà B ko được tại nó vi phạm trong mảng 2 (xuất hiện giữa mảng), tiếp theo chọn E, thấy E ok vì nó chỉ đầu ở mảng 2, 4, còn 1, 3 thì ko xuất hiện, nên chọn E.
-> [FDAE] + merge([BO], [BCO], [CO], [C]) # Ở đây thấy B ok
-> [FDAEB] + merge([O], [CO], [CO], [C]) # Đầu tiên thấy O ko được do vi phạm ở mảng 2, 3 (đứng sau), tiếp chọn C thấy OK, và cuối cùng là O.
-> [FDAEBCO]

Chạy code ví dụ ở file mro_2.py