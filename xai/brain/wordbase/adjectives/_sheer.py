

#calss header
class _SHEER():
	def __init__(self,): 
		self.name = "SHEER"
		self.definitions = [u'used to emphasize how very great, important, or powerful a quality or feeling is; nothing except: ', u'extremely steep; almost vertical: ', u'Sheer clothing or material is so thin, light, and delicate that you can see through it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
