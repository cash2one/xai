

#calss header
class _ATTRIBUTIVE():
	def __init__(self,): 
		self.name = "ATTRIBUTIVE"
		self.definitions = [u'(of the position or use of an adjective, noun, or phrase) before a noun: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
