"""问题：现有红白蓝三个不同颜色的小球，乱序排列在一起，请重新排列这些小球，使得红白蓝三色的同颜色的球在一起。这个问题之所以叫荷兰国旗问题，
是因为我们可以将红白蓝三色小球想象成条状物，有序排列后正好组成荷兰国旗。
分析：先计算每种颜色有多少个，然后将不同颜色排列,可推广到n种不同颜色的小球。"""
def re_sort(a):
    l = [0,0,0]
    ls=[]
    for i in a:
        #计算每种颜色球的个数
        l[i]+=1
    for k in range(3):
        for g in range(l[k]):
            #按每种球排列
            ls.append(k)
    return ls
