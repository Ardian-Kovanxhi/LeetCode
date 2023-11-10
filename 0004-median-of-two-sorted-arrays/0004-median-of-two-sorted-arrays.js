/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    const arr = nums1.concat(nums2).sort((a,b) => a-b);
    if (arr.length % 2) return arr[Math.floor(arr.length / 2)];
    return (arr[Math.floor(arr.length / 2) - 1] + arr[Math.ceil(arr.length / 2)]) / 2;
};