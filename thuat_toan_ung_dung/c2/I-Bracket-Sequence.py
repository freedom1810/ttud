s = input()

x = []
list_index = []
count = 0
final_res = ''
final_count = 0
temp_res = ''
temp_count = 0
reset_idx = 0

for i, w in enumerate(s):
    if w in '[(':
        x.append(w)
        list_index.append(i)
    if w in '])':
        if len(x) > 0:
            w_ = x.pop()
            i_ = list_index.pop()
            if (w == ']' and w_ == '[') or (w == ')' and w_ == '('):
                # temp_res = w_ + temp_res + w
                if w == ']':
                    temp_count += 1
            else:
                if temp_count > final_count:
                    final_res = s[i_ : i]
                    final_count = temp_count
                    temp_res = ''
                    temp_count = 0
                x = []
                continue
        
        else:
            if temp_count > final_count:
                final_res = s[i_ : i]
                final_count = temp_count
                temp_res = ''
                temp_count = 0
        
        if len(x) == 0:
            if temp_count > final_count:
                final_res = s[i_ : i+1]
                final_count = temp_count
                temp_res = ''
                temp_count = 0

        

print(final_count)
print(final_res)


