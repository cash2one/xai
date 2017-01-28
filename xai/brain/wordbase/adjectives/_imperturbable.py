

#calss header
class _IMPERTURBABLE():
	def __init__(self,): 
		self.name = "IMPERTURBABLE"
		self.definitions = [u'always staying calm and controlled, even in difficult situations that would cause other people to worry']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
