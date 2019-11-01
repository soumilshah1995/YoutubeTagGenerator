
try:

    import  requests
    import ast
except Exception as e:
    print("Some Modules are Missings ")

class MetaClass(type):

    """ Meta class """

    _instance = {}

    def __call__(cls, *args, **kwargs):

        """ Implementing Singleton Design Pattern  """

        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]

    def __init__(cls, name, base, attr):

        """ Defining Your Own Rules  """

        if cls.__name__[0].isupper():

            """ Create class only if First Letter is Capital    """

            for k, v in attr.items():
                if hasattr(v, '__call__'):

                    if v.__name__[0] == '_' or v.__name__[0].islower():

                        """  check name function starts with _ or lower case  """

                        if v.__doc__ is None:

                            """  Check is User has provided Documentation """

                            raise ValueError("Make sure to Provide Documentation check {}".format(v.__name__))
                        else:

                            """ if function has Doccumentation pass """

                            pass
                    else:

                        """ function name starts with upper case throw error  """

                        raise ValueError("Function should start with Lower case :{}".format(v.__name__))
        else:
            raise ValueError("Class Name  should start with Capital Letter :{} ".format(cls.__name__[0]))


class YoutubeTagGenerator(metaclass=MetaClass):

    def __init__(self,title = 'Python Data structure'):

        """constructor  """

        self.__headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive',}
        self.__url = "https://rapidtags.io/api/index.php?tool=tag-generator"
        self.title = title
        self.query_string ={
            "tool": "tag-generator",
            "input": "{}".format(self.title)}

    @property
    def getTags(self):
        """ return list """
        r = requests.get(url=self.__url, headers=self.__headers, params=self.query_string)
        data = ast.literal_eval(r.text)
        return data

if __name__ == "__main__":
    obj = YoutubeTagGenerator(title="Python Data Structure ")
    print(obj.getTags)