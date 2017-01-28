

#calss header
class _FORCED():
	def __init__(self,): 
		self.name = "FORCED"
		self.definitions = [u'done against your wishes: ', u'An action that is forced is done because it is suddenly made necessary by a new and usually unexpected situation: ', u'used to describe laughter, a smile, or an emotion that is produced with effort and is not sincerely felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
