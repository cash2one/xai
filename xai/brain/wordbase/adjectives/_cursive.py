

#calss header
class _CURSIVE():
	def __init__(self,): 
		self.name = "CURSIVE"
		self.definitions = [u'Cursive writing is written with rounded letters that are joined together.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
