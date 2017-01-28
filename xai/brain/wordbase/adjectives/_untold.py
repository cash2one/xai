

#calss header
class _UNTOLD():
	def __init__(self,): 
		self.name = "UNTOLD"
		self.definitions = [u'so great in amount or level that it can not be measured or expressed in words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
