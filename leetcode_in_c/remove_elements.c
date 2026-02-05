int removeElement(int* nums, int numsSize, int val) {
    int p1 = 0;
    int p2 = numsSize - 1;
    int counter = 0;
    while (nums[p2] != val) p2--; 
    while (p2 > p1)
    {
        if (nums[p1] == val)
        {
            counter++;
            nums[p1] = nums[p2];
            p1++;
            continue;
        }
        else p2--;
    }
    return (counter);
}

int main (void){
    printf("Array:")
}