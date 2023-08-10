# https://leetcode.com/discuss/interview-question/3597465/Wayfair-or-SDE-2-(L2-4)-or-Bengaluru-or-OA
# There is a list of encrypted files of size n, each with a different value, and a
# list of n binary values. A value of 1 represents a file that has been
# decrypted, and 0 represents an encrypted file that is not yet decrypted.
# The value sum of the encrypted files is the sum of all values of the files
# where the corresponding value in the binary list is 1. In a single operation,
# a group of up to k encrypted files can be decrypted simultaneously.
#
# The values of the encrypted files and the binary list are given, along with
# the maximum number of encrypted files that can be decrypted in a single
# operation. Find the maximum possible value sum of the decrypted files.
#
# Note: A group, i.e., subarray is defined as any contiguous segment of the
# array.
#
# Example  1
# Given n =4, k =2, encrypted _file =[7, 4, 3, 5], and binary =[1, 0, 0, 0].
# Here the answer is 15.
#
# Example 2
# Given n=6,k=3,encrypted_files = [1,3,5,2,5,4] and binary = [1,1,0,1,0,0]
# answer is 16
# since you can decrypt 3rd and 5th element
#
# Question Type : Generic
# Used : solve using sliding window
