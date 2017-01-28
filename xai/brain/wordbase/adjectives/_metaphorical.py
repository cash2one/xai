

#calss header
class _METAPHORICAL():
	def __init__(self,): 
		self.name = "METAPHORICAL"
		self.definitions = [u'Metaphorical language contains metaphors: ', u'not having real existence but representing some truth about a situation or other subject: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
