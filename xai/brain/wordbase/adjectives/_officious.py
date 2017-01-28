

#calss header
class _OFFICIOUS():
	def __init__(self,): 
		self.name = "OFFICIOUS"
		self.definitions = [u'too eager to tell people what to do and having too high an opinion of your own importance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
