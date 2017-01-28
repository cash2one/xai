

#calss header
class _REMINISCENT():
	def __init__(self,): 
		self.name = "REMINISCENT"
		self.definitions = [u'making you remember a particular person, event, or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
