

#calss header
class _RUSHED():
	def __init__(self,): 
		self.name = "RUSHED"
		self.definitions = [u'done in a hurry, or feeling that you must do something quickly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
