

#calss header
class _UNASSAILABLE():
	def __init__(self,): 
		self.name = "UNASSAILABLE"
		self.definitions = [u'in such a strong position that you cannot be defeated: ', u'impossible to doubt or argue with: ', u'impossible to attack: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
