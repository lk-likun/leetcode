import pathlib

filePath = r'E:\highkick\[搞XY家人 3][ 微信公众号：林买买 ]'
p = pathlib.Path(filePath)
for f in p.glob("*.pdf"):
    f.replace(f.parent.parent.joinpath(f.name[:-4]))