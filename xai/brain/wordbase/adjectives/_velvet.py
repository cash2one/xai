

#calss header
class _VELVET():
	def __init__(self,): 
		self.name = "VELVET"
		self.definitions = [u'made of velvet: ', u'Something that is velvety has a beautiful soft, smooth quality or appearance, usually something dark or deep: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
