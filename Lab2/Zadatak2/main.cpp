#include <iostream>
#include <string>
#include <vector>
#include <set>

template <typename Iterator, typename Predicate>
Iterator mymax (    // TEMPLATE AND PARAMETERS ARE TASK-GIVEN
    Iterator first, Iterator last, Predicate pred){
    if (first == last) return last; // empty range

    Iterator max = first;
    for (Iterator it = first; it != last; ++it) {
        if (pred(*it, *max) == 1) max = it;
    }
    return max;
}

int gt_int(const int& a, const int& b) {
    return a > b;
}

int gt_char(char a, char b) {
    return a > b;
}

int gt_str(const std::string& a, const std::string& b) {
    return a > b;
}

int main() {
    int arr_int[] = { 1, 3, 5, 7, 4, 6, 9, 2, 0 };
    const int* maxint = mymax(&arr_int[0], &arr_int[sizeof(arr_int)/sizeof(*arr_int)], gt_int);
    std::cout << "Max int: " << *maxint << "\n";
    
    char arr_char[] = "Suncana strana ulice";
    const char* maxchar = mymax(&arr_char[0], &arr_char[sizeof(arr_char)/sizeof(*arr_char)], gt_char);
    std::cout << "Max char: " << *maxchar << "\n";

    const char* arr_str[] = {"Gle", "malu", "vocku", "poslije", "kise", "Puna", "je", "kapi", "pa", "ih", "njise"};
    const char** maxstr = mymax(&arr_str[0], &arr_str[sizeof(arr_str)/sizeof(*arr_str)], gt_str);
    std::cout << "Max string: " << *maxstr << "\n";
    
    std::string s = "Suncana strana ulice";
    const char* maxstr2 = mymax(&s[0], &s[s.size()], gt_char);
    std::cout << "Max string2: " << *maxstr2 << "\n";
    
    std::set<std::string> set_str = {"Gle", "malu", "vocku", "poslije", "kise", "Puna", "je", "kapi", "pa", "ih", "njise"};
    auto maxset = mymax(set_str.begin(), set_str.end(), gt_str);
    std::cout << "Max set: " << *maxset << "\n";

    std::vector<std::string> vec_str = {"Gle", "malu", "vocku", "poslije", "kise", "Puna", "je", "kapi", "pa", "ih", "njise"};
    auto maxvec = mymax(vec_str.begin(), vec_str.end(), gt_str);
    std::cout << "Max vector: " << *maxvec << "\n";

    return 0;
}