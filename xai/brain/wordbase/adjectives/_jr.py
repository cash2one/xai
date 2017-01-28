

#calss header
class _JR():
	def __init__(self,): 
		self.name = "JR"
		self.definitions = [u'abbreviation for  junior noun ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
