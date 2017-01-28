

#calss header
class _FOUL():
	def __init__(self,): 
		self.name = "FOUL"
		self.definitions = [u'extremely unpleasant: ', u'Foul speech or other language is offensive, rude, or shocking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
