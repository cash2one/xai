

#calss header
class _RETURN():
	def __init__(self,): 
		self.name = "RETURN"
		self.definitions = [u'The return part of a journey is the part in which you go back to the place where you started: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
