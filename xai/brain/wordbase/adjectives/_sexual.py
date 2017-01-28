

#calss header
class _SEXUAL():
	def __init__(self,): 
		self.name = "SEXUAL"
		self.definitions = [u'relating to the activity of sex: ', u'relating to the production of young living things by the combining of a cell from a male with a cell from a female: ', u'relating to being male or female: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
