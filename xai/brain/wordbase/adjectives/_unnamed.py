

#calss header
class _UNNAMED():
	def __init__(self,): 
		self.name = "UNNAMED"
		self.definitions = [u'An unnamed person or thing is talked about, but their name is not known or mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
