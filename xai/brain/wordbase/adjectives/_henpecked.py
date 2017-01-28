

#calss header
class _HENPECKED():
	def __init__(self,): 
		self.name = "HENPECKED"
		self.definitions = [u'A henpecked man is controlled by and a little frightened of a woman, especially his wife.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
