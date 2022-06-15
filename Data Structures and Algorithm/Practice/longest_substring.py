def lengthOfLongestSubstring(s: str) -> int:
    # lngst_str = 1 if len(s) > 0 else 0
    # str_ary = [x for x in s.strip()]
    # for i in range(0, len(str_ary)-1):
    #     cnt_ary = []
    #     count = 1
    #     for j in range(i+1, len(str_ary)):
    #         if str_ary[i] != str_ary[j]:
    #             if str_ary[j] not in cnt_ary:
    #                 cnt_ary.append(str_ary[j])
    #                 count +=1
    #             else:
    #                 break
    #         else:
    #             break
    #     if count > lngst_str:
    #         lngst_str = count
    str_dict = {}
    ln_ary = [0]
    mx = 0
    for index, item in enumerate(s):
        if item not in str_dict.keys():
            mx += 1
            # curr_mx = mx
        else:
            ln_ary.append(mx) 
            mx = index - str_dict[item]
        str_dict[item] = index
    bigst_num = max(ln_ary)
    return max(bigst_num, mx)


str_lngt = lengthOfLongestSubstring('dvfd')
print(str_lngt)


# for index, i in enumerate('abc'):
#     print(index,i)