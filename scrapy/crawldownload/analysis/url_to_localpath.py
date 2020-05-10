import os

# www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2019h31.html というパス名を取得する
str = 'https://www.jitec.ipa.go.jp/1_04hanni_sukiru/mondai_kaitou_2019h31_2/2019r01a_sg_am_qs.pdf'
p = str.split("/")

p.pop(0)
p.pop(0)

print(os.path.join(*p))