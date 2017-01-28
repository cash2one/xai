

#calss header
class _AUTHENTIC():
	def __init__(self,): 
		self.name = "AUTHENTIC"
		self.definitions = [u'If something is authentic, it is real, true, or what people say it is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
