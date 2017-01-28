

#calss header
class _MILKY():
	def __init__(self,): 
		self.name = "MILKY"
		self.definitions = [u'A milky liquid contains milk or is made with a lot of milk: ', u'white, pale, or not transparent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
