

#calss header
class _INDISCREET():
	def __init__(self,): 
		self.name = "INDISCREET"
		self.definitions = [u'saying or doing things that tell people things that should be secret or that embarrass people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
