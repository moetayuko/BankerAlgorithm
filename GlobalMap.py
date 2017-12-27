class GlobalMap:
    map = {}

    @classmethod
    def set(cls, key, value):
        try:
            cls.map[key] = value
            # print(key + ":" + str(value))
        except BaseException as msg:
            raise msg

    @classmethod
    def del_map(cls, key):
        try:
            del cls.map[key]
            return cls.map
        except KeyError:
            print("key:'" + str(key) + "'  不存在")

    @classmethod
    def get(cls, *args):
        try:
            dic = {}
            for key in args:
                if len(args) == 1:
                    dic = cls.map[key]
                    # print(key + ":" + str(dic))
                elif len(args) == 1 and args[0] == 'all':
                    dic = cls.map
                else:
                    dic[key] = cls.map[key]
            return dic
        except KeyError:
            return None
