

#calss header
class _THREATENING():
	def __init__(self,): 
		self.name = "THREATENING"
		self.definitions = [u'expressing a threat of something unpleasant or violent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
