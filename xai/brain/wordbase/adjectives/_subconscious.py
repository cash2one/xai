

#calss header
class _SUBCONSCIOUS():
	def __init__(self,): 
		self.name = "SUBCONSCIOUS"
		self.definitions = [u'relating to this part of your mind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
