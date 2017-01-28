

#calss header
class _MAMMARY():
	def __init__(self,): 
		self.name = "MAMMARY"
		self.definitions = [u'relating to the breasts or milk organs']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
