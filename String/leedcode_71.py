'''
简化路径

以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

示例 1：
输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。

示例 2：
输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。

示例 3：
输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

示例 4：
输入："/a/./b/../../c/"
输出："/c"

示例 5：
输入："/a/../../b/../c//.//"
输出："/c"

示例 6：
输入："/a//b////c/d//././/.."
输出："/a/b/c"

思路一：不用split
路径问题考察栈
用栈存储有效文件路径的名字（即文件夹名），最后用"/"连接返回结果。
遍历path，忽略第一个"/"
遇到非"/"存储在临时字符数组fold_name
遇到"/"时，判断fold_name是否为有效文件夹名
如果fold_name是"."或者""（连续两个"/"）,忽略跳过，将fold_name重置为空
如果是".."，弹栈
如果是其他有效名，入栈
记得每次判断完fold_name后要重置为空

思路2：使用split
用split切割path，遍历每个文件夹名，进行分类讨论。其他步骤同上。

结果：
思路1
72ms通过
思路2
32ms
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        '''
        不用split
        '''
        # dir_stack = []
        # fold_name = ""
        # for ind, c in enumerate(path):
        #     if ind == 0:
        #         continue
        #     if c != "/":
        #         fold_name += c
        #     if c == "/" or ind == len(path) - 1:
        #         if fold_name == "." or fold_name == "":
        #             fold_name = ""
        #             continue
        #         elif fold_name == "..":
        #             if len(dir_stack) > 0:
        #                 dir_stack.pop()
        #         else:
        #             dir_stack.append(fold_name)
        #         fold_name = ""
        #
        # return "/" + "/".join(dir_stack)

        '''
        思路二
        '''
        dir_stack = []
        foldname_list = path.split("/")
        for foldname in foldname_list:
            if foldname == "." or foldname == "":
                continue
            elif foldname == "..":
                if len(dir_stack) > 0:
                    dir_stack.pop()
            else:
                dir_stack.append(foldname)
        return "/{}".format("/".join(dir_stack))

if __name__ == "__main__":
    sol = Solution()
    print(sol.simplifyPath("/a//b////c/d//././/.."))