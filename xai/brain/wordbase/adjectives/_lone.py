

#calss header
class _LONE():
	def __init__(self,): 
		self.name = "LONE"
		self.definitions = [u'alone: ', u'someone who has children but no partner living with them']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
