

#calss header
class _VISIBLE():
	def __init__(self,): 
		self.name = "VISIBLE"
		self.definitions = [u'able to be seen: ', u'able or likely to attract public attention and be noticed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
