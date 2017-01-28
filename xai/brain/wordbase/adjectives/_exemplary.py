

#calss header
class _EXEMPLARY():
	def __init__(self,): 
		self.name = "EXEMPLARY"
		self.definitions = [u'very good and suitable to be copied by other people: ', u'An exemplary punishment is severe and intended as a warning to others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
