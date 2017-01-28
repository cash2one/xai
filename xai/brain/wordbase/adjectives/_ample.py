

#calss header
class _AMPLE():
	def __init__(self,): 
		self.name = "AMPLE"
		self.definitions = [u'more than enough: ', u"If the shape of someone's body or a part of their body is ample, it is large: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
