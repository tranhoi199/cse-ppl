import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_(self):
        input = r"""

var n, m: integer;
var a: array[0 .. 100000] of integer;

procedure main();
var i: integer;
begin
    // n := 50; m := 1997;
    n := 50000; m := 1000000009;
    a[1] := 1;
    a[2] := 2;
    for i := 3 to n do a[i] := ((3 * a[i-1]) mod m - (4 * a[i-2]) mod m + m) mod m;

    // ha_log_arr();
    ha_i_space(ha_check_arr());

    sort(1, n);

    // ha_log_arr();
    ha_i_space(ha_check_arr());
end

procedure sort(l, r: integer);
var x,i,j: integer;
begin
    if l >= r then return;
    x := (l+r) div 2;
    i := l;
    j := r;
    while i <= j do begin
        while a[i] < a[x] do i := i+1;
        while a[j] > a[x] do j := j-1;
        if i <= j then begin
            with tmp: integer; do begin 
                tmp := a[i]; a[i] := a[j]; a[j] := tmp;
            end
            i := i+1;
            j := j-1;
        end
    end
    sort(l, j);
    sort(i, r);
end

function ha_check_arr(): integer;
var i: integer;
begin
    with res: integer; do begin
        res := 0;
        for i := 1 to n do res := (res + a[i] * i mod m) mod m;
        return res;
    end
end

procedure ha_log_arr();
var i: integer;
begin
    for i := 1 to n do ha_i_space(a[i]);
    putLn();
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end

"""
        expect = r"""15123137 270342704 """
        self.assertTrue(TestCodeGen.test(input,expect,1))


"""


var n, m: integer;

procedure main();
var a: array[0 .. 100000] of integer;
    i: integer;
begin
    n := 5000;
    m := 1000000009;
    a[1] := 1;
    a[2] := 2;
    for i := 3 to n do a[i] := ((3 * a[i-1]) mod m - (4 * a[i-2]) mod m + m) mod m;
    putInt(ha_check_arr(a));
    putInt(ha_check_arr(sort(a, 1, n)));
end

function sort(a: array[0 .. 100000] of integer; l, r: integer): array[0 .. 100000] of integer;
var x: integer;
begin
    if l >= r then return a;
    x := (l+r) div 2;
    while l <= r do begin
        while a[l] < a[x] do l := l+1;
        while a[r] > a[x] do r := r-1;
        if l < r then begin
            with tmp: integer; do begin 
                tmp := a[l]; a[l] := a[r]; a[r] := tmp;
                l := l+1; r := r-1;
            end
        end
    end
    return ha_merge_arr(a, sort(a, l, x), l, x);
    //return ha_merge_arr(ha_merge_arr(a, sort(a, l, x), l, x), sort(a, x, r), x, r);
end

function ha_merge_arr(master, a: array[0 .. 100000] of integer; l,r: integer): array[0 .. 100000] of integer;
var i: integer;
begin
    for i := l to r do master[i] := a[i];
    return master;
end

function ha_check_arr(a: array[0 .. 100000] of integer): integer;
var i: integer;
begin
    with res: integer; do begin
        res := 0;
        for i := 1 to n do res := (res + a[i] * i mod m) mod m;
        return res;
    end
end

procedure ha_log_arr(a: array[0 .. 100000] of integer);
var i: integer;
begin
    for i := 1 to n do ha_i_space(a[i]);
end

procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end





procedure ha_i_space(ha0852i: integer); begin putInt(ha0852i); putString(" "); end
procedure ha_f_space(ha0852f: real); begin putFloat(ha0852f); putString(" "); end
procedure ha_b_space(ha0852b: boolean); begin putBool(ha0852b); putString(" "); end

function ha_str_1(): string; begin return "0852 1"; end
function ha_str_2(): string; begin return "0852 2"; end
function ha_str_3(): string; begin return "0852 3"; end

"""