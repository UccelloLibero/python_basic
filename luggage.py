def packer(name=None, **kwargs):
    print(kwargs)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


packer(name="BlahBlah", num=42, spanish_inquisition=None)
unpacker(**{"last_name": "YoYo", "first_name":"Yo"})
