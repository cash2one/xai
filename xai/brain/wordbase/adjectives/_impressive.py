

#calss header
class _IMPRESSIVE():
	def __init__(self,): 
		self.name = "IMPRESSIVE"
		self.definitions = [u'If an object or achievement is impressive, you admire or respect it, usually because it is special, important, or very large: ', u'If someone is impressive, you admire or respect that person for their special skills or abilities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
