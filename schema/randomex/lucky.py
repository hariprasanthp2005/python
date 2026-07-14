from random import choice,choices

enames=["hp","vk","ab","cg","rp","bk","faf","dsp","ddp","jb"]

luck_name=choice(enames)
print(luck_name)

luck_draw_List=choices(enames,k=3)
luck_draw_List=choices(enames,3)

print(luck_draw_List)